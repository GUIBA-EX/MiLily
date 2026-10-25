"""Rebuild README performance figures. Requires matplotlib; run from any directory."""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
def read(p):
    with (ROOT/p).open() as f:return list(csv.DictReader(f))
rows=read('results/comparison.csv'); metrics={r['scheme']:r for r in read('results/taxonomic_comparison.csv')}
for r in rows:
 r['coverage_pct']=metrics[r['scheme']]['order_coverage_pct'];r['exact_pct']=metrics[r['scheme']]['order_exact_pct']
seq={r['name']:r for r in read('sequences/primer_pairs.csv')}
strict={r['name']:r for r in read('results/xs/strict_background_comparison.csv')}
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'axes.labelcolor':'#233949','text.color':'#233949','svg.fonttype':'none','savefig.facecolor':'white'})
colors={'XS':'#dc6876','S':'#209b9b','M':'#d99b27','L':'#3987c9','XL':'#9566b1'}
def save(fig,name):
    fig.savefig(ROOT/'figures'/f'{name}.svg',bbox_inches='tight')
    fig.savefig(ROOT/'figures'/f'{name}.png',bbox_inches='tight',dpi=180)
    plt.close(fig)
names=[r['scheme'] for r in rows]; y=np.arange(len(rows))
fig,ax=plt.subplots(figsize=(10,6.4))
cv=[float(r['coverage_pct']) for r in rows]; ex=[float(r['exact_pct']) for r in rows]
ax.barh(y,cv,height=.65,color='#dbe9ed',label='Coverage')
ax.barh(y,ex,height=.65,color='#268a97',label='Exact matching')
for i,(c,e) in enumerate(zip(cv,ex)):
    ax.text(102,i,f'{c:.0f}% / {e:.0f}%',va='center',fontsize=9)
ax.set(yticks=y,yticklabels=names,xlim=(0,122),xticks=[0,20,40,60,80,100],xlabel='Order-balanced matching (%)')
ax.invert_yaxis(); ax.set_title('Target matching across 13 primer portfolios',loc='left',fontweight='bold',pad=28)
ax.text(0,1.02,'Common panel: 27 references / 25 labels     |     Right column: coverage / exact',transform=ax.transAxes,fontsize=9)
ax.legend(loc='upper center',bbox_to_anchor=(.5,-.12),ncol=2,frameon=False); ax.grid(axis='x',alpha=.15); ax.set_axisbelow(True)
fig.tight_layout();save(fig,'performance_matching')
fig,(a,b)=plt.subplots(1,2,figsize=(12,6.5),gridspec_kw={'width_ratios':[1,1.2]})
selected=['XS','SD','MD','LD','XLD']; sy=np.arange(5)
a.barh(sy,[int(strict[n]['WC_le2last3']) for n in selected],color='#c4dfe3',height=.6,label='Strict matching')
a.barh(sy,[int(strict[n]['WC_exact']) for n in selected],color='#dd785c',height=.6,label='Exact matching')
for i,n in enumerate(selected):a.text(int(strict[n]['WC_le2last3'])+.4,i,f"{strict[n]['WC_le2last3']} / {strict[n]['WC_exact']}",va='center')
a.set(yticks=sy,yticklabels=selected,xlim=(0,24),xlabel='Non-target records (linear scale)');a.invert_yaxis()
a.set_title('A  Strict and exact hits: degenerate pairs',loc='left',fontsize=11,fontweight='bold');a.legend(loc='lower right',frameon=False,fontsize=9)
for shift,key,col,label in [(-.22,'WC3','#388fa4','WC3'),(0,'GT2','#d69a30','GT2'),(.22,'WC4','#9b77af','WC4')]:
    vals=[int(r[key]) for r in rows]
    b.scatter(vals,y+shift,color=col,s=24,label=label)
# explicitly report all three counts to make zeros and near-overlap readable
for i,r in enumerate(rows):b.text(7000,i,f"{r['WC3']} / {r['GT2']} / {r['WC4']}",va='center',fontsize=8)
b.set_xscale('symlog',linthresh=1);b.set(xlim=(-.15,150000),yticks=y,yticklabels=names,xticks=[0,1,10,100,1000],xlabel='Non-target records (symlog; includes zero)');b.invert_yaxis()
b.set_title('B  Permissive paired-hit screens',loc='left',fontsize=11,fontweight='bold');b.legend(loc='upper center',bbox_to_anchor=(.5,-.12),ncol=3,frameon=False,fontsize=9)
for ax in (a,b):ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
fig.suptitle('Background matching: 7,177 non-crinoid references',x=.07,ha='left',fontweight='bold',fontsize=14)
fig.tight_layout(rect=(0,0,1,.95));save(fig,'performance_background')
fig,(a,b)=plt.subplots(1,2,figsize=(11,4.6))
for i,n in enumerate(selected):
 r=next(r for r in rows if r['scheme']==n);c=colors[r['region']]
 lo,hi=int(r['product_min']),int(r['product_max']);ref=int(seq[n]['reference_span'])
 a.plot([lo,hi],[i,i],lw=7,color=c,solid_capstyle='round');a.scatter([ref],[i],marker='D',s=45,color='white',edgecolor='#233949',zorder=3)
 a.text(hi+8,i,f'{lo}–{hi}',va='center',fontsize=9)
 for offset,key in [(-.17,'degeneracy_F'),(.17,'degeneracy_R')]:
  v=int(seq[n][key]);b.barh(i+offset,v,height=.28,color=c,alpha=1 if offset<0 else .45)
  b.text(v+1,i+offset,str(v),va='center',fontsize=9)
a.set(yticks=range(5),yticklabels=selected,xlim=(140,540),xlabel='Primer-inclusive length (bp)');a.invert_yaxis();a.set_title('A  Product ranges: full target scan',loc='left',fontweight='bold',fontsize=11)
a.text(.02,.02,'Diamond: AF049132.1 reference span',transform=a.transAxes,fontsize=9)
b.set(yticks=range(5),yticklabels=selected,xlim=(0,76),xlabel='Concrete sequence variants per primer');b.invert_yaxis();b.set_title('B  Degeneracy per direction',loc='left',fontweight='bold',fontsize=11)
b.text(.35,.02,'Solid: forward   |   Pale: reverse',transform=b.transAxes,fontsize=9)
for ax in (a,b):ax.grid(axis='x',alpha=.15);ax.set_axisbelow(True)
fig.suptitle('Length and synthesis complexity of degenerate single pairs',x=.07,ha='left',fontweight='bold',fontsize=14)
fig.tight_layout(rect=(0,0,1,.94));save(fig,'performance_design')

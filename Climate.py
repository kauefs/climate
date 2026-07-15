# Libraries
import     pandas        as pd
import  streamlit        as st
import matplotlib.pyplot as plt
import    seaborn        as sns
# Configs
plt.rcParams[  'font.family'    ]='sans-serif'
plt.rcParams['figure.autolayout']= True
st.set_page_config(page_title='CW&GC', page_icon='🔥', layout='wide', initial_sidebar_state='collapsed')
# DATA
DATA         = 'datasets/VCP.csv'
@st.cache_data
def LoadData( ):
    rename   ={'casos-confirmados'   :'Cases',
               'chuva'               :'Rain' ,
               'temperatura-mininima':'Min'  ,
               'temperatura-media'   :'Mean' ,
               'temperatura-maxima'  :'Max'  }
    try:data =  pd.read_csv(DATA, index_col='data', parse_dates=True)
    except Exception:
        # FallBack
        dates=  pd.date_range(start='1998-01-01', end='2014-12-31', freq='D')
        data =  pd.DataFrame(index=dates, columns=list(rename.keys( )))
        data  ['temperatura-mínima']=15.
        data  ['temperatura-media' ]=22.
        data  ['temperatura-maxima']=30.
        data  [            'chuva' ]= 5.
    data     =  data.rename(columns=rename     )
# Cleaning
    data     =  data.fillna({'Rain':      0.00})
# Selecting
    columns  =['Min','Mean','Max','Rain']
    return      data[columns]
df           =  LoadData( )
# SIDE
st.sidebar.title    ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider  (                     )
st.sidebar.success  ('Climate Warming'    )
st.sidebar.info     ('Global  Change '    )
st.sidebar.divider  (                     )
st.sidebar.subheader('Data   Analysis'    )
st.sidebar.markdown (f"Source: [CIIAGRO](https://ciiagro.sp.gov.br/) – temperature & precipitation reports from {df.index.min( ).strftime('%Y.%m.%d')} to {df.index.max( ).strftime('%Y.%m.%d')}")
table       = st.sidebar.empty( )
st.sidebar.divider  (           )
st.sidebar.markdown ('''
![2023.11.23   ](https://img.shields.io/badge/2023.11.23-000000)

[![License     ](https://img.shields.io/badge/Apache--2.0-D22128?&logo=apache&logoColor=CB2138&label=License&labelColor=6D6E71)](https://www.apache.org/licenses/LICENSE-2.0)

[![GitHub      ](https://img.shields.io/badge/-000000?logo=github&logoColor=FFFFFF)](https://github.com/kauefs/)
[![Medium      ](https://img.shields.io/badge/-000000?logo=medium&logoColor=FFFFFF)](https://medium.com/@kauefs)
[![LinkedIn    ](https://img.shields.io/badge/in-0077B5?logo=linkedin&logoColor=FFFFFF)](https://www.linkedin.com/in/kauefs/)
[![Python      ](https://img.shields.io/badge/3-646464?logo=python&logoColor=FFDE57&labelColor=4584B6)](https://www.python.org/)

[![ƊⱭȾɅViƧi🧿Ƞ](https://img.shields.io/badge/ƊⱭȾɅViƧi🧿Ƞ&trade;-0065FF?style=plastic&logoColor=0065FF&label=&copy;2023&labelColor=0065FF)](https://datavision.one/)
                     ''')
# MAIN
st.divider (                         )
st.title   ('In Search of a Warming!')
st.divider (                         )
st.markdown('''
After observing a climate series from 1998 to 2014 for the city of Campinas/SP, in Brazil, it is hard to see, from the data, any temperature anomaly.
Minimum and maximum temperatures have been stable, with close mean and median, resulting, as consequence, in a small standard deviation,
which is further verified by the small distance among the quantiles, thus, confirming no notable change in temperatures in the region during the analyzed period.

Therefore, one may wonder where is all that global warming claimed by everyone, everywhere, because it does not show in the data!
            ''')
# Chart
st.subheader('Chart')
st.write    (f"➡️ Showing temperature & precipitation reports from {df.index.min( ).strftime('%Y.%m.%d')} to {df.index.max( ).strftime('%Y.%m.%d')}")
# Altogheter with Bar
fig,ax=plt.subplots(figsize=(20, 10), frameon=True, tight_layout=True)
# Maximum Temperature
df['Max'].plot (kind     = 'line' , ax=ax,
                linewidth= '3.25' ,
                linestyle='dashed',
                color    ='maroon') #FF4500
# Mean    Temperature
df['Mean'].plot(kind     = 'line'  , ax=ax,
                linewidth= '3.25'  ,
                linestyle= 'solid' ,
                color    ='#4CAF50')
# Minimum Temperature
df['Min'].plot (kind     = 'line'  , ax=ax,
                linewidth= '3.25'  ,
                linestyle='dotted' ,
                color    ='#0065FF')
# Rain
ax .bar(df.index, df['Rain']/25, color='DeepSkyBlue', width=.75)
ax .set_title(f"Temperature (ºC) & Precipitation (mm/25) for Campinas/SP (Brazil) from {df.index.min( ).strftime('%Y')} to {df.index.max( ).strftime('%Y')}",
             fontsize=25, fontweight='semibold', loc='center')
ax .set_xlabel(None)
for spine in ['top','right','left','bottom']:ax.spines[spine].set_visible(False)
ax .tick_params(axis='both' , which='both', left=False, bottom=False)
plt.grid(axis='y', linestyle=':', linewidth=3.15, color='#DCDCDC')
plt.ylim(0, 35)
leg=ax.legend(['Max','Mean','Min','Rain'], loc='upper center', ncol=4, fontsize=20, frameon=False)
plt.gca( ).add_artist(leg)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
st .pyplot(fig)
st .divider(  )
# HeatMap
A, B = st.columns(2)
with A:
    st.subheader('Heat Map')
    st.markdown ('''
                 As it can be seen, there is a loose correlation of about 50% between temperature and precipitation,
                 meaning high temperatures do not automatically translate to more rain,
                 as it can be observed in places with severe drought around the world.
                 ''')
with B:
    fig2,ax2=plt.subplots(frameon=True, tight_layout=True)
    ax      =sns.heatmap (df.corr(   ),
                          fmt         ='.2f',
                          cbar        = True,
                          annot       = True,
                          square      = True,
                          cmap        ='autumn_r',
                          linewidths  =        1 ,
                          linecolor   ='#FFFFFF',
                          ax          = ax2)
    ax2.xaxis.tick_top( )
    ax2.tick_params(axis='both', which='both', length=0)
    ax2.collections[0].colorbar.ax.tick_params(length=0)
    st .pyplot(fig2)
st.divider( )
# Columns
L, R    =st.columns(2)
with L:
    st.subheader('Summary Statistics')
    st.dataframe(df.describe( ).round(2), width='stretch')
with R:
    st.subheader('Correlation Matrix')
    st.dataframe(df.corr    ( ).round(2), width='stretch')
st.divider( )
# DataFrame
if table.checkbox('DataFrame', value=False):
    st.subheader ('DATA')
    st.write     (f"➡️ Showing temperature & precipitation reports from {df.index.min( ).strftime('%Y.%m.%d')} to {df.index.max( ).strftime('%Y.%m.%d')}")
    st.dataframe (df, width='stretch')
    st.divider(  )
st.toast('Climate Terrorism!', icon='🔥')

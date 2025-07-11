# Libraries:
import     pandas        as pd
import  streamlit        as st
import matplotlib.pyplot as plt
import    seaborn        as sns
st.set_page_config(page_title='CW&GC', page_icon='🔥', layout='wide', initial_sidebar_state='collapsed')
# DATA:
DATA       = 'datasets/VCP.csv'
@st.cache_data
def load_data():
    rename ={'casos-confirmados'   :'Cases',
             'chuva'               :'Rain' ,
             'temperatura-mininima':'Min'  ,
             'temperatura-media'   :'Mean' ,
             'temperatura-maxima'  :'Max'  }
    data   =  pd.read_csv(DATA, index_col='data', parse_dates=True)
    #data.index  = data.index.date
    data   =  data.rename(columns=rename     )
# Cleaning:
    data   =  data.fillna({'Rain':      0.00})
# Selecting:
    columns=['Min' ,
             'Mean',
             'Max' ,
             'Rain']    
    data    = data[list(columns)]
    return    data
df          = load_data( )
# SIDE:
st.sidebar.title    ('ƊⱭȾɅViƧi🧿Ƞ&trade;')
st.sidebar.divider  (                     )
st.sidebar.success  ('Climate Warming'    )
st.sidebar.info     ('Global  Change '    )
st.sidebar.divider  (                     )
st.sidebar.subheader('Data   Analysis'    )
st.sidebar.markdown ('''Source: [CIIAGRO](https://ciiagro.sp.gov.br/) – temperature & precipitation reports from {} to {}'''
                    .format(df.index.min( ), df.index.max( )))
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
# MAIN:
st.divider (                         )
st.title   ('In Search of a Warming!')
st.divider (                         )
st.markdown('''
After observing a climate series from 1998 to 2014 for the city of Campinas/SP, in Brazil, it is hard to see, from the data, any temperature anomaly.
Minimum and maximum temperatures have been stable, with close mean and median, resulting, as consequence, in a small standard deviation,
which is further verified by the small distance among the quantiles, thus, confirming no notable change in temperatures in the region during the analyzed period.

Therefore, one may wonder where is all that global warming claimed by everyone, everywhere, because it does not show in the data!
            ''')
# Chart:
st.subheader('Chart')
st.write    ('➡️ Showing temperature & precipitation reports from {} to {}'.format(df.index.min( ), df.index.max( )))
# Altogheter with Bar:
fig,ax=plt.subplots(figsize=(20, 10), tight_layout=True)
plt.rcParams['font.family']='sans-serif'
# Maximum Temperature:
df['Max'].plot (kind     = 'line' , ax=ax,
                linewidth= '3.25' ,
                linestyle='dashed',
                color    ='maroon') #FF4500
# Mean    Temperature:
df['Mean'].plot(kind     = 'line'  , ax=ax,
                linewidth= '3.25'  ,
                linestyle= 'solid' ,
                color    ='#4CAF50')
# Minimum Temperature:
df['Min'].plot (kind     = 'line'  , ax=ax,
                linewidth= '3.25'  ,
                linestyle='dotted' ,
                color    ='#0065FF')
# Rain:
plt.bar(df.index, df['Rain']/25, color='DeepSkyBlue', width=.75)
ax.set_title('Temperature (ºC) & Precipitation (mm/25) for Campinas/SP (Brazil) from 1998 to 2014',
             fontsize=25, fontweight='semibold', loc='center')
ax.set_xlabel(None)
for spine in ['top','right','left','bottom']:ax.spines[spine].set_visible(False)
ax.tick_params(axis   =     'both',
               which  =     'both',
               left   =      False,
               bottom =      False)
plt.grid(axis='y', linestyle=':', linewidth=3.15, color='#DCDCDC', label='Rain')
plt.ylim(0, 35)
leg=plt.legend(['Max','Mean','Min','Rain'], loc='upper center', ncol=4, fontsize=20, frameon=False)
plt.gca( ).add_artist(leg)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.show (   )
st.pyplot(fig)
st.divider(  )
# HeatMap:
A, B = st.columns(2)
with A:
    st.subheader('Heat Map')
    st.markdown ('''
                 As it can be seen, there is a loose correlation of about 50% between temperature and precipitation,
                 meaning high temperatures do not automatically translate to more rain,
                 as it can be observed in places with severe drought around the world.
                 ''')
with B:
    sns.set_style( )
    fig, ax =plt.subplots(tight_layout=True)
    ax      =sns.heatmap (df.corr(   ),
                          fmt         ='.2f',
                          cbar        = True,
                          annot       = True,
                          square      = True,
                          cmap        ='autumn_r',
                          linewidths  =        1 ,
                          linecolor   ='white')
    ax.xaxis.tick_top( )
    plt.show (   )
    st.pyplot(fig)
st.divider( )
# Columns:
L, R    =st.columns(2)
with L:
    st.subheader('Statistics Summary')
    S   =df.describe( ).round(2)
    S
with R:
    st.subheader('Correlation Matrix')
    corr=df.corr( ).round(2)
    corr
st.divider( )
# DataFrame:
if table.checkbox('DataFrame', value=False):
    st.subheader ('DATA')
    st.write     ('➡️ Showing temperature & precipitation reports from {} to {}'.format(df.index.min( ), df.index.max( )))
    st.write  (df)
    st.divider(  )
st.toast('Climate Terrorism!', icon='🔥')

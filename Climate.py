# Libraries:
import pandas              as pd
import matplotlib.pyplot   as plt
import seaborn             as sns
import streamlit           as st
st.set_page_config(page_title='CW&GC', page_icon='🔥', initial_sidebar_state='collapsed')
# DATA:
DATA        = 'datasets/CampinasSP.csv'
@st.cache_data
def load_data():
    rename  = {'casos-confirmados'   :'Cases'   ,
               'chuva'               :'Rain'    ,
               'temperatura-mininima':'MinTemp' ,
               'temperatura-media'   :'MeanTemp',
               'temperatura-maxima'  :'MaxTemp' }
    data    = pd.read_csv(DATA, index_col='data', parse_dates=True)
    #data.index  = data.index.date
    data    = data.rename(columns=rename        )
# Cleaning:
    data    = data.fillna({'Rain' :        0.00})
# Selecting:
    columns = ['MinTemp' ,
               'MeanTemp',
               'MaxTemp' ,
               'Rain'    ]    
    data    = data[list(columns)]
    return data
df          = load_data()
# SIDEBAR:
#st.sidebar.header(   'In Search of a Warming!')
st.sidebar.success(  'Climate Warming')
st.sidebar.info(     'Global  Change ')
st.sidebar.divider()
st.sidebar.subheader('Data   Analysis')
st.sidebar.markdown('''Source: [CIIAGRO](https://ciiagro.sp.gov.br/) – temperature & precipitation reports from {} to {}'''
                    .format(df.index.min(), df.index.max()))
# PlaceHolder for Table:
table          = st.sidebar.empty()
st.sidebar.divider()
with st.sidebar.container():
     C1,C2,C3  = st.columns(3)
     with C1:st.empty()
     with C2:st.markdown('''©2023™''')
     with C3:st.empty()
# MAIN:
st.title(   'In Search of a Warming!')
st.markdown('''
[![GitHub](https://img.shields.io/badge/GitHub-000000?logo=github&logoColor=white)](https://github.com/kauefs/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kauefs/)
[![Python](https://img.shields.io/badge/Python-3-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Apache_2.0-black.svg)](https://www.apache.org/licenses/LICENSE-2.0)
            ''')
st.write('23 November 2023')
st.markdown('''
After observing a climate series from 1998 to 2014 for the city of Campinas/SP, in Brazil, it is hard to see, from the data, any temperature anomaly.
Minimum and maximum temperatures have been stable, with close mean and median, resulting, as consequence, in a small standard deviation,
which is further confirmed by the small distance among the quantiles, thus, confirming no notable change in temperatures in the region during the analyzed period.

Therefore, one may wonder where is all that global warming claimed by everyone, everywhere, because it does not show in the data!
            ''')
# Chart:
st.subheader('Chart')
st.write(    '➡️ Showing temperature & precipitation reports from {} to {}'.format(df.index.min(), df.index.max()))
# Altogheter with Bar:
fig, ax = plt.subplots(figsize=(20, 10), tight_layout=True)
plt.rcParams['font.family']='sans-serif'
# Maximum Temperature:
df['MaxTemp'].plot(kind    ='line', ax=ax,
                linewidth  ='3.25',
                linestyle  ='dashed',
                color      ='maroon') #FF4500
# Mean    Temperature:
df['MeanTemp'].plot(kind       ='line', ax=ax,
                linewidth  ='3.25',
                linestyle  ='solid',
                color      ='#4CAF50')
# Minimum Temperature:
df['MinTemp'].plot(kind    ='line', ax=ax,
                linewidth  ='3.25',
                linestyle  ='dotted',
                color      ='#0065FF')
# Rain:
plt.bar(df.index, df['Rain']/25, color='DeepSkyBlue', width=.75)
ax.set_title('Temperature (ºC) & Precipitation (mm/25) for Campinas/SP (Brazil) from 1998 to 2014',
             fontsize=25, fontweight='semibold', loc='center')
ax.set_xlabel(None)
for spine in ['top', 'right', 'left', 'bottom']:ax.spines[spine].set_visible(False)
ax.tick_params(axis   =    'both',
               which  =    'both',
               left   =     False,
               bottom =     False)
plt.grid(axis='y', linestyle=':', linewidth=3.15, color='#DCDCDC', label='Rain')
plt.ylim(0, 35)
leg = plt.legend(['MaxTemp', 'MeanTemp', 'MinTemp', 'Rain'], loc='upper center', ncol=4, fontsize=20)
plt.gca().add_artist(leg)
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.show()
st.pyplot(fig)
st.divider()
# HeatMap:
A, B = st.columns(2)
with A: st.subheader('Heat Map')
with B:
    sns.set_style()
    corr    = df.corr()
    fig, ax = plt.subplots(tight_layout=True)
    ax = sns.heatmap(corr,
                fmt='.2f',
                cbar=True,
                annot=True,
                square=True,
                cmap='autumn_r',
                linewidths=1,
                linecolor='white')
    ax.xaxis.tick_top()
    plt.show()
    st.pyplot(fig)
st.divider()
# Columns:
L, R = st.columns(2)
with L:
    st.subheader('Summary Statistics')
    S = df.describe()
    S
with R:
    st.subheader('Correlation Matrix')
    corr
# Table:
if table.checkbox('Show Table Data', value=False):
    st.divider()
    st.subheader('DATA')
    st.write(    '➡️ Showing temperature & precipitation reports from {} to {}'.format(df.index.min(), df.index.max()))
    st.write(df)
st.toast('Climate Terrorism!', icon='🔥')

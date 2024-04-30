import pycountry
import dash
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


URL_DATASET = r'fossil-fuel-co2-emissions-by-nation.csv'
df1 = pd.read_csv(URL_DATASET)
df2 = pd.read_csv('epa-sea-level_csv.csv')
list_countries = df1['Country'].unique().tolist()
d_country_code = {} 
for country in list_countries:
    try:
        country_data = pycountry.countries.search_fuzzy(country)
        country_code = country_data[0].alpha_3
        d_country_code.update({country: country_code})
    except:
        print('could not add ISO 3 code for ->', country)
        d_country_code.update({country: ' '})

for k, v in d_country_code.items():
    df1.loc[(df1.Country == k), 'iso_alpha'] = v

fig = px.choropleth(data_frame = df1,
                    locations= "iso_alpha",
                    color= "Total",  
                    hover_name= "Country",
                    color_continuous_scale= ['cyan','blue','midnightblue','darkblue'], 
                    animation_frame= "Year")

sea_x=[]
sea_y=[]
sea_upper=[]
sea_lower=[]
for i in range (0,len(df2)):
    sea_x.append(df2['Year'][i])
    sea_y.append(df2['CSIRO Adjusted Sea Level'][i])
    sea_upper.append(df2['Upper Error Bound'][i])
    sea_lower.append(df2['Lower Error Bound'][i])

fig4 = go.Figure([
    go.Scatter(
        x=sea_x,
        y=sea_y,
        line=dict(color='rgb(0,100,80)'),
        mode='lines'
    ),
    go.Scatter(
        x=sea_x+sea_x[::-1], # x, then x reversed
        y=sea_upper+sea_lower[::-1], # upper, then lower reversed
        fill='toself',
        fillcolor='rgba(0,100,80,0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        hoverinfo="skip",
        showlegend=False
    )
])

y1=[]
t1=[]
y2=[]
t2=[]
for i in range (0,len(df1)):
  if df1['Country'][i] == 'INDIA':
    y1.append(df1['Year'][i])
    t1.append(df1['Total'][i])

for j in range (0,len(df1)):
  if df1['Country'][j] == 'UNITED STATES OF AMERICA':
    y2.append(df1['Year'][j])
    t2.append(df1['Total'][j])

fig1 = px.line( x = y1 ,
              y = t1,
              title = 'INDIA: Emmission of CO2 over years')

fig2 = px.line( x = y2 ,
              y = t2,
              title = 'USA: Emmission of CO2 over years')

from pandas import *
 
# reading CSV file
data = read_csv("numbers.csv")
 
# converting column data to list
year=data['Year'].tolist()
india = data['INDIA'].tolist()
uk = data['UNITED KINGDOM'].tolist()
canada= data['CANADA'].tolist()
germany = data['GERMANY'].tolist()
poland = data['POLAND'].tolist()
usa = data['UNITED STATES OF AMERICA'].tolist()
belgium = data['BELGIUM'].tolist()
france = data['FRANCE'].tolist()
austria = data['AUSTRIA'].tolist()
norway = data['NORWAY'].tolist()
hungary = data['HUNGARY'].tolist()
spain = data['SPAIN'].tolist()
sweden = data['SWEDEN'].tolist()
denmark = data['DENMARK'].tolist()
netherlands = data['NETHERLANDS'].tolist()
switzerland = data['SWITZERLAND'].tolist()
finland = data['FINLAND'].tolist()
italy = data['ITALY'].tolist()
turkey = data['TURKEY'].tolist()
greece = data['GREECE'].tolist()
japan = data['JAPAN'].tolist()
bulgaria = data['BULGARIA'].tolist()
indonesia = data['INDONESIA'].tolist()
malaysia = data['MALAYSIA'].tolist()
jordan = data['JORDAN'].tolist()
egypt = data['EGYPT'].tolist()
china = data['CHINA'].tolist()


fig5 = px.line( x = year ,
              y = [india,uk,canada,germany,poland,usa,belgium,france,austria,norway,hungary,spain,sweden,denmark,netherlands,switzerland,finland,italy,turkey,greece,japan,bulgaria,indonesia,malaysia,jordan,egypt,china],
              title = 'Emmission of CO2 over years of all countries from 1900 to 2014 (Un-Normalized)')

norm_india=[]
for i in range(0,len(india)):
    norm_india.append((india[i]-min(india))/(max(india)-min(india)))

norm_uk=[]
for i in range(0,len(uk)):
    norm_uk.append((uk[i]-min(uk))/(max(uk)-min(uk)))

norm_canada=[]
for i in range(0,len(canada)):
    norm_canada.append((canada[i]-min(canada))/(max(canada)-min(canada)))

norm_germany=[]
for i in range(0,len(germany)):
    norm_germany.append((germany[i]-min(germany))/(max(germany)-min(germany)))

norm_poland=[]
for i in range(0,len(poland)):
    norm_poland.append((poland[i]-min(poland))/(max(poland)-min(poland)))

norm_usa=[]
for i in range(0,len(india)):
    norm_usa.append((usa[i]-min(usa))/(max(usa)-min(usa)))

norm_belgium=[]
for i in range(0,len(india)):
    norm_belgium.append((belgium[i]-min(belgium))/(max(belgium)-min(belgium)))

norm_france=[]
for i in range(0,len(india)):
    norm_france.append((france[i]-min(france))/(max(france)-min(france)))

norm_austria=[]
for i in range(0,len(india)):
    norm_austria.append((austria[i]-min(austria))/(max(austria)-min(austria)))

norm_norway=[]
for i in range(0,len(india)):
    norm_norway.append((norway[i]-min(norway))/(max(norway)-min(norway)))

norm_hungary=[]
for i in range(0,len(india)):
    norm_hungary.append((hungary[i]-min(hungary))/(max(hungary)-min(hungary)))

norm_spain=[]
for i in range(0,len(india)):
    norm_spain.append((spain[i]-min(spain))/(max(spain)-min(spain)))

norm_sweden=[]
for i in range(0,len(india)):
    norm_sweden.append((sweden[i]-min(sweden))/(max(sweden)-min(sweden)))

norm_denmark=[]
for i in range(0,len(india)):
    norm_denmark.append((denmark[i]-min(denmark))/(max(denmark)-min(denmark)))

norm_netherlands=[]
for i in range(0,len(india)):
    norm_netherlands.append((netherlands[i]-min(netherlands))/(max(netherlands)-min(netherlands)))

norm_switzerland=[]
for i in range(0,len(india)):
    norm_switzerland.append((switzerland[i]-min(switzerland))/(max(switzerland)-min(switzerland)))

norm_finland=[]
for i in range(0,len(india)):
    norm_finland.append((finland[i]-min(finland))/(max(finland)-min(finland)))

norm_italy=[]
for i in range(0,len(india)):
    norm_italy.append((italy[i]-min(italy))/(max(italy)-min(italy)))

norm_turkey=[]
for i in range(0,len(india)):
    norm_turkey.append((turkey[i]-min(turkey))/(max(turkey)-min(turkey)))

norm_greece=[]
for i in range(0,len(india)):
    norm_greece.append((greece[i]-min(greece))/(max(greece)-min(greece)))

norm_japan=[]
for i in range(0,len(india)):
    norm_japan.append((japan[i]-min(japan))/(max(japan)-min(japan)))

norm_bulgaria=[]
for i in range(0,len(india)):
    norm_bulgaria.append((bulgaria[i]-min(bulgaria))/(max(bulgaria)-min(bulgaria)))

norm_indonesia=[]
for i in range(0,len(india)):
    norm_indonesia.append((indonesia[i]-min(indonesia))/(max(indonesia)-min(indonesia)))

norm_malaysia=[]
for i in range(0,len(india)):
    norm_malaysia.append((malaysia[i]-min(malaysia))/(max(malaysia)-min(malaysia)))

norm_jordan=[]
for i in range(0,len(india)):
    norm_jordan.append((jordan[i]-min(jordan))/(max(jordan)-min(jordan)))

norm_egypt=[]
for i in range(0,len(india)):
    norm_egypt.append((egypt[i]-min(egypt))/(max(egypt)-min(egypt)))

norm_china=[]
for i in range(0,len(india)):
    norm_china.append((china[i]-min(china))/(max(china)-min(china)))


fig6 = px.line( x = year ,
              y = [norm_india,norm_uk,norm_canada,norm_germany,norm_poland,norm_usa,norm_belgium,norm_france,norm_austria,norm_norway,norm_hungary,norm_spain,norm_sweden,norm_denmark,norm_switzerland,norm_finland,norm_italy,norm_turkey,norm_greece,norm_japan,norm_bulgaria,norm_indonesia,norm_malaysia,norm_egypt,norm_china],
              title = 'Emmission of CO2 over years of all countries from 1900 to 2014 (Normalized)')

#dtw from this point on
# the centers chosen are India, USA and China
d_uk=[]
d_canada=[]
d_germany=[]
d_poland=[]
d_belgium=[]
d_france=[]
d_austria=[]
d_norway=[]
d_hungary=[]
d_spain=[]
d_sweden=[]
d_denmark=[]
d_switzerland=[]
d_finland=[]
d_italy=[]
d_turkey=[]
d_greece=[]
d_japan=[]
d_bulgaria=[]
d_indonesia=[]
d_malaysia=[]
d_egypt=[]
d_china=[]

import math
def DTWDistance(s1, s2, array):
    DTW={}
    
    for i in range(len(s1)):
        DTW[(i, -1)] = float('inf')
    for i in range(len(s2)):
        DTW[(-1, i)] = float('inf')
    DTW[(-1, -1)] = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            dist= (s1[i]-s2[j])**2
            DTW[(i, j)] = dist + min(DTW[(i-1, j)],DTW[(i, j-1)], DTW[(i-1, j-1)])
		
    array.append(math.sqrt(DTW[len(s1)-1, len(s2)-1]))

DTWDistance(norm_uk,norm_india,d_uk)
DTWDistance(norm_uk,norm_usa,d_uk)
DTWDistance(norm_uk,norm_china,d_uk)

DTWDistance(norm_canada,norm_india,d_canada)
DTWDistance(norm_canada,norm_usa,d_canada)
DTWDistance(norm_canada,norm_china,d_canada)

DTWDistance(norm_germany,norm_india,d_germany)
DTWDistance(norm_germany,norm_usa,d_germany)
DTWDistance(norm_germany,norm_china,d_germany)

DTWDistance(norm_poland,norm_india,d_poland)
DTWDistance(norm_poland,norm_usa,d_poland)
DTWDistance(norm_poland,norm_china,d_poland)

DTWDistance(norm_belgium,norm_india,d_belgium)
DTWDistance(norm_belgium,norm_usa,d_belgium)
DTWDistance(norm_belgium,norm_china,d_belgium)

DTWDistance(norm_france,norm_india,d_france)
DTWDistance(norm_france,norm_usa,d_france)
DTWDistance(norm_france,norm_china,d_france)

DTWDistance(norm_austria,norm_india,d_austria)
DTWDistance(norm_austria,norm_usa,d_austria)
DTWDistance(norm_austria,norm_china,d_austria)

DTWDistance(norm_norway,norm_india,d_norway)
DTWDistance(norm_norway,norm_usa,d_norway)
DTWDistance(norm_norway,norm_china,d_norway)

DTWDistance(norm_hungary,norm_india,d_hungary)
DTWDistance(norm_hungary,norm_usa,d_hungary)
DTWDistance(norm_hungary,norm_china,d_hungary)

DTWDistance(norm_spain,norm_india,d_spain)
DTWDistance(norm_spain,norm_usa,d_spain)
DTWDistance(norm_spain,norm_china,d_spain)

DTWDistance(norm_sweden,norm_india,d_sweden)
DTWDistance(norm_sweden,norm_usa,d_sweden)
DTWDistance(norm_sweden,norm_china,d_sweden)

DTWDistance(norm_denmark,norm_india,d_denmark)
DTWDistance(norm_denmark,norm_usa,d_denmark)
DTWDistance(norm_denmark,norm_china,d_denmark)

DTWDistance(norm_switzerland,norm_india,d_switzerland)
DTWDistance(norm_switzerland,norm_usa,d_switzerland)
DTWDistance(norm_switzerland,norm_china,d_switzerland)

DTWDistance(norm_finland,norm_india,d_finland)
DTWDistance(norm_finland,norm_usa,d_finland)
DTWDistance(norm_finland,norm_china,d_finland)

DTWDistance(norm_italy,norm_india,d_italy)
DTWDistance(norm_italy,norm_usa,d_italy)
DTWDistance(norm_italy,norm_china,d_italy)

DTWDistance(norm_turkey,norm_india,d_turkey)
DTWDistance(norm_turkey,norm_usa,d_turkey)
DTWDistance(norm_turkey,norm_china,d_turkey)

DTWDistance(norm_greece,norm_india,d_greece)
DTWDistance(norm_greece,norm_usa,d_greece)
DTWDistance(norm_greece,norm_china,d_greece)

DTWDistance(norm_japan,norm_india,d_japan)
DTWDistance(norm_japan,norm_usa,d_japan)
DTWDistance(norm_japan,norm_china,d_japan)

DTWDistance(norm_bulgaria,norm_india,d_bulgaria)
DTWDistance(norm_bulgaria,norm_usa,d_bulgaria)
DTWDistance(norm_bulgaria,norm_china,d_bulgaria)

DTWDistance(norm_indonesia,norm_india,d_indonesia)
DTWDistance(norm_indonesia,norm_usa,d_indonesia)
DTWDistance(norm_indonesia,norm_china,d_indonesia)

DTWDistance(norm_malaysia,norm_india,d_malaysia)
DTWDistance(norm_malaysia,norm_usa,d_malaysia)
DTWDistance(norm_malaysia,norm_china,d_malaysia)

DTWDistance(norm_egypt,norm_india,d_egypt)
DTWDistance(norm_egypt,norm_usa,d_egypt)
DTWDistance(norm_egypt,norm_china,d_egypt)

# https://nbviewer.org/github/alexminnaar/time-series-classification-and-clustering/blob/master/Time%20Series%20Classification%20and%20Clustering.ipynb

cluster_india=[]
cluster_usa=[]
cluster_china=[]

if max(d_uk)==d_uk[0]:
    cluster_india.append(norm_uk)
elif max(d_uk)==d_uk[1]:
    cluster_usa.append(norm_uk)
elif max(d_uk)==d_uk[2]:
    cluster_china.append(norm_uk)

if max(d_canada)==d_canada[0]:
    cluster_india.append(norm_canada)
elif max(d_canada)==d_canada[1]:
    cluster_usa.append(norm_canada)
elif max(d_canada)==d_canada[2]:
    cluster_china.append(norm_canada)

if max(d_germany)==d_germany[0]:
    cluster_india.append(norm_germany)
elif max(d_germany)==d_germany[1]:
    cluster_usa.append(norm_germany)
elif max(d_germany)==d_germany[2]:
    cluster_china.append(norm_germany)

if max(d_belgium)==d_belgium[0]:
    cluster_india.append(norm_belgium)
elif max(d_belgium)==d_belgium[1]:
    cluster_usa.append(norm_belgium)
elif max(d_belgium)==d_belgium[2]:
    cluster_china.append(norm_belgium)

if max(d_poland)==d_poland[0]:
    cluster_india.append(norm_poland)
elif max(d_poland)==d_poland[1]:
    cluster_usa.append(norm_poland)
elif max(d_poland)==d_poland[2]:
    cluster_china.append(norm_poland)

if max(d_france)==d_france[0]:
    cluster_india.append(norm_france)
elif max(d_france)==d_france[1]:
    cluster_usa.append(norm_france)
elif max(d_france)==d_france[2]:
    cluster_china.append(norm_france)

if max(d_austria)==d_austria[0]:
    cluster_india.append(norm_austria)
elif max(d_austria)==d_austria[1]:
    cluster_usa.append(norm_austria)
elif max(d_austria)==d_austria[2]:
    cluster_china.append(norm_austria)

if max(d_norway)==d_norway[0]:
    cluster_india.append(norm_norway)
elif max(d_norway)==d_norway[1]:
    cluster_usa.append(norm_norway)
elif max(d_norway)==d_norway[2]:
    cluster_china.append(norm_norway)

if max(d_hungary)==d_hungary[0]:
    cluster_india.append(norm_hungary)
elif max(d_hungary)==d_hungary[1]:
    cluster_usa.append(norm_hungary)
elif max(d_hungary)==d_hungary[2]:
    cluster_china.append(norm_hungary)

if max(d_spain)==d_spain[0]:
    cluster_india.append(norm_spain)
elif max(d_spain)==d_spain[1]:
    cluster_usa.append(norm_spain)
elif max(d_spain)==d_spain[2]:
    cluster_china.append(norm_spain)

if max(d_sweden)==d_sweden[0]:
    cluster_india.append(norm_sweden)
elif max(d_sweden)==d_sweden[1]:
    cluster_usa.append(norm_sweden)
elif max(d_sweden)==d_sweden[2]:
    cluster_china.append(norm_sweden)

if max(d_denmark)==d_denmark[0]:
    cluster_india.append(norm_denmark)
elif max(d_denmark)==d_denmark[1]:
    cluster_usa.append(norm_denmark)
elif max(d_denmark)==d_denmark[2]:
    cluster_china.append(norm_denmark)

if max(d_switzerland)==d_switzerland[0]:
    cluster_india.append(norm_switzerland)
elif max(d_switzerland)==d_switzerland[1]:
    cluster_usa.append(norm_switzerland)
elif max(d_switzerland)==d_switzerland[2]:
    cluster_china.append(norm_switzerland)

if max(d_finland)==d_finland[0]:
    cluster_india.append(norm_finland)
elif max(d_finland)==d_finland[1]:
    cluster_usa.append(norm_finland)
elif max(d_finland)==d_finland[2]:
    cluster_china.append(norm_finland)

if max(d_italy)==d_italy[0]:
    cluster_india.append(norm_italy)
elif max(d_italy)==d_italy[1]:
    cluster_usa.append(norm_italy)
elif max(d_italy)==d_italy[2]:
    cluster_china.append(norm_italy)

if max(d_turkey)==d_turkey[0]:
    cluster_india.append(norm_turkey)
elif max(d_turkey)==d_turkey[1]:
    cluster_usa.append(norm_turkey)
elif max(d_turkey)==d_turkey[2]:
    cluster_china.append(norm_turkey)

if max(d_greece)==d_greece[0]:
    cluster_india.append(norm_greece)
elif max(d_greece)==d_greece[1]:
    cluster_usa.append(norm_greece)
elif max(d_greece)==d_greece[2]:
    cluster_china.append(norm_greece)

if max(d_japan)==d_japan[0]:
    cluster_india.append(norm_japan)
elif max(d_japan)==d_japan[1]:
    cluster_usa.append(norm_japan)
elif max(d_japan)==d_japan[2]:
    cluster_china.append(norm_japan)

if max(d_bulgaria)==d_bulgaria[0]:
    cluster_india.append(norm_bulgaria)
elif max(d_bulgaria)==d_bulgaria[1]:
    cluster_usa.append(norm_bulgaria)
elif max(d_bulgaria)==d_bulgaria[2]:
    cluster_china.append(norm_bulgaria)

if max(d_indonesia)==d_indonesia[0]:
    cluster_india.append(norm_indonesia)
elif max(d_indonesia)==d_indonesia[1]:
    cluster_usa.append(norm_indonesia)
elif max(d_indonesia)==d_indonesia[2]:
    cluster_china.append(norm_indonesia)

if max(d_malaysia)==d_malaysia[0]:
    cluster_india.append(norm_malaysia)
elif max(d_malaysia)==d_malaysia[1]:
    cluster_usa.append(norm_malaysia)
elif max(d_malaysia)==d_malaysia[2]:
    cluster_china.append(norm_malaysia)

if max(d_egypt)==d_egypt[0]:
    cluster_india.append(norm_uk)
elif max(d_egypt)==d_egypt[1]:
    cluster_usa.append(norm_uk)
elif max(d_egypt)==d_egypt[2]:
    cluster_china.append(norm_uk)


fig7 = px.line( x = year ,
              y = cluster_india,
              title = 'Clusters of India')

fig8 = px.line( x = year ,
              y = cluster_usa,
              title = 'Clusters of USA')

fig9 = px.line( x = year ,
              y = cluster_china,
              title = 'Clusters of China')




app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    # All elements from the top of the page
    html.Div([
        html.H1(children='Carbon Dioxide Emmissions',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

        html.Div(children='''
            This graph shows us how the trend of emmission of CO2 from various countries changed over the 
            past few centuries. We can easily see how various nations contributed to the abundance of CO2
            in the atmosphere in an year wise manner using the slider.
        ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(
            id='graph1',
            figure=fig
        ),  
    ]),
    # New Div for all elements in the new 'row' of the page
    html.Div([
        html.Div([
            html.H1(children='CO2 Emmission of India Over Years',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

            html.Div(children='''
                Using this interactive visualization, we track the amount of Carbon Dioxide 
                India has produced over the years. The X axis shows the years while the Y axis
                shows the amount of CO2 discharged.
            ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

            dcc.Graph(
                id='graph2',
                figure=fig1
            ),  
        ], className='six columns'),

        html.Div([
            html.H1(children='CO2 Emmission of USA Over Years',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

            html.Div(children='''
                Using this interactive visualization, we track the amount of Carbon Dioxide 
                USA has produced over the years. The X axis shows the years while the Y axis
                shows the amount of CO2 discharged.
            ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

            dcc.Graph(
                id='graph3',
                figure=fig2
            ),  
        ], className='six columns'),

    ], className='row'),
    html.Div([
        html.H1(children='Changing Sea Levels Over Years',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

        html.Div(children='''
            This interactive graph shows us the averga increase in the sea level which is a direct impact of Global
            Warming or indirectly increasing levels of CO2 and other greenhouse gases. 
            This graph also gives the confidence intervals with the upper and lower bounds 
            for each data point.
        ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

        dcc.Graph(
            id='graph4',
            figure=fig4
        ),  
    ]),

    html.Div([
        html.H1(children='CO2 Emmission of different countries Over Years (Un-Normalized)',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

            html.Div(children='''
               Here we analyse the CO2 emmission of all countries in a single graph. This is the 
               un-normalized version.
            ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

            dcc.Graph(
                id='graph5',
                figure=fig5
        ),  
    ]),

    html.Div([
        html.H1(children='CO2 Emmission of different countries Over Years (Normalized)',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

            html.Div(children='''
               Here we analyse the CO2 emmission of all countries in a single graph. This is the 
               normalized version.
            ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

            dcc.Graph(
                id='graph6',
                figure=fig6
        ),  
    ]),

    html.Div([
        html.H1(children='Clusters of USA',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

            html.Div(children='''
               Here are all the countries which are the part of cluster of USA in the normalized form.
            ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

            dcc.Graph(
                id='graph8',
                figure=fig8
        ),  
    ]),

    html.Div([
        html.H1(children='Clusters of China',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

            html.Div(children='''
               Here are all the countries which are the part of cluster of China in the normalized form.
            ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

            dcc.Graph(
                id='graph9',
                figure=fig9
        ),  
    ]),

    html.Div([
        html.H1(children='Clusters of India',style={
            'textAlign': 'center',
            'color': colors['text'], 'padding': 30
        }),

            html.Div(children='''
               Here are all the countries which are the part of cluster of India in the normalized form.
            ''',style={
            'textAlign': 'center',
            'color': colors['text']
        }),

            dcc.Graph(
                id='graph7',
                figure=fig7
        ),  
    ]),
])

if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)


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
])

if __name__ == '__main__':
    app.run_server(debug=True,use_reloader=False)


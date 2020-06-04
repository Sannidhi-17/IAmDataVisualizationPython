#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing all the libraries

import numpy as np
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import dash_auth

#read csv file
df = pd.read_csv('covid_19_data.csv')
df.head()


# # Active cases

# In[2]:


# find the active cases from the dataset and save in new column Active

df['Active'] = df['Confirmed'] - df['Deaths'] - df['Recovered']
df


# In[3]:


# Select countries and apply in new dataframe

ar1 = ['Mainland China']
df1 = df[df.Country.isin(ar1)]
ar2 = ['South Korea']
df2 = df[df.Country.isin(ar2)]
ar3 = ['France']
df3 = df[df.Country.isin(ar3)]
ar4 = ['Italy']
df4 = df[df.Country.isin(ar4)]
ar5 = ['US']
df5 = df[df.Country.isin(ar5)]
ar6 = ['Spain']
df6 = df[df.Country.isin(ar6)]
ar7 = ['Germany']
df7 = df[df.Country.isin(ar7)]


# In[4]:


#sum of the all active cases as per date
df1 = df1.groupby('ObservationDate')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
df2 = df2.groupby('ObservationDate')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
df3 = df3.groupby('ObservationDate')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
df4 = df4.groupby('ObservationDate')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
df5 = df5.groupby('ObservationDate')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
df6 = df6.groupby('ObservationDate')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()
df7 = df7.groupby('ObservationDate')['Confirmed', 'Deaths', 'Recovered', 'Active'].sum().reset_index()


# In[5]:


#select specific dates for plotting 

array1 = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020']
df1 = df1[df1.ObservationDate.isin(array1)]
df2 = df2[df2.ObservationDate.isin(array1)]
df3 = df3[df3.ObservationDate.isin(array1)]
df4 = df4[df4.ObservationDate.isin(array1)]
df5 = df5[df5.ObservationDate.isin(array1)]
df6 = df6[df6.ObservationDate.isin(array1)]
df7 = df7[df7.ObservationDate.isin(array1)]
df1


# In[6]:


#sort the values as per confirmed

df1 = df1.sort_values(by='Confirmed')
df2 = df2.sort_values(by='Confirmed')
df3 = df3.sort_values(by='Confirmed')
df4 = df4.sort_values(by='Confirmed')
df5 = df5.sort_values(by='Confirmed')
df6 = df6.sort_values(by='Confirmed')
df7 = df7.sort_values(by='Confirmed')
df1


# In[7]:


import plotly.graph_objs as go

figActive = go.Figure()

figActive.add_trace(go.Scatter(x=df1['ObservationDate'], y=df1['Active'], name = 'China',
                     line = {'width': 2, 'color': 'black'}))
figActive.add_trace(go.Scatter(x=df3['ObservationDate'], y=df3['Active'], name = 'France',
                    line = {'width': 2, 'color': 'Blue'}))
figActive.add_trace(go.Scatter(x=df4['ObservationDate'], y=df4['Active'], name = 'Italy',
                    line = {'width': 2, 'color': 'red'}))
figActive.add_trace(go.Scatter(x=df5['ObservationDate'], y=df5['Active'], name = 'USA',
                   line = {'width': 2, 'color': 'green'}))
figActive.add_trace(go.Scatter(x=df6['ObservationDate'], y=df6['Active'], name = 'Spain',
                    line = {'width': 2, 'color': 'orange'}))
figActive.add_trace(go.Scatter(x=df7['ObservationDate'], y=df7['Active'], name = 'Germany',
                    line = {'width': 2, 'color': 'yellow'}))



figActive.update_layout(
    #yaxis=dict(range=[0,12000]),
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    ),
    autosize=False,
    width=1500,
    height=700,
    xaxis_title="<b> Dates </b> ",
    yaxis_title="<b> Number of active cases in thousand </b>",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#000000"
    )
)

figActive.add_annotation(
            x=6.05,
            y=1000,
            ax=0,
            ay=-360,
            text="<br> USA <br>on 20 March </b>")
figActive.add_annotation(
            x=5.60,
            y=5500,
            ax=0,
            ay=-200,
            text="<br> France <br>16th March </b>")
figActive.add_annotation(
            x=5.00,
            y=1000,
            ax=0,
            ay=-290,
            text="<br> Italy <br>10th March </b>")
figActive.add_annotation(
            x=7.15,
            y=70000,
            ax=0,
            ay=-250,
            text="<br> Germany <br>2nd April </b>")
figActive.add_annotation(
            x=0.10,
            y=1000,
            ax=0,
            ay=-250,
            text="<br> China <br>23rd January</b>")

figActive.add_annotation(
            x=5.40,
            y=5500,
            ax=0,
            ay=-450,
            text="<br> Spain <br>14th March</b>"),

figActive.update_annotations(dict(
            xref="x",
            yref="y",
            showarrow=True,
            font=dict(
            family="Courier New, monospace",
            size=16,
            color="#000000"
            ),
        align="center",
        arrowhead=2,
        arrowsize=1,
        arrowwidth=2,
        arrowcolor="#000011",
        bordercolor="#c7c7c7",
        borderwidth=2,
        borderpad=4,
        bgcolor="#ffffff",
        opacity=0.8
))



# # Confirmed Cases

# In[8]:


# minus below row from above row for the date wise cases
df1['new'] = df1.Confirmed.diff()
df2['new'] = df2.Confirmed.diff()
df3['new'] = df3.Confirmed.diff()
df4['new'] = df4.Confirmed.diff()
df5['new'] = df5.Confirmed.diff()
df6['new'] = df6.Confirmed.diff()
df7['new'] = df7.Confirmed.diff()
df1


# In[9]:


# convert into positive number
df1['new'] = df1['new'].abs()
df2['new'] = df2['new'].abs()
df3['new'] = df3['new'].abs()
df4['new'] = df4['new'].abs()
df5['new'] = df5['new'].abs()
df6['new'] = df6['new'].abs()
df7['new'] = df7['new'].abs()
df1


# In[10]:


# now filling epmty space with cases
df1["new"].fillna("1", inplace = True)
df2["new"].fillna("1", inplace = True)
df3["new"].fillna("5", inplace = True)
df4["new"].fillna("3", inplace = True)
df5["new"].fillna("1", inplace = True)
df6["new"].fillna("2", inplace = True)
df7["new"].fillna("4", inplace = True)
df1


# In[11]:


import plotly.graph_objects as go # or plotly.express as px
figConfirmed = go.Figure()
figConfirmed.add_trace(go.Scatter(x=df1['ObservationDate'], y=df1['new'], name = 'China',
                     line = {'width': 2, 'color': 'black'}))
figConfirmed.add_trace(go.Scatter(x=df3['ObservationDate'], y=df3['new'], name = 'France',
                    line = {'width': 2, 'color': 'Blue'}))
figConfirmed.add_trace(go.Scatter(x=df4['ObservationDate'], y=df4['new'], name = 'Italy',
                    line = {'width': 2, 'color': 'red'}))
figConfirmed.add_trace(go.Scatter(x=df6['ObservationDate'], y=df6['new'], name = 'Spain',
                    line = {'width': 2, 'color': 'orange'}))
figConfirmed.add_trace(go.Scatter(x=df7['ObservationDate'], y=df7['new'], name = 'Germany',
                    line = {'width': 2, 'color': 'yellow'}))

figConfirmed.update_layout(
    #yaxis=dict(range=[0,12000
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    ),
    autosize=False,
    width=1500,
    height=700,
    xaxis_title="<b> Dates </b> ",
    yaxis_title="<b> Number of Confirmed Cases in Thousand </b>",
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="#000000"
    )
)

figConfirmed.add_annotation(
            x=0.10,
            y=1000,
            ax=0,
            ay=-200,
            text="<br> China <br>23rd January")
figConfirmed.add_annotation(
            x=5.65,
            y=6500,
            ax=0,
            ay=-200,
            text="<br> France <br>16th March")
figConfirmed.add_annotation(
            x=7.25,
            y=49000,
            ax=0,
            ay=-200,
            text="<br> Germany <br>2nd April")
figConfirmed.add_annotation(
            x=5.00,
            y=7300,
            ax=0,
            ay=-290,
            text="<br> Italy <br>10th March")
figConfirmed.add_annotation(
            x=5.45,
            y=8200,
            ax=0,
            ay=-380,
            text="<br> Spain <br>14th March"),
figConfirmed.update_annotations(dict(
            xref="x",
            yref="y",
            arrowcolor = "#000011",
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            bordercolor="#c7c7c7",
            borderwidth=2,
            borderpad=4,
            bgcolor="#ffffff",
            opacity=0.8
))


    
# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     html.H1(children='Confirmed cases per country '),
#     html.Div(children='''Below graph shows decrease in the new covid-19 cases after social distancing measures are inacted.'''),
#     dcc.Graph(id = 'Confirmed Graph', figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter


# # Death cases

# In[12]:


#deaths pr day and storing in onther column
df1['new_deaths'] = df1.Deaths.diff()
df2['new_deaths'] = df2.Deaths.diff()
df3['new_deaths'] = df3.Deaths.diff()
df4['new_deaths'] = df4.Deaths.diff()
df5['new_deaths'] = df5.Deaths.diff()
df6['new_deaths'] = df6.Deaths.diff()
df7['new_deaths'] = df7.Deaths.diff()
df3


# In[13]:


# filling empty values as per dataset
df1["new_deaths"].fillna("17", inplace = True)
df2["new_deaths"].fillna("0", inplace = True)
df3["new_deaths"].fillna("0", inplace = True)
df4["new_deaths"].fillna("0", inplace = True)
df5["new_deaths"].fillna("0", inplace = True)
df6["new_deaths"].fillna("0", inplace = True)
df7["new_deaths"].fillna("0", inplace = True)
df3


# In[14]:


import plotly.graph_objects as go # or plotly.express as px
from plotly.subplots import make_subplots

figDeaths = go.Figure() # or any Plotly Express function e.g. px.bar(...)
figDeaths = make_subplots(rows=3, cols=2, shared_yaxes=False, x_title='Dates', 
                    y_title='Number of death in thousand ',
                    subplot_titles=("China Announced Lockdown On 23rd January ","USA Announced Lockdown On 20th March", "France 16th Announced Lockdown On March",
                                    "Italy Announced Lockdown On 10th March",
                                    "Spain Announced Lockdown On 14th March",
                                    "Germany Announced Lockdown On 2nd April"))
figDeaths.add_trace(go.Scatter(x=df1['ObservationDate'], y=df1['new_deaths'], name = 'China',
                     line = {'width': 2, 'color': 'black'}),row=1, col=1)
figDeaths.add_trace(go.Scatter(x=df5['ObservationDate'], y=df5['new_deaths'], name = 'USA',
                    line = {'width': 2, 'color': 'green'}),row=1, col=2)
figDeaths.add_trace(go.Scatter(x=df3['ObservationDate'], y=df3['new_deaths'], name = 'France',
                    line = {'width': 2, 'color': 'Blue'}),row=2, col=1)
figDeaths.add_trace(go.Scatter(x=df4['ObservationDate'], y=df4['new_deaths'], name = 'Italy',
                    line = {'width': 2, 'color': 'red'}),row=2, col=2)
figDeaths.add_trace(go.Scatter(x=df6['ObservationDate'], y=df6['new_deaths'], name = 'Spain',
                    line = {'width': 2, 'color': 'orange'}),row=3, col=1)
figDeaths.add_trace(go.Scatter(x=df7['ObservationDate'], y=df7['new_deaths'], name = 'Germany',
                    line = {'width': 2, 'color': 'green'}),row=3, col=2)

figDeaths.update_layout(height=1000, width=1500)
#fig.update_xaxes(tickangle=340)
figDeaths.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    ),
    xaxis2 = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    ),
    xaxis3 = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    ),
    xaxis4 = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    ),
    xaxis5 = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    ),
    xaxis6 = dict(
        tickmode = 'array',
        tickvals = ['22-01-2020', '30-01-2020', '10-02-2020', '20-02-2020', '29-02-2020', '10-03-2020',
         '20-03-2020', '30-03-2020','10-04-2020', '20-04-2020', '30-04-2020'],
        ticktext = ['22 Jan','30 Jan','10 Feb','20 Feb','29 Feb','10 Mar','20 Mar','30 Mar','30 Mar', '10 Apr','20 Apr','30 Apr'],
        tickangle=360
    )
)

# import dash
# import dash_core_components as dcc
# import dash_html_components as html

# app = dash.Dash()
# app.layout = html.Div([
#     html.H1(children='''Multiple Subplots with Shared Y-Axes'''),
#     html.H3(children='''Below subplots shows the decline in death rate after lockdown was initiated in each country this was due to 
#     the decrease in new cases which resulted in Medical Facilities not being overburdened.'''),
    
#     dcc.Graph(id = 'Death Graph', figure=fig)
# ])

# app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter


# In[15]:


import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    html.H1(children='Active cases in worst hit countries '),
    html.Div(children='''Above graph displays the flattening of curve after social
    distancing measure are applied by different countries. The total no. Of active cases flatten and then decrease gradually.'''),
    
    dcc.Graph(id = 'Active Graph', figure=figActive),
    
    html.H1(children='Confirmed cases per country '),
    html.Div(children='''Below graph shows decrease in the new covid-19 cases after social distancing measures are inacted.'''),
    dcc.Graph(id = 'Confirmed Graph', figure=figConfirmed),
    
    html.H1(children='''Multiple Subplots with Shared Y-Axes'''),
    html.H3(children='''Below subplots shows the decline in death rate after lockdown was initiated in each country this was due to 
    the decrease in new cases which resulted in Medical Facilities not being overburdened.'''),
    
    dcc.Graph(id = 'Death Graph', figure=figDeaths)
])

app.run_server(debug=True, use_reloader=False)  # Turn off reloader if inside Jupyter


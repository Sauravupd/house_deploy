# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
from dash import no_update


# Create a dash application
app = dash.Dash(__name__)


app.config.suppress_callback_exceptions = True


df =  pd.read_csv(r'C:\Users\upadh\Desktop\house\house_clean7.csv')







# City vs Price
bar_data = df.groupby(["City"])['Price'].sum().reset_index()
 # Bedroom Vs Price
line_data = df.groupby(['Bedroom','City'])['Price'].mean().reset_index()
 # Face Vs Price
div_data = df.groupby(['Face'])['Price'].mean().to_frame().reset_index()
 #City vs Number of properties listed
bar_data2 = df["City"].value_counts().to_frame().reset_index()
bar_data2.columns=['City','Price']
 # Amenities vs Price
line_data2 = df.groupby(['Number of Amenities','City'])['Price'].mean().reset_index()

bar_fig = px.bar(bar_data, x='City', y='Price', title='Total price')
            
            
line_fig = px.line(line_data, x='Bedroom', y='Price',color='City' ,title='Total price')
            
        
bar3_fig = px.bar(bar_data2, x='City', y='Price', title='number of property listed in each city')
            
            
bar2_fig = px.bar(div_data, x='Face', y='Price' ,title='Total price')
            
            
            
line_fig2 = px.line(line_data2, x='Number of Amenities', y='Price' ,color='City',title='Total price')
    



# Application layout
app.layout = html.Div(children=[ html.H1('Nepal Property Listing Visualization',style={'textAlign':'left','color':'#503D36','font-size':24}),
                                
                                    
                                
                                
                                html.Div([dcc.Graph(figure= bar3_fig)], id='plot1'),
    
                                html.Div([
                                        html.Div([dcc.Graph(figure=bar_fig)], id='plot2'),
                                        html.Div([ line_fig], id='plot3')
                                ], style={'display': 'flex'}),
                                
                                
                                html.Div([
                                    html.Div([dcc.Graph(figure=bar2_fig)]),
                                    html.Div([dcc.Graph(figure=line_fig2)])
                                ])

])
                               
                            

            
            

            
            
            
       


# Run the app
if __name__ == '__main__':
    app.run_server()
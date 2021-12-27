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


df =  pd.read_csv('https://github.com/Sauravupd/Nepal-housing-data-cleaning-and-visualizaion/blob/main/house_clean7.csv?raw=True')







# City vs Price
bar_data = df.groupby(["City"])['Price'].sum().reset_index()
 # Area Vs Price
line_data = df.groupby(['City','New_Area'])['Price'].mean().reset_index()
 # Face Vs Price
div_data = df.groupby(['Face'])['Price'].mean().to_frame().reset_index()
 #City vs Number of properties listed
bar_data2 = df["City"].value_counts().to_frame().reset_index()
bar_data2.columns=['City','Number of properties']
 # Amenities vs Price
line_data2 = df.groupby(['Number of Amenities','City'])['Price'].mean().reset_index()


bar_fig = px.bar(bar_data, x='City', y='Price', title='Total price',color ='City')
            
            
line_fig = px.scatter(df, x='New_Area', y='Price',color='City' ,range_x=[0,300],title='New Area Vs Price')
            
        
bar3_fig = px.bar(bar_data2, x='City', y='Number of properties', title='number of property listed in each city',color = "City")

#road width vs price
road_fig = px.scatter(df,x='Road_Width',y='Price',range_x=[0,80],title = 'Road Width VS Price',color="City")
            
            
bar2_fig = px.bar(div_data, x='Face', y='Price' ,title='Average price With Respect to Face',color="Face")
            
            
            
line_fig2 = px.line(line_data2, x='Number of Amenities', y='Price' ,color='City',title='Average Price With Respect to Number of Amenities')
    



# Application layout
app.layout = html.Div(children=[ html.H1('Nepal Property Listing Visualization',style={'textAlign':'center','color':'#503D36','font-size':24}),
                                
                                    
                                
                                
                                html.Div([dcc.Graph(figure= bar3_fig)], id='plot1'),
    
                                html.Div([
                                        html.Div([dcc.Graph(figure=bar_fig)], id='plot2'),
                                        html.Div([ dcc.Graph(figure=line_fig)], id='plot3')
                                ], style={'display': 'flex'}),
                                
                                
                                html.Div([
                                    html.Div([dcc.Graph(figure=bar2_fig)]),
                                    html.Div([dcc.Graph(figure=line_fig2)])
                                ]),

                                html.Div([dcc.Graph(figure=road_fig)])

])
                               
                            

            
            

            
            
            
       


# Run the app
if __name__ == '__main__':
    app.run_server()
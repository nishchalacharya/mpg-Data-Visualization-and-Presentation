import plotly.express as px
import dash
from dash import html, dcc
import pandas as pd

# Load dataset
df = pd.read_csv('mpg.csv')

# Columns
numerical_features = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']
categorical_cols = ['cylinders', 'origin', 'model_year']

# Univariate Analysis
univariate_figs = [px.histogram(df, x=feature, nbins=20, title=f'{feature} Histogram', marginal="box", opacity=0.75)
                   for feature in numerical_features]

box_figs = [px.box(df, x=feature, title=f'{feature} Boxplot') for feature in numerical_features]

# Categorical Analysis
categorical_figs = [px.histogram(df, x=col, title=f'{col} Histogram', color=col) for col in categorical_cols]
fig_pie = px.pie(df, names='cylinders', title='Cylinders Pie Chart')

# Bivariate Analysis
bivariate_figs = [
    px.scatter(df, x='horsepower', y='mpg', title='Horsepower vs MPG'),
    px.scatter(df, x='displacement', y='mpg', title='Displacement vs MPG'),
    px.scatter(df, x='weight', y='mpg', title='Weight vs MPG'),
    px.bar(df, x='cylinders', y='mpg', title='MPG vs Cylinders'),
    px.bar(df, x='origin', y='mpg', title='MPG vs Origin'),
    px.bar(df, x='model_year', y='mpg', title='MPG vs Model Year'),
]

# Heatmaps
corr = df.corr(numeric_only=True)
fig_heatmap = px.imshow(corr, text_auto=True, color_continuous_scale='RdBu_r', origin='upper',
                        title='Correlation Heatmap')

crosstab = pd.crosstab(df['cylinders'], df['origin'])
fig_heatmap2 = px.imshow(crosstab, text_auto=True, color_continuous_scale='Blues',
                         labels=dict(x='Origin', y='Cylinders', color='Count'),
                         title='Cylinders vs Origin Crosstab Heatmap')

# Multivariate Analysis
multivariate_figs = [
    px.scatter(df, x='weight', y='mpg', color='origin',
               title='MPG vs Weight by Origin'),
    px.scatter(df, x='horsepower', y='mpg', color='cylinders', size='weight',
               title='MPG vs Horsepower with Cylinders and Weight',
               size_max=15)
]

# Bootstrap Dash app
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Card component function
def create_card(title, figure):
    return html.Div(className='col-md-6 mb-4', children=[
        html.Div(className='card shadow-sm', children=[
            html.Div(className='card-body', children=[
                html.H5(title, className='card-title text-center'),
                dcc.Graph(figure=figure)
            ])
        ])
    ])

# App layout
app.layout = html.Div(className='container-fluid', children=[

    html.H1("MPG Dataset Dashboard", className='text-center my-4'),

    html.H2("Univariate Analysis", className='mt-4'),
    html.Div(className='row', children=[
        create_card(fig.layout.title.text, fig) for fig in univariate_figs
    ]),
    html.Div(className='row', children=[
        create_card(fig.layout.title.text, fig) for fig in box_figs
    ]),

    html.H2("Categorical Analysis", className='mt-4'),
    html.Div(className='row', children=[
        create_card(fig.layout.title.text, fig) for fig in categorical_figs
    ]),
    html.Div(className='row', children=[
        create_card("Cylinders Pie Chart", fig_pie)
    ]),

    html.H2("Bivariate Analysis", className='mt-4'),
    html.Div(className='row', children=[
        create_card(fig.layout.title.text, fig) for fig in bivariate_figs
    ]),
    html.Div(className='row', children=[
        create_card("Correlation Heatmap", fig_heatmap),
        create_card("Cylinders vs Origin Crosstab", fig_heatmap2)
    ]),

    html.H2("Multivariate Analysis", className='mt-4'),
    html.Div(className='row', children=[
        create_card(fig.layout.title.text, fig) for fig in multivariate_figs
    ]),
    
    html.H4("Insights", className='text-primary mt-4'),
    html.Ul([
        html.Li("MPG is negatively correlated with weight and horsepower."),
        html.Li("Japanese cars tend to have higher MPG on average."),
        
        html.Li("mpg and weight(-0.83)-this shows ,higher  weight car always tend to have  low mpg"),
        html.Li("cylinders and displacement (0.95) ,higher engine displacement tend to have high no of cylinders"),
        html.Li("cylinders and mpg(-0.78) ,shows that high no of cylinders in engine tends to strongly decrease mpg"),
        html.Li("horsepower and displacement (0.9) ,this tends high displacement engines have high horse powers."),
        html.Li("mpg and acceleration (0.42) -shows  postive corelation high acceleration cars tends to have high mpg"),
        html.Li("mpg and model year(0.58) -postive corelation "),
        html.Li(" the cars with high weight tends to have high horsepower, low mpeg and high cylinders"),
        html.Li(" cars with more cylinders tends to cluster towars horsepower and lower mpg "),
        html.Li("cars with low horsepower tends to have low cylinders and high mpg "),
        
        html.Li(" USA  origin cars have high weight with low mpg and high number of cylinders "),
        html.Li(" Generally Japan and Europe cars tend to have low weight with high mpg with 4 cylindrs" ),

    ])
    
    
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

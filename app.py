import plotly.express as px
import dash
from dash import html, dcc
import pandas as pd

df = pd.read_csv('mpg.csv')  # Load your data
# fig = px.histogram(df, x='mpg', nbins=30, title='MPG Distribution')

# Assuming df is already loaded
numerical_features = ['mpg', 'displacement', 'horsepower', 'weight', 'acceleration']
univariate_figs = []

for feature in numerical_features:
    fig = px.histogram(df, x=feature, nbins=20, title=f'Distribution of {feature}', marginal="box", opacity=0.75)
    univariate_figs.append(fig)

    
fig1=[]
for feature in numerical_features:
    fig=px.box(df,x=feature,title=f"Distribution of {feature}")
    fig1.append(fig)    
 
categorical_cols = ['cylinders', 'origin', 'model_year'] 
categorical_data=[]
for col in categorical_cols:
    fig=px.histogram(df,x=col,title=f"Count of {col}", color=col)   
    categorical_data.append(fig)  
    
fig_pie = px.pie(df, names='cylinders', title='Distribution of Cylinders')  

##Bivariate analysis
bivariate_figs=[]
fig1 = px.scatter(df, x='horsepower', y='mpg', title='Horsepower vs MPG')
bivariate_figs.append(fig1)
pfig2 = px.scatter(df, x='displacement', y='mpg', title='Displacement vs MPG')
bivariate_figs.append(pfig2)
pfig2 = px.scatter(df, x='weight', y='mpg', title='weight vs MPG')
bivariate_figs.append(pfig2)

fig3 = px.bar(df, x='cylinders', y='mpg', title='MPG vs Cylinders', barmode='group', 
              labels={'mpg': 'Miles per Gallon', 'cylinders': 'Cylinders'})
bivariate_figs.append(fig3)  

fig4 = px.bar(df, x='origin', y='mpg', title='MPG vs Origin', barmode='group',
              labels={'mpg': 'Miles per Gallon', 'origin': 'Origin'})
bivariate_figs.append(fig4)


fig5 = px.bar(df, x='model_year', y='mpg', title='MPG vs Model Year', barmode='group',
              labels={'mpg': 'Miles per Gallon', 'model_year': 'Model Year'})
bivariate_figs.append(fig5)

#lets show heatmap too
# Compute correlation matrix (numeric columns only)
corr = df.corr(numeric_only=True)

fig_heatmap = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale='RdBu_r',
    origin='upper',
    title='Correlation Heatmap'
)

#categorical-categorical column
crosstab=pd.crosstab(df['cylinders'],df['origin'])
fig_heatmap2 = px.imshow(
    crosstab,
    text_auto=True,
    color_continuous_scale='Blues',
    labels=dict(x='Origin', y='Cylinders', color='Count'),
    title='Cylinders vs Origin Crosstab Heatmap'
)


#now lets make multivariate analysis
multivariate=[]
figure = px.scatter(
    df,
    x='weight',
    y='mpg',
    color='origin',  # This adds the hue grouping by 'origin'
    title='MPG vs Weight by Origin',
    labels={'weight': 'Weight', 'mpg': 'Miles per Gallon', 'origin': 'Origin'}
)
multivariate.append(figure)


figure2 = px.scatter(
    df,
    x='horsepower',
    y='mpg',
    color='cylinders',    # categorical coloring
    size='weight',        # size by weight
    title='MPG vs Horsepower with Cylinders and Weight',
    labels={'horsepower': 'Horsepower', 'mpg': 'Miles per Gallon', 'cylinders': 'Cylinders', 'weight': 'Weight'},
    size_max=15           # max size of points
)
multivariate.append(figure2)














app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("MPG Dataset Dashboard"),
    *[dcc.Graph(figure=fig) for fig in univariate_figs],
    *[dcc.Graph(figure=fig) for fig in fig1 ],
    *[dcc.Graph(figure=fig) for fig in categorical_data ],
    *[dcc.Graph(figure=fig_pie) ],
    
    
    html.H1("Bivariate Analysis "),
    *[dcc.Graph(figure=fig) for fig in bivariate_figs],
    *[dcc.Graph(figure=fig_heatmap) ],
    *[dcc.Graph(figure=fig_heatmap2) ],
    
    html.H1("Multi variate Analysis"),
    *[dcc.Graph(figure=fig) for fig in multivariate],
    
    
    
    
])

if __name__ == '__main__':
    app.run(debug=True)

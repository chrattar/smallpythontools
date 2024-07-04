from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

# Load your data
df = pd.read_csv('gmpdata.csv')

# Convert 'Total Revenue' and 'Total Cost' to numeric, removing non-numeric characters like '$' and commas
df['Total Revenue'] = pd.to_numeric(df['Total Revenue'].replace('[\$,]', '', regex=True), errors='coerce')
df['Total Cost'] = pd.to_numeric(df['Total Cost'].replace('[\$,]', '', regex=True), errors='coerce')

# Calculate Gross Margin % and Gross Profit %
df['Gross Margin %'] = (df['Total Revenue'] - df['Total Cost']) / df['Total Revenue'] * 100
df['Gross Profit %'] = df['Gross Margin %']  # Assuming it's calculated similarly

# Ensure 'Period' is treated as a categorical type that can work with the slider
df['Period'] = pd.Categorical(df['Period'])

# Create a consistent color map for 'TopGrp'
unique_groups = df['TopGrp'].unique()
colors = px.colors.qualitative.Plotly  # or any other color palette
color_discrete_map = {group: colors[i % len(colors)] for i, group in enumerate(unique_groups)}

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='revenue-gross-margin-graph'),
    dcc.Graph(id='gross-profit-percentage-graph'),
    dcc.Slider(
        0,
        len(df['Period'].cat.categories) - 1,
        step=None,
        value=0,
        marks={i: str(period) for i, period in enumerate(df['Period'].cat.categories)},
        id='period-slider'
    )
])

@app.callback(
    [Output('revenue-gross-margin-graph', 'figure'),
     Output('gross-profit-percentage-graph', 'figure')],
    [Input('period-slider', 'value')])
def update_figures(selected_period_index):
    selected_period = df['Period'].cat.categories[selected_period_index]
    filtered_df = df[df.Period == selected_period]

    # First graph for Total Revenue and Gross Margin %
    fig1 = px.scatter(filtered_df, x="Total Revenue", y="Gross Margin %",
                      size="Total Revenue", color="TopGrp", hover_name="TopGrp",
                      size_max=60, log_x=True, color_discrete_map=color_discrete_map)

    fig1.update_layout(transition_duration=500)

    # Second graph for Gross Profit % over months
    fig2 = px.scatter(df, x='Period', y='Gross Profit %', color='TopGrp',
                      labels={"Period": "Month", "Gross Profit %": "Gross Profit Percentage"},
                      color_discrete_map=color_discrete_map)

    fig2.update_layout(transition_duration=500)

    return fig1, fig2

if __name__ == '__main__':
    app.run_server(debug=True)

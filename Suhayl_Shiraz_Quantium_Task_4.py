# Suhayl Shiraz
# March 2026
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Read the combined sales file
df = pd.read_csv("Pink_Morsel_Sales_Data.csv")

# Convert the date column to datetime
# Specify dd/mm/yy format
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

app = Dash(__name__)

app.layout = html.Div([
    # Page titles
    html.H1("Soul Foods Pink Morsel Sales", style={"textAlign": "center", "color": "#d81b60"}),
    html.H2("Suhayl Shiraz - March 2026", style={"textAlign": "center", "color": "#d81b60"}),

    # Filtering by regions
    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={"textAlign": "center", "marginBottom": "20px"}
    ),

    dcc.Graph(id="sales-chart")
], style={"width": "80%", "margin": "auto", "paddingTop": "20px"})

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
        title = "All Regions"
    else:
        filtered_df = df[df["Region"] == selected_region]
        title = f"{selected_region.capitalize()} Region"

    # For 'All', combine sales from every region
    sales_by_date = filtered_df.groupby("Date", as_index=False)["Sales"].sum()
    sales_by_date = sales_by_date.sort_values("Date")

    # Create line charts
    fig = px.line(
        sales_by_date,
        x="Date",
        y="Sales",
        title=f"Pink Morsel Sales Over Time - {title}"
    )

    # Axis titles and background colours
    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales ($)",
        plot_bgcolor="#fffafc",
        paper_bgcolor="#fffafc",
        font=dict(color="#333")
    )

    fig.update_traces(line=dict(color="#d81b60"))
    return fig

if __name__ == "__main__":
    app.run(debug=True)

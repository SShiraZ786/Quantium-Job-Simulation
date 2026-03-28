# Suhayl Shiraz
# March 2026
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Use the combined pink morsel sales data sheet
df = pd.read_csv("Pink_Morsel_Sales_Data.csv")

# Convert the date column to datetime
# Must specify dd/mm/yy format since it assumes month first
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

# Not separating based on region
# Must combine all sales on each day
daily_sales = df.groupby("Date", as_index=False)["Sales"].sum()

# Sort by date
daily_sales = daily_sales.sort_values("Date")

# Create the line chart
fig = px.line(
    daily_sales,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales over Time",
)

# Axis labels
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales ($)",
    title_x=0.5
)


# Build Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Pink Morsel Sales Visualiser"),
    html.H2("Suhayl Shiraz - March 2026"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)
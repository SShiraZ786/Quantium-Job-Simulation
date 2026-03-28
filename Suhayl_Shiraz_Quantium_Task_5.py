# Suhayl Shiraz
# March 2026

from Suhayl_Shiraz_Quantium_Task_4 import app

# Check if header is present
def test_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1").text == "Soul Foods Pink Morsel Sales Visualiser"

# Check if visualisation is present
def test_visualisation_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-line-chart") is not None

# Check if region picker is present
def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-filter") is not None

# Run the follwing in the terminal to check
# pytest Suhayl_Shiraz_Quantium_Task_5.py
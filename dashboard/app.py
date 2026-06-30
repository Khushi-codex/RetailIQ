import streamlit as st
import requests

from charts import (
    sales_by_store_chart,
    top_products_chart,
    low_stock_chart
)

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="RetailIQ Dashboard",
    layout="wide"
)

st.title("📊 RetailIQ Dashboard")

# ----------------------------
# Sales Summary
# ----------------------------

st.header("Sales Summary")

summary = requests.get(f"{API_URL}/sales-summary").json()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"{summary['total_sales']:.0f}")
col2.metric("Average Sales", f"{summary['average_sales']:.2f}")
col3.metric("Minimum Sales", f"{summary['minimum_sales']}")
col4.metric("Maximum Sales", f"{summary['maximum_sales']}")

st.divider()

# ----------------------------
# Prediction
# ----------------------------

st.header("Predict Sales")

store = st.number_input("Store", 1, 10, 1)
item = st.number_input("Item", 1, 50, 1)
year = st.number_input("Year", 2013, 2030, 2018)
month = st.number_input("Month", 1, 12, 1)
day = st.number_input("Day", 1, 31, 1)
dayofweek = st.number_input("Day of Week", 0, 6, 0)
weekofyear = st.number_input("Week", 1, 53, 1)
quarter = st.number_input("Quarter", 1, 4, 1)
is_weekend = st.selectbox("Weekend", [0, 1])

if st.button("Predict"):

    payload = {
        "store": store,
        "item": item,
        "year": year,
        "month": month,
        "day": day,
        "dayofweek": dayofweek,
        "weekofyear": weekofyear,
        "quarter": quarter,
        "is_weekend": is_weekend
    }

    response = requests.post(
        f"{API_URL}/predict",
        json=payload
    )

    prediction = response.json()

    if response.status_code == 200:
        st.success(
            f"Predicted Sales: {prediction['predicted_sales']:.2f}"
        )
    else:
        st.error(prediction.get("detail", "Prediction failed"))

st.divider()

# ----------------------------
# Sales by Store
# ----------------------------

st.header("Sales by Store")

stores = requests.get(f"{API_URL}/sales-by-store").json()

st.plotly_chart(
    sales_by_store_chart(stores),
    use_container_width=True
)

st.divider()

# ----------------------------
# Top Products
# ----------------------------

st.header("Top Products")

products = requests.get(f"{API_URL}/top-products").json()

st.plotly_chart(
    top_products_chart(products),
    use_container_width=True
)

st.divider()

# ----------------------------
# Low Stock
# ----------------------------

st.header("Lowest Selling Products")

low_stock = requests.get(f"{API_URL}/low-stock").json()

chart = low_stock_chart(low_stock)

if chart:
    st.plotly_chart(chart, use_container_width=True)
else:
    st.info("No low stock products found.")
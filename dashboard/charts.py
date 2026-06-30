import pandas as pd
import plotly.express as px


def sales_by_store_chart(data):
    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="store",
        y="total_sales",
        title="Total Sales by Store"
    )

    return fig


def top_products_chart(data):
    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="item",
        y="total_sales",
        title="Top 10 Products"
    )

    return fig


def low_stock_chart(data):

    if not data:
        return None

    if isinstance(data, dict):
        data = [data]

    df = pd.DataFrame(data)

    fig = px.bar(
        df,
        x="item",
        y="average_sales",
        title="Lowest Average Sales by Product"
    )

    return fig
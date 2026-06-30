import os
import joblib
import pandas as pd

from fastapi import APIRouter, HTTPException
from sqlalchemy import text

from database.db import engine
from api.schemas import PredictionRequest

router = APIRouter()

import traceback
import os

MODEL_PATH = os.path.join("model", "retail_model.pkl")

print("Current directory:", os.getcwd())
print("Model path:", MODEL_PATH)
print("Model exists:", os.path.exists(MODEL_PATH))

try:
    model = joblib.load(MODEL_PATH)
except Exception as e:
    print("Model could not be loaded:", e)
    model = None
    
@router.get("/")
def home():
    return {"message": "RetailIQ API Running Successfully"}


@router.post("/predict")
def predict(data: PredictionRequest):

    if model is None:
        raise HTTPException(
            status_code=500,
            detail="Model not found. Train the model first."
        )

    df = pd.DataFrame([{
        "store": data.store,
        "item": data.item,
        "year": data.year,
        "month": data.month,
        "day": data.day,
        "dayofweek": data.dayofweek,
        "weekofyear": data.weekofyear,
        "quarter": data.quarter,
        "is_weekend": data.is_weekend
    }])

    prediction = model.predict(df)

    return {
        "predicted_sales": float(prediction[0])
    }


@router.get("/sales-summary")
def sales_summary():

    query = """
    SELECT
        SUM(sales) AS total_sales,
        AVG(sales) AS average_sales,
        MIN(sales) AS minimum_sales,
        MAX(sales) AS maximum_sales
    FROM retail_sales;
    """

    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().first()

    return dict(result)


@router.get("/top-products")
def top_products():

    query = """
    SELECT
        item,
        SUM(sales) AS total_sales
    FROM retail_sales
    GROUP BY item
    ORDER BY total_sales DESC
    LIMIT 10;
    """

    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().all()

    return result


@router.get("/sales-by-store")
def sales_by_store():

    query = """
    SELECT
        store,
        SUM(sales) AS total_sales
    FROM retail_sales
    GROUP BY store
    ORDER BY store;
    """

    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().all()

    return result
@router.get("/low-stock")
def low_stock():

    query = """
    SELECT
    item,
    ROUND(AVG(sales), 2) AS average_sales
    FROM retail_sales
    GROUP BY item
    HAVING AVG(sales) < 20
    ORDER BY average_sales;
    """

    with engine.connect() as conn:
        result = conn.execute(text(query)).mappings().all()

    return result
from pydantic import BaseModel


class PredictionRequest(BaseModel):
    store: int
    item: int
    year: int
    month: int
    day: int
    dayofweek: int
    weekofyear: int
    quarter: int
    is_weekend: int


class PredictionResponse(BaseModel):
    predicted_sales: float
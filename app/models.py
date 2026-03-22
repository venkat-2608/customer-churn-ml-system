from sqlalchemy import Column, Integer, Float
from .database import Base


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True, index=True)
    tenure = Column(Integer)
    monthly_charges = Column(Float)
    prediction = Column(Integer)
from tinydb import TinyDB, JSONStorage

from src.utils import DateTimeSerializer, SerializationMiddleware, DateSerializer

import os

# make sure "data" dir exists
os.makedirs("data", exist_ok=True)

WeightDB = TinyDB("data/weights.db.json", storage=SerializationMiddleware(
    JSONStorage, {"Date": DateSerializer(), "DateTime": DateTimeSerializer()}
))
ExerciseDB = TinyDB("data/exercises.db.json", storage=SerializationMiddleware(
    JSONStorage, {"Date": DateSerializer(), "DateTime": DateTimeSerializer()}
))

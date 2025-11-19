import os

from tinydb import TinyDB

from src.utils import JSONStorageSupportsDates

# make sure "data" dir exists
os.makedirs("data", exist_ok=True)

WeightDB = TinyDB(
    "data/weights.db.json",
    storage=JSONStorageSupportsDates(),
)
ExerciseDB = TinyDB(
    "data/exercises.db.json",
    storage=JSONStorageSupportsDates(),
)

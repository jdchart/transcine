import transcine
import os

DATABASE_PATH = os.path.join(os.getcwd(), "data", "databases", "database.duckdb")
db = transcine.Database(DATABASE_PATH)

db.process_asr(subcorpus = ["9338847d-5e57-42e1-9e77-a049af3187bf"])
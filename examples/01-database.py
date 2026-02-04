import transcine
import os

DATABASE_PATH = os.path.join(os.getcwd(), "data", "databases", "database.duckdb")
VIDEO_FOLDER = '/Users/jacob/Downloads/Les Reportages'

db = transcine.Database(DATABASE_PATH)

db.ingest_folder(VIDEO_FOLDER)

print(db.table_to_pandas("videos"))

db.table_to_pandas("videos").to_csv(os.path.join(os.getcwd(), "OUTPUT.csv"))
import transcine
import os

DATABASE_PATH = os.path.join(os.getcwd(), "data", "databases", "database.duckdb")
VIDEO_FOLDER = "/Users/jacob/Downloads/swisstransfer_5a6b61eb-f3e6-4d8f-b899-b403ff043e9b"

db = transcine.Database(DATABASE_PATH)

db.ingest_folder(VIDEO_FOLDER)


import duckdb
import os
from .utils import collect_files
from .video import get_video_info

class Database:
    def __init__(self, path):
        self.path = path

        if os.path.isfile(path):
            self.db = duckdb.connect(self.path)
        else:
            if os.path.isdir(os.path.split(path)[0]):
                self._init_db()
            else:
                os.makedirs(os.path.split(path)[0], exist_ok = True)
                self._init_db()

    def ingest_folder(self, path):
        # Find path to all videos in path
        video_files = collect_files(path, [".mp4"])

        # Extract info about each video
        for video_file in video_files:
            print(get_video_info(video_file))

                # Extract audio

                # Add to database

    def _init_db(self):
        self.db = duckdb.connect(self.path)
        self._create_table(
            "videos",
            {
                "uuid" : "TEXT", 
                "video_path": "TEXT", 
                "audio_path": "TEXT", 
                "title" : "TEXT", 
                "year": "INT", 
                "duration" : "FLOAT", 
                "width" : "INT", 
                "height" : "INT"
            }
        )

    def get_tables(self):
        return self.db.execute("SHOW TABLES").fetchall()
    
    def _create_table(self, table_name, table_dict):
        execute_string = f"CREATE TABLE {table_name}("

        for header_name in table_dict:
            execute_string = execute_string + f'{header_name} {table_dict[header_name]}, '
        execute_string = execute_string[:-2] + ")"

        self.db.execute(execute_string)
    
    def _remove_table(self, table_name):
        self.db.execute(f"DROP TABLE IF EXISTS {table_name}")

    def add_entry(self, items):
        placeholders = ", ".join("?" for _ in items)
        self.db.execute(f"INSERT INTO videos VALUES ({placeholders})", items)

    def table_to_pandas(self, table_name):
        return self.db.execute(f"SELECT * FROM {table_name}").fetchdf()
import duckdb
import os
from .utils import collect_files, write_json
from .video import get_video_info, extract_audio
from .asr import process_audio
import uuid

class Database:
    def __init__(self, path):
        self.path = path
        self.media_dir = os.path.join(os.path.dirname(path), "media")
        self.data_dir = os.path.join(os.path.dirname(path), "data")

        if os.path.dirname(self.media_dir) == False:
            os.makedirs(self.media_dir, exist_ok = True)
        if os.path.dirname(self.data_dir) == False:
            os.makedirs(self.data_dir, exist_ok = True)

        if os.path.isfile(path):
            self.db = duckdb.connect(self.path)
        else:
            if os.path.isdir(os.path.split(path)[0]):
                self._init_db()
            else:
                os.makedirs(os.path.split(path)[0], exist_ok = True)
                self._init_db()

    def process_asr(self, method = "whisper", model = "turbo", **kwargs):
        subcorpus = kwargs.get("subcorpus", [])
        
        df = self.table_to_pandas("videos")
        for row in df.itertuples(index = False):
            can_process = True
            if len(subcorpus) > 0:
                if row.uuid not in subcorpus:
                    can_process = False
            if can_process == True:
                print(f"Processing {os.path.basename(row.audio_path)} ({row.uuid})...")
                result = process_audio(row.audio_path, method, model)
                
                result_dir = os.path.join(self.data_dir, f"{method}_{model}")
                if os.path.dirname(result_dir) == False:
                    os.makedirs(result_dir, exist_ok = True)
                
                write_json(os.path.join(result_dir, f"{row.uuid}.json"), result)

    def ingest_folder(self, path):
        # Find path to all videos in path
        video_files = collect_files(path, [".mp4"])

        for video_file in video_files:
            # Extract info about each video
            video_info = get_video_info(video_file)

            # Extract audio
            audio_file = extract_audio(video_file, self.media_dir)

            # Add to database
            self.add_entry([
                str(uuid.uuid4()),
                video_file,
                audio_file,
                os.path.basename(video_file),
                1945,
                video_info["duration_ms"],
                video_info["width"],
                video_info["height"]
            ])

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
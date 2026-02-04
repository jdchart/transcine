# transcine
A python package for video transcription

## Usage

```python
db = transcine.Database(DATABASE_PATH)
db.ingest_folder(VIDEO_FOLDER)
```

## Requirements
- You must have [`ffmpeg`](https://www.ffmpeg.org/) installed for the package to work.
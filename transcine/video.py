import os
import mimetypes
from pymediainfo import MediaInfo
import subprocess

def get_video_info(path : str) -> dict:
    """Returns info about a video file"""
    
    info = MediaInfo.parse(path)
    for track in info.tracks:
        if track.track_type == "Video":

            return {
                "width" : track.width,
                "height" : track.height,
                "duration_ms" : track.duration,
                "frame_rate" : float(track.frame_rate),
                "duration_s" : track.duration / 1000
            }
        
def extract_audio(video_path, out_dest, format = "wav"):
    if os.path.isdir(out_dest) == False:
        os.makedirs(out_dest, exist_ok = True)
    
    filename = os.path.basename(video_path)
    filename_no_ext = os.path.splitext(filename)[0]
    outfile = os.path.join(out_dest, f"{filename_no_ext}.{format}")

    if os.path.isfile(outfile) == False:
        subprocess.run([
            "ffmpeg", "-i", video_path, outfile
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
        )

    return outfile
import os
import mimetypes

def get_video_info(path : str) -> dict:
    """Returns info about a video file"""
    
    found, _ = mimetypes.guess_type(os.path.basename(path))
    if found != None:
        if found.split("/") == "video":
            print("On peut continuer")
        else:
            print("Il ne s'agit pas d'un fiuchier video")
            return None
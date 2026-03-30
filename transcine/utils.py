import os
import json

def collect_files(path, accepted_formats):
    ret = []
    
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):

            file_format = os.path.splitext(os.path.basename(full_path))[1]

            if file_format in accepted_formats:
                ret.append(full_path)

    return ret

def write_json(path : str, content : dict, indent : int = 4) -> None:
    """
    Write to json. Will create folder if doesn't exist.
    """
    if os.path.splitext(path)[1] == ".json":
        check_dir_exists(path)

        with open(path, 'w', encoding='utf-8') as f:
            json.dump(content, f, ensure_ascii = False, indent = indent)
    else:
        print(f"{path} needs to be a json file.")

def read_json(path : str) -> dict:
    """Read a json file"""
    if os.path.isfile(path):
        if os.path.splitext(path)[1].lower() == ".json":
            with open(path, 'r') as f:
                return json.load(f)
        else:
            print(f"{path} is not a json file.")
            return None
    else:
        print(f"{path} doesn't exist.")
        return None
    
def check_dir_exists(filepath):
    """Check if folder exists, if not, create it."""
    if os.path.isdir(os.path.dirname(filepath)) == False:
        os.makedirs(os.path.dirname(filepath))
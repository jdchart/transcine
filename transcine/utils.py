import os

def collect_files(path, accepted_formats):
    ret = []
    
    for file in os.listdir(path):
        full_path = os.path.join(path, file)
        if os.path.isfile(full_path):

            file_format = os.path.splitext(os.path.basename(full_path))[1]

            if file_format in accepted_formats:
                ret.append(full_path)

    return ret
import json
import shutil
import os
def move(json_file,score):
    pwd = os.path.abspath('.')
    directory = pwd +'/'+'blur'
    if not os.path.exists(directory):
        os.makedirs(directory)
    with open(json_file) as f:
        data = json.load(f)
        for i in data['results']:
            if i['score'] < score:
                shutil.move(i['input_path'], directory)



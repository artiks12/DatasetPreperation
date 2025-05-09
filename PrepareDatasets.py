import os
from os import listdir
from os.path import isfile, join
import json
from pyquery import PyQuery as pq
import re
import random

def GetDataFiles(path: str, start=0, end=None):
    if not os.path.exists(path):
        os.makedirs(path)
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    
    if end == None: return onlyfiles[start:]
    return onlyfiles[start:end]
    
def SaveDataset(path, onlyfiles, saveFullPath, shuffle = False):
    print(onlyfiles[0],'-',onlyfiles[-1])

    dataset = []

    for file in onlyfiles:
        fullPath = path + '/' + file
        with open(fullPath, encoding='utf-8') as f:
            entries: list = json.load(f)
            for entry in entries:
                temp = {}
                temp['instruction'] = re.sub(r'(\n)+', ' ', pq(entry['Saturi'][0]['Saturs']).text())
                temp['output'] = re.sub(r'(\n)+', ' ', pq(entry['Saturi'][1]['Saturs']).text())
                dataset.append(temp)
    
    if shuffle: random.shuffle(dataset)
    
    with open(saveFullPath, 'wt', encoding='utf-8') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)

def PrepareDataset(path, saveFullPath, start=0, end=None, shuffle = False):
    onlyfiles = GetDataFiles(path, start, end)
    SaveDataset(path, onlyfiles, saveFullPath, shuffle)
    
PrepareDataset('data/Training', 'datasets/instruction_dataset_2881.json', start=-10)
PrepareDataset('data/Training', 'datasets/instruction_dataset_14873.json', start=-58)
PrepareDataset('data/Training', 'datasets/instruction_dataset_all.json')

PrepareDataset('data/Validation', 'datasets/validation_dataset.json')

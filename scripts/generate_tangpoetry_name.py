import json 
import glob

titles = []

files = glob.glob('../data/chinese-poetry/全唐诗/poet.tang.*.json')
print(files)
for file in files:
    with open(file) as f:
        data = json.load(f)
        for item in data:
            if "句" in item['title']:
                continue
            titles.append(item['title'])

with open('../data/tangpoetry_titles.txt', 'w') as f: 
    for title in titles:
        f.write(title + '\n')
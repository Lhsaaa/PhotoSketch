import sys
if sys.version_info[0] < 3:
    raise Exception("Python 2 is about to retire. Please use Python 3")
    
import csv
import os
import urllib.request

IDX_COL = 0
CID_COL = 1
URL_COL = 2
LARGEURL_COL = 3
TAGS_COL = 4

out_dir = 'image'

if not os.path.isdir(out_dir):
    os.makedirs(out_dir)
    
with open('imagemeta.csv', encoding='utf-8') as meta_file:
    reader = csv.reader(meta_file)
    for i, row in enumerate(reader):
        if i < 396:
            continue
        print('Downloading image %d/1000 from %s' % (i, row[URL_COL]))
        name = '%08d.jpg' % i
        urllib.request.urlretrieve(row[URL_COL], os.path.join(out_dir, name))
        
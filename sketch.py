import index
import json
from pprint import pprint
with open('afinn.json') as data_file:
    data = json.load(data_file)

txt = select('#txt')
pprint(data)

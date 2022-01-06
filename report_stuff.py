import json
import re

with open("downloaded-logs-20220105-082917.json", "r") as read_file:
    data = json.load(read_file)

count = 1

for i in data:
    #print(f"{count} {i['textPayload']}")
    s = i['textPayload']

    s_find = re.search('INC[0-9][0-9][0-9][0-9][0-9][0-9][0-9]', s)
    print(f'{count} {s_find.group()}')
    
    count +=1
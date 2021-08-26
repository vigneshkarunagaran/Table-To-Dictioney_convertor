import re
from functools import reduce
from collections import OrderedDict
from pprint import  pprint as pp
from conversionHandler import DataHandler as DATA

#File Handler
with open("sample_input4.txt", "r") as file_object:
    content = file_object.read().split('\n')

#Retrives Table Title
ind = re.findall("[a-zA-Z0-9\s]+", content[0])
table_title = ind[0].strip()

#Retrives and manupulates column headers
next_row = 1
column_heading = []
while '+' not in content[next_row]:
    heading = [x for x in content[next_row].split('|')][1:-1]
    column_heading.append(heading)
    next_row += 1


DATA.validate_header_list(column_heading)
DATA.cleanup_header_list(column_heading)

#Generates keys from header retrived
if len(column_heading) != 1:
    nested_keys = [reduce(DATA.generate_keys,column_heading)][0]
else:
    nested_keys = [list(map(lambda x: x[0].strip(), column_heading[0]))]

header_keys = DATA.extend_keys(nested_keys)

#Table data retrival
next_row += 1
table_data = []
while '+' not in content[next_row]:
    data = [x.strip() for x in content[next_row].split('|')][1:-1]
    table_data.append(data)
    next_row += 1

#Converted output >> list of dict
output_list = [{'Title' : table_title}]

#Converted output >> Dict
output_dictionery = {'Title' : table_title}

# Converted output >> OrderedDict
output_ordered_dictionery = OrderedDict()
output_ordered_dictionery['Title'] = table_title

for i, data in enumerate(table_data):
    output_list.append(dict(zip(header_keys, data)))
    output_dictionery['Row '+str(i)] = dict(zip(header_keys, data))  
    output_ordered_dictionery['Row '+str(i)] = dict(zip(header_keys, data))

print(f'Generated Output for {table_title} table')
# pp(output_list)
pp(output_dictionery)
# pp(output_ordered_dictionery)

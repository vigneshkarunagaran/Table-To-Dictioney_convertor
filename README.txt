# Table-To-Dictioney_convertor
Python script to convert cmd line tables into Dictionary/ List of dictionaries/ OrderedDict using Python

Libs:
import re
import sys
from functools import reduce
from collections import OrderedDict
from pprint import  pprint as pp

Execution:
python table_to_dict_convertor.py <dir of text file containing cmd line table>

Example:
python table_to_dict_convertor.py sample_input1.txt


Sample_input1.txt
+---------------------------- Aggregation  State -----------------------------+
|           Parameter            |                    Value                   |
+--------------------------------+--------------------------------------------+
| Bridge Aggregation Admin       | Enabled                                    |
|                                | Manual (ZTP Disabled)                      |
| Aggregation Group Created      | 11                                         |
| Time Since Last Update         | 001 days 14:20:24                          |
| Time Since Last Selection      | 000 days 01:10:37                          |
| Marker Frame Timeout           | 50   (ms)                                  |
| Total Selection Sm Called      | 471                                        |
+--------------------------------+--------------------------------------------+

Generated Output for Aggregation  State table

Converted output >> Dict

{'Row 0': {'Parameter': 'Bridge Aggregation Admin', 'Value': 'Enabled'},
 'Row 1': {'Parameter': '', 'Value': 'Manual (ZTP Disabled)'},
 'Row 2': {'Parameter': 'Aggregation Group Created', 'Value': '11'},
 'Row 3': {'Parameter': 'Time Since Last Update', 'Value': '001 days 14:20:24'},
 'Row 4': {'Parameter': 'Time Since Last Selection',
           'Value': '000 days 01:10:37'},
 'Row 5': {'Parameter': 'Marker Frame Timeout', 'Value': '50   (ms)'},
 'Row 6': {'Parameter': 'Total Selection Sm Called', 'Value': '471'},
 'Title': 'Aggregation  State'}

Converted output >> list of dict

[{'Title': 'Aggregation  State'},
 {'Parameter': 'Bridge Aggregation Admin', 'Value': 'Enabled'},
 {'Parameter': '', 'Value': 'Manual (ZTP Disabled)'},
 {'Parameter': 'Aggregation Group Created', 'Value': '11'},
 {'Parameter': 'Time Since Last Update', 'Value': '001 days 14:20:24'},
 {'Parameter': 'Time Since Last Selection', 'Value': '000 days 01:10:37'},
 {'Parameter': 'Marker Frame Timeout', 'Value': '50   (ms)'},
 {'Parameter': 'Total Selection Sm Called', 'Value': '471'}]

Converted output >> OrderedDict

OrderedDict([('Title', 'Aggregation  State'),
             ('Row 0',
              {'Parameter': 'Bridge Aggregation Admin', 'Value': 'Enabled'}),
             ('Row 1', {'Parameter': '', 'Value': 'Manual (ZTP Disabled)'}),
             ('Row 2',
              {'Parameter': 'Aggregation Group Created', 'Value': '11'}),
             ('Row 3',
              {'Parameter': 'Time Since Last Update',
               'Value': '001 days 14:20:24'}),
             ('Row 4',
              {'Parameter': 'Time Since Last Selection',
               'Value': '000 days 01:10:37'}),
             ('Row 5',
              {'Parameter': 'Marker Frame Timeout', 'Value': '50   (ms)'}),
             ('Row 6',
              {'Parameter': 'Total Selection Sm Called', 'Value': '471'})])

Sample_input2.txt
+-------------------------------- L3 INTERFACE OPERATIONAL STATE ------------------------------+-----------------+
|                 |        |                                             | Admin    | Oper     | Vrf             |
| Name            | Type   | IP Address/Prefix                           | State    | State    | Name            |
+-----------------+--------+---------------------------------------------+----------+----------+-----------------+
| AT-ne1-loop     | loop   | 1.1.1.1/32                                  | Enabled  | Enabled  | default         |
| AT_IP1_11       | p2p    | 11.11.1.1/24                                | Enabled  | Enabled  | default         |
| AT_IP2_11       | p2p    | 11.11.2.1/24                                | Enabled  | Enabled  | default         |
| AT_IP5_11       | p2p    | 11.11.5.1/24                                | Enabled  | Enabled  | default         |
+-----------------+--------+---------------------------------------------+----------+----------+-----------------+
Generated Output for L3 INTERFACE OPERATIONAL STATE table

Converted output >> Dict

{'Row 0': {' IP Address/Prefix': '1.1.1.1/32',
           ' Name': 'AT-ne1-loop',
           ' Type': 'loop',
           'Admin State': 'Enabled',
           'Oper State': 'Enabled',
           'Vrf Name': 'default'},
 'Row 1': {' IP Address/Prefix': '11.11.1.1/24',
           ' Name': 'AT_IP1_11',
           ' Type': 'p2p',
           'Admin State': 'Enabled',
           'Oper State': 'Enabled',
           'Vrf Name': 'default'},
 'Row 2': {' IP Address/Prefix': '11.11.2.1/24',
           ' Name': 'AT_IP2_11',
           ' Type': 'p2p',
           'Admin State': 'Enabled',
           'Oper State': 'Enabled',
           'Vrf Name': 'default'},
 'Row 3': {' IP Address/Prefix': '11.11.5.1/24',
           ' Name': 'AT_IP5_11',
           ' Type': 'p2p',
           'Admin State': 'Enabled',
           'Oper State': 'Enabled',
           'Vrf Name': 'default'},
 'Title': 'L3 INTERFACE OPERATIONAL STATE'}

Converted output >> list of dict

[{'Title': 'L3 INTERFACE OPERATIONAL STATE'},
 {' IP Address/Prefix': '1.1.1.1/32',
  ' Name': 'AT-ne1-loop',
  ' Type': 'loop',
  'Admin State': 'Enabled',
  'Oper State': 'Enabled',
  'Vrf Name': 'default'},
 {' IP Address/Prefix': '11.11.1.1/24',
  ' Name': 'AT_IP1_11',
  ' Type': 'p2p',
  'Admin State': 'Enabled',
  'Oper State': 'Enabled',
  'Vrf Name': 'default'},
 {' IP Address/Prefix': '11.11.2.1/24',
  ' Name': 'AT_IP2_11',
  ' Type': 'p2p',
  'Admin State': 'Enabled',
  'Oper State': 'Enabled',
  'Vrf Name': 'default'},
 {' IP Address/Prefix': '11.11.5.1/24',
  ' Name': 'AT_IP5_11',
  ' Type': 'p2p',
  'Admin State': 'Enabled',
  'Oper State': 'Enabled',
  'Vrf Name': 'default'}]

Converted output >> OrderedDict

OrderedDict([('Title', 'L3 INTERFACE OPERATIONAL STATE'),
             ('Row 0',
              {' IP Address/Prefix': '1.1.1.1/32',
               ' Name': 'AT-ne1-loop',
               ' Type': 'loop',
               'Admin State': 'Enabled',
               'Oper State': 'Enabled',
               'Vrf Name': 'default'}),
             ('Row 1',
              {' IP Address/Prefix': '11.11.1.1/24',
               ' Name': 'AT_IP1_11',
               ' Type': 'p2p',
               'Admin State': 'Enabled',
               'Oper State': 'Enabled',
               'Vrf Name': 'default'}),
             ('Row 2',
              {' IP Address/Prefix': '11.11.2.1/24',
               ' Name': 'AT_IP2_11',
               ' Type': 'p2p',
               'Admin State': 'Enabled',
               'Oper State': 'Enabled',
               'Vrf Name': 'default'}),
             ('Row 3',
              {' IP Address/Prefix': '11.11.5.1/24',
               ' Name': 'AT_IP5_11',
               ' Type': 'p2p',
               'Admin State': 'Enabled',
               'Oper State': 'Enabled',
               'Vrf Name': 'default'})])

Sample_input3.txt
+-------------------- PORT 3/1 INFO ------------------------------------------+
| Field                   | Admin                   | Oper                    |
+-------------------------+-------------------------+-------------------------+
| Description             |                         |                         |
| Type                    | 10GigEthernet           |                         |
| Port AID                | ETTP-6-3-1              |                         |
| Interface OID           | ifIndex.101569          |                         |
| Link State              | Enabled                 | Enabled                 |
| ETTP Status             | Enabled                 |                         |
| Port Status             | Enabled                 |                         |
| Degrade Detection Status| Disabled                | none                    |
| Speed                   | 10 Gbps                 | 10 Gbps                 |
| Duplex                  | full                    | full                    |
+-------------------------+-------------------------+-------------------------+

Generated Output for PORT 3 table

Converted output >> Dict

{'Row 0': {'Admin': '', 'Field': 'Description', 'Oper': ''},
 'Row 1': {'Admin': '10GigEthernet', 'Field': 'Type', 'Oper': ''},
 'Row 2': {'Admin': 'ETTP-6-3-1', 'Field': 'Port AID', 'Oper': ''},
 'Row 3': {'Admin': 'ifIndex.101569', 'Field': 'Interface OID', 'Oper': ''},
 'Row 4': {'Admin': 'Enabled', 'Field': 'Link State', 'Oper': 'Enabled'},
 'Row 5': {'Admin': 'Enabled', 'Field': 'ETTP Status', 'Oper': ''},
 'Row 6': {'Admin': 'Enabled', 'Field': 'Port Status', 'Oper': ''},
 'Row 7': {'Admin': 'Disabled',
           'Field': 'Degrade Detection Status',
           'Oper': 'none'},
 'Row 8': {'Admin': '10 Gbps', 'Field': 'Speed', 'Oper': '10 Gbps'},
 'Row 9': {'Admin': 'full', 'Field': 'Duplex', 'Oper': 'full'},
 'Title': 'PORT 3'}

Converted output >> list of dict

[{'Title': 'PORT 3'},
 {'Admin': '', 'Field': 'Description', 'Oper': ''},
 {'Admin': '10GigEthernet', 'Field': 'Type', 'Oper': ''},
 {'Admin': 'ETTP-6-3-1', 'Field': 'Port AID', 'Oper': ''},
 {'Admin': 'ifIndex.101569', 'Field': 'Interface OID', 'Oper': ''},
 {'Admin': 'Enabled', 'Field': 'Link State', 'Oper': 'Enabled'},
 {'Admin': 'Enabled', 'Field': 'ETTP Status', 'Oper': ''},
 {'Admin': 'Enabled', 'Field': 'Port Status', 'Oper': ''},
 {'Admin': 'Disabled', 'Field': 'Degrade Detection Status', 'Oper': 'none'},
 {'Admin': '10 Gbps', 'Field': 'Speed', 'Oper': '10 Gbps'},
 {'Admin': 'full', 'Field': 'Duplex', 'Oper': 'full'}]

Converted output >> OrderedDict

OrderedDict([('Title', 'PORT 3'),
             ('Row 0', {'Admin': '', 'Field': 'Description', 'Oper': ''}),
             ('Row 1', {'Admin': '10GigEthernet', 'Field': 'Type', 'Oper': ''}),
             ('Row 2',
              {'Admin': 'ETTP-6-3-1', 'Field': 'Port AID', 'Oper': ''}),
             ('Row 3',
              {'Admin': 'ifIndex.101569',
               'Field': 'Interface OID',
               'Oper': ''}),
             ('Row 4',
              {'Admin': 'Enabled', 'Field': 'Link State', 'Oper': 'Enabled'}),
             ('Row 5',
              {'Admin': 'Enabled', 'Field': 'ETTP Status', 'Oper': ''}),
             ('Row 6',
              {'Admin': 'Enabled', 'Field': 'Port Status', 'Oper': ''}),
             ('Row 7',
              {'Admin': 'Disabled',
               'Field': 'Degrade Detection Status',
               'Oper': 'none'}),
             ('Row 8',
              {'Admin': '10 Gbps', 'Field': 'Speed', 'Oper': '10 Gbps'}),
             ('Row 9', {'Admin': 'full', 'Field': 'Duplex', 'Oper': 'full'})])

Sample_input4.txt
+------------------------------------- PHYSICAL PORT INFO ----------------------------------------------+
|  Port        | AggMode |AggAdmin     |ActAdmSt| ActorOperState  |ActorKey |     LacpduStats     |     |
|  Name     |Op|Adm |Oper|Add2  |Sel2  |AC|TO|AG|AC|TO|AG|Agg|Dist|Adm |Oper| Tx       | Rx       | BFD |
+-----------+--+----+----+------+------+--+--+--+--+--+--+---+----+----+----+----------+----------+-----+
|3/1        |UP|Manu|Manu|------|  1569|A | L|A |A | L|A | T | T  |0621|0621|         0|         0| n/a |
|7/3        |UP|Manu|Manu|------|  4035|A | L|A |A | L|A | T | T  |0FC3|0FC3|         0|         0| n/a |
|8/3        |UP|Manu|Manu|------|  4547|A | L|A |A | L|A | T | T  |11C3|11C3|         0|         0| n/a |
+-----------+--+----+----+------+------+--+--+--+--+--+--+---+----+----+----+----------+----------+-----+
Generated Output for PHYSICAL PORT INFO table

Converted output >> Dict

{'Row 0': {' BFD': 'n/a',
           'ActAdmSt AC': 'A',
           'ActAdmSt AG': 'A',
           'ActAdmSt TO': 'L',
           'ActorKey Adm': '0621',
           'ActorKey Oper': '0621',
           'ActorOperState AC': 'A',
           'ActorOperState AG': 'A',
           'ActorOperState Agg': 'T',
           'ActorOperState Dist': 'T',
           'ActorOperState TO': 'L',
           'AggAdmin Add2': '------',
           'AggAdmin Sel2': '1569',
           'AggMode Adm': 'Manu',
           'AggMode Oper': 'Manu',
           'LacpduStats Rx': '0',
           'LacpduStats Tx': '0',
           'Port Name': '3/1',
           'Port Op': 'UP'},
 'Row 1': {' BFD': 'n/a',
           'ActAdmSt AC': 'A',
           'ActAdmSt AG': 'A',
           'ActAdmSt TO': 'L',
           'ActorKey Adm': '0FC3',
           'ActorKey Oper': '0FC3',
           'ActorOperState AC': 'A',
           'ActorOperState AG': 'A',
           'ActorOperState Agg': 'T',
           'ActorOperState Dist': 'T',
           'ActorOperState TO': 'L',
           'AggAdmin Add2': '------',
           'AggAdmin Sel2': '4035',
           'AggMode Adm': 'Manu',
           'AggMode Oper': 'Manu',
           'LacpduStats Rx': '0',
           'LacpduStats Tx': '0',
           'Port Name': '7/3',
           'Port Op': 'UP'},
 'Row 2': {' BFD': 'n/a',
           'ActAdmSt AC': 'A',
           'ActAdmSt AG': 'A',
           'ActAdmSt TO': 'L',
           'ActorKey Adm': '11C3',
           'ActorKey Oper': '11C3',
           'ActorOperState AC': 'A',
           'ActorOperState AG': 'A',
           'ActorOperState Agg': 'T',
           'ActorOperState Dist': 'T',
           'ActorOperState TO': 'L',
           'AggAdmin Add2': '------',
           'AggAdmin Sel2': '4547',
           'AggMode Adm': 'Manu',
           'AggMode Oper': 'Manu',
           'LacpduStats Rx': '0',
           'LacpduStats Tx': '0',
           'Port Name': '8/3',
           'Port Op': 'UP'},
 'Title': 'PHYSICAL PORT INFO'}

Converted output >> list of dict

[{'Title': 'PHYSICAL PORT INFO'},
 {' BFD': 'n/a',
  'ActAdmSt AC': 'A',
  'ActAdmSt AG': 'A',
  'ActAdmSt TO': 'L',
  'ActorKey Adm': '0621',
  'ActorKey Oper': '0621',
  'ActorOperState AC': 'A',
  'ActorOperState AG': 'A',
  'ActorOperState Agg': 'T',
  'ActorOperState Dist': 'T',
  'ActorOperState TO': 'L',
  'AggAdmin Add2': '------',
  'AggAdmin Sel2': '1569',
  'AggMode Adm': 'Manu',
  'AggMode Oper': 'Manu',
  'LacpduStats Rx': '0',
  'LacpduStats Tx': '0',
  'Port Name': '3/1',
  'Port Op': 'UP'},
 {' BFD': 'n/a',
  'ActAdmSt AC': 'A',
  'ActAdmSt AG': 'A',
  'ActAdmSt TO': 'L',
  'ActorKey Adm': '0FC3',
  'ActorKey Oper': '0FC3',
  'ActorOperState AC': 'A',
  'ActorOperState AG': 'A',
  'ActorOperState Agg': 'T',
  'ActorOperState Dist': 'T',
  'ActorOperState TO': 'L',
  'AggAdmin Add2': '------',
  'AggAdmin Sel2': '4035',
  'AggMode Adm': 'Manu',
  'AggMode Oper': 'Manu',
  'LacpduStats Rx': '0',
  'LacpduStats Tx': '0',
  'Port Name': '7/3',
  'Port Op': 'UP'},
 {' BFD': 'n/a',
  'ActAdmSt AC': 'A',
  'ActAdmSt AG': 'A',
  'ActAdmSt TO': 'L',
  'ActorKey Adm': '11C3',
  'ActorKey Oper': '11C3',
  'ActorOperState AC': 'A',
  'ActorOperState AG': 'A',
  'ActorOperState Agg': 'T',
  'ActorOperState Dist': 'T',
  'ActorOperState TO': 'L',
  'AggAdmin Add2': '------',
  'AggAdmin Sel2': '4547',
  'AggMode Adm': 'Manu',
  'AggMode Oper': 'Manu',
  'LacpduStats Rx': '0',
  'LacpduStats Tx': '0',
  'Port Name': '8/3',
  'Port Op': 'UP'}]

Converted output >> OrderedDict

OrderedDict([('Title', 'PHYSICAL PORT INFO'),
             ('Row 0',
              {' BFD': 'n/a',
               'ActAdmSt AC': 'A',
               'ActAdmSt AG': 'A',
               'ActAdmSt TO': 'L',
               'ActorKey Adm': '0621',
               'ActorKey Oper': '0621',
               'ActorOperState AC': 'A',
               'ActorOperState AG': 'A',
               'ActorOperState Agg': 'T',
               'ActorOperState Dist': 'T',
               'ActorOperState TO': 'L',
               'AggAdmin Add2': '------',
               'AggAdmin Sel2': '1569',
               'AggMode Adm': 'Manu',
               'AggMode Oper': 'Manu',
               'LacpduStats Rx': '0',
               'LacpduStats Tx': '0',
               'Port Name': '3/1',
               'Port Op': 'UP'}),
             ('Row 1',
              {' BFD': 'n/a',
               'ActAdmSt AC': 'A',
               'ActAdmSt AG': 'A',
               'ActAdmSt TO': 'L',
               'ActorKey Adm': '0FC3',
               'ActorKey Oper': '0FC3',
               'ActorOperState AC': 'A',
               'ActorOperState AG': 'A',
               'ActorOperState Agg': 'T',
               'ActorOperState Dist': 'T',
               'ActorOperState TO': 'L',
               'AggAdmin Add2': '------',
               'AggAdmin Sel2': '4035',
               'AggMode Adm': 'Manu',
               'AggMode Oper': 'Manu',
               'LacpduStats Rx': '0',
               'LacpduStats Tx': '0',
               'Port Name': '7/3',
               'Port Op': 'UP'}),
             ('Row 2',
              {' BFD': 'n/a',
               'ActAdmSt AC': 'A',
               'ActAdmSt AG': 'A',
               'ActAdmSt TO': 'L',
               'ActorKey Adm': '11C3',
               'ActorKey Oper': '11C3',
               'ActorOperState AC': 'A',
               'ActorOperState AG': 'A',
               'ActorOperState Agg': 'T',
               'ActorOperState Dist': 'T',
               'ActorOperState TO': 'L',
               'AggAdmin Add2': '------',
               'AggAdmin Sel2': '4547',
               'AggMode Adm': 'Manu',
               'AggMode Oper': 'Manu',
               'LacpduStats Rx': '0',
               'LacpduStats Tx': '0',
               'Port Name': '8/3',
               'Port Op': 'UP'})])

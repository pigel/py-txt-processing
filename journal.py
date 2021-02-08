#!/usr/bin/env python
'''
Script for convert file (input_file)
To further open in Exel as CSV (separator ;)
Exemple run $./journal.py <input_file>
'''
import sys
fr_name = sys.argv[1]
fw_name = 'table_' + fr_name
fr = open(fr_name, 'r')
fw = open(fw_name, 'w')
for line in fr:
    w_line = ''
    data = line[0:10]
    nkm = line[11:27]
    if len(line) > 36:  # activation
        if line[-6].isdigit() :  # nomer a000aa000
            nom = line[-12:-1]
            if line[-14].isdigit():  # vin
                vin = line[-30:-13]
                org = line[29:-30]
            else:  # no vin
                vin = '-'
                org = line[29:-13]
        else:  # nomer a000aa00
            nom = line[-11:-1]
            if line[-13].isdigit() : #vin
                vin = line[-29:-12]
                org = line[29:-29]
            else:  # no vin
                vin = '-'
                org = line[29:-12]
        w_line = data + ';' + nkm + ';' + org + ';' + vin + ';' + nom + '\n'
    else:  # deactivation
        w_line = data + ';' + nkm + '; ; ; ' + '\n'
    fw.write(w_line)
print('Complete OK')
fr.close()
fw.close()
exit()

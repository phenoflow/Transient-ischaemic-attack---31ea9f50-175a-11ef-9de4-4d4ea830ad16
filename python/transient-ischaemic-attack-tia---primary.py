# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"14AB.00","system":"readv2"},{"code":"2417.0","system":"readv2"},{"code":"18996.0","system":"readv2"},{"code":"15788.0","system":"readv2"},{"code":"19354.0","system":"readv2"},{"code":"10794.0","system":"readv2"},{"code":"1895.0","system":"readv2"},{"code":"6489.0","system":"readv2"},{"code":"1433.0","system":"readv2"},{"code":"105738.0","system":"readv2"},{"code":"63746.0","system":"readv2"},{"code":"28278.0","system":"readv2"},{"code":"16507.0","system":"readv2"},{"code":"19004.0","system":"readv2"},{"code":"100015.0","system":"readv2"},{"code":"1195.0","system":"readv2"},{"code":"504.0","system":"readv2"},{"code":"5268.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('transient-ischaemic-attack-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["transient-ischaemic-attack-tia---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["transient-ischaemic-attack-tia---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["transient-ischaemic-attack-tia---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

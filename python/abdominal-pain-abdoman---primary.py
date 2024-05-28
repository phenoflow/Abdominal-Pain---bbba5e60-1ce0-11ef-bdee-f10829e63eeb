# Rebecca M Joseph, Ruth H Jack, Richard Morriss, Roger David Knaggs, Debbie Buttler, Chris Hollis, Julia Hippisley-Cox, Carrol Coupland, 2024.

import sys, csv, re

codes = [{"code":"25C..00","system":"readv2"},{"code":"25C5.00","system":"readv2"},{"code":"25C7.00","system":"readv2"},{"code":"Ryu1000","system":"readv2"},{"code":"25C3.00","system":"readv2"},{"code":"1964","system":"readv2"},{"code":"25CA.00","system":"readv2"},{"code":"25C8.00","system":"readv2"},{"code":"25C9.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-pain-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-pain-abdoman---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-pain-abdoman---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-pain-abdoman---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

# Rebecca M Joseph, Ruth H Jack, Richard Morriss, Roger David Knaggs, Debbie Buttler, Chris Hollis, Julia Hippisley-Cox, Carrol Coupland, 2024.

import sys, csv, re

codes = [{"code":"1969000","system":"readv2"},{"code":"R073200","system":"readv2"},{"code":"197Z.00","system":"readv2"},{"code":"R090C00","system":"readv2"},{"code":"196A.00","system":"readv2"},{"code":"R090800","system":"readv2"},{"code":"1962","system":"readv2"},{"code":"196Z.00","system":"readv2"},{"code":"197A.00","system":"readv2"},{"code":"1979","system":"readv2"},{"code":"196..12","system":"readv2"},{"code":"1971","system":"readv2"},{"code":"197..00","system":"readv2"},{"code":"1963","system":"readv2"},{"code":"R090E00","system":"readv2"},{"code":"R090700","system":"readv2"},{"code":"R090P00","system":"readv2"},{"code":"197A.11","system":"readv2"},{"code":"R090B00","system":"readv2"},{"code":"R090z00","system":"readv2"},{"code":"196..00","system":"readv2"},{"code":"197..13","system":"readv2"},{"code":"R090N00","system":"readv2"},{"code":"R090y00","system":"readv2"},{"code":"Ryu1100","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-pain-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-pain---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-pain---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-pain---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)

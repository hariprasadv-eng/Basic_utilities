def convertcsvtoexcel(source, target):
    import csv
    import openpyxl, os
    for filename in os.listdir(source):
        print(filename)
        infilename = os.path.join(source, filename)
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = filename.replace('.csv', '')
        f = open(infilename)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            ws.append(row)
        output = os.path.join(target, (filename.replace('.csv', '') + '.xlsx'))
        f.close()
        wb.save(output)


source = u'.'
target = u'.\Excel\'
convertcsvtoexcel(source, target)

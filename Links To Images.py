import openpyxl

wb = openpyxl.load_workbook(filename='H:\Documents\Excel\Baths eBay Table.xlsx')
ws = wb.active

column = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
h = 0
for col in column:
    i=0

    for cell in ws[col]:
        try:
            if cell.value == '.jpg' or cell.value == '.JPG':
                cell.value = 'NULL'
            elif  str(cell.value) != 'None' and '.jpg' in cell.value or '.JPG' in cell.value and cell.value != 'NULL' and cell.value != '' and cell.value != '.jpg':
                cell.value = cell.value.replace('.jpg', '_ebay.jpg')
                cell.value = cell.value.replace('.JPG', '_ebay.jpg')
                cell.value = 'https://www.bathroomcity.co.uk/sites/default/files/external/' + cell.value
                print(cell.value)

            i+=1
        except:
            print('ERROR: ' + str(cell.value))
    h += 1
    wb.save('sample.xlsx')

import openpyxl

wb = openpyxl.load_workbook(filename='H:\Scripts\Auto eBay Cat Filler\BATHS MASTER For eBay Table.xlsx')
ws = wb.active

column = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
h = 0
for col in column:
    i=0

    for cell in ws[col]:
        try:
            if str(cell.value) != 'None' and cell.value != 'NULL' and cell.value != '':
                cell.value = cell.value.replace('https://www.bathroomcity.co.uk/sites/default/files/external/', '')
                cell.value = cell.value.replace('https://www.Bathroomcity.co.uk/sites/default/files/external/', '')
                print(cell.value)

            i+=1
        except:
            print('ERROR: ' + str(cell.value))
    h += 1
    wb.save('BATHS Without URLs.xlsx')

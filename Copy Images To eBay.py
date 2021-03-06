from shutil import copyfile
import openpyxl
from PIL import Image

wb = openpyxl.load_workbook(filename='H:\Documents\Excel\MASTER - SHOWER ENCLOSURES.xlsx')
ws = wb.active

column = ['E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']

for col in column:
    i=0
    for cell in ws[col]:
        if cell.value == '.jpg' or cell.value == '.JPG':
            cell.value = 'NULL'
        elif cell.value != None:
            if '.jpg' in cell.value.lower() and cell.value != 'NULL' and cell.value != '' and cell.value != '.jpg':
                try:
                    imgSize = Image.open('Z:/' + cell.value).size
                    if imgSize[0] > 500 and imgSize[1] > 500:
                        copyfile('Z:/' + cell.value, 'Z:/eBay/ebay_upload/' + cell.value.lower().replace('.jpg', '_ebay.jpg'))
                        print(cell.value)
                        cell.value = cell.value.lower().replace('.jpg', '_ebay.jpg')
                    else:
                        with open('Too Small.txt', 'a') as txt:
                            txt.write(cell.value + '\n')
                except FileNotFoundError:
                    with open('Not Found.txt', 'a') as txt:
                        txt.write(cell.value + '\n')
        i+=1
wb.save('MASTER - SHOWER ENCLOSURES NEW.xlsx')
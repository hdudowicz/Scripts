import openpyxl
from urllib.request import Request, urlopen
from urllib.error import HTTPError


wb = openpyxl.load_workbook(filename='H:\Scripts\MASTER - SHOWER ENCLOSURES NEWW.xlsm')
ws = wb.active

column = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
imgheaders = ['Image1', 'Image2', 'Image3',	'Image4', 'Image5', 'Image6', 'Image7', 'Image8', 'Image9', 'Image10', 'Image11','eDrawing']

h = 0
for col in column:

    for cell in ws[col]:
        try:
            if cell.value != "NULL" and cell.value != None and cell.value not in imgheaders:
                req = Request('https://www.bathroomcity.co.uk/sites/default/files/external/' + cell.value,
                              headers={'User-Agent': 'Mozilla/5.0'})
                a = urlopen(req)
                print(a.getcode())
                if a.getcode() == 200:
                    print(cell.value + " - Valid!")
        except:
            print(str(cell.value) + ' - Failed!')

            with open('Invalid Img Links.txt', 'r+') as txt:
                if cell.value not in txt.read():
                    txt.write('https://www.bathroomcity.co.uk/sites/default/files/external/' + cell.value + '\n')


    h += 1

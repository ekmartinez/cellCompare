import xlwings as xw
from xlwings import Range, constants

app1 = xw.apps
wb = app1.active.books.active

payRate = [10.25, 12.55, 13.45, 15.65, 25.45]

Range('A1').value = 'Pay Rate'
Range('A2:A6').options(transpose=True).value = payRate

for x in Range('A2:A6'):
    if x.value > 13:
        x.api.Interior.ColorIndex = 6
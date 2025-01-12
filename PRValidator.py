import openpyxl
import re
from openpyxl import load_workbook

def find_errors(path):
    wb = load_workbook(path)
    ws = wb.active

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):

        personnummer = row[4].value  # Index 4 corresponds to column E


        if(personnummer is None):
            print(f'Manglende personnummer på linje {row[0].row}')
        elif not re.match(r'^\d{5}$', str(personnummer)):
            print(f'Feil personnummer på linje {row[0].row} Verdi: {personnummer}')

find_errors('D:/Viktor/Bodø kommune. Barnehagekontoret. Fa 1-45. AKS_23_157_7.xlsx')
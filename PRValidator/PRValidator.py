import re
import datetime
from openpyxl import load_workbook

kommuneInfo = {
    1804: 'Bodø',
    1806: 'Narvik',
    1811: 'Bindal',
    1812: 'Sømna',
    1813: 'Brønnøy',
    1815: 'Vega',
    1816: 'Vevelstad',
    1818: 'Herøy',
    1820: 'Alstahaug',
    1822: 'Leirfjord',
    1824: 'Vefsn',
    1825: 'Grane',
    1826: 'Hattfjelldal',
    1827: 'Dønna',
    1828: 'Nesna',
    1832: 'Hemnes',
    1833: 'Rana',
    1834: 'Lurøy',
    1835: 'Træna',
    1836: 'Rødøy',
    1837: 'Meløy',
    1838: 'Gildeskål',
    1839: 'Beiarn',
    1840: 'Saltdal',
    1841: 'Fauske',
    1845: 'Sørfold',
    1848: 'Steigen',
    1851: 'Lødingen',
    1853: 'Evenes',
    1856: 'Røst',
    1857: 'Værøy',
    1859: 'Flakstad',
    1860: 'Vestvågøy',
    1865: 'Vågan',
    1866: 'Hadsel',
    1867: 'Bø',
    1868: 'Øksnes',
    1870: 'Sortland',
    1871: 'Andøy',
    1874: 'Moskenes',
    1875: 'Hamarøy'
}


def find_errors(path):
    wb = load_workbook(path)
    ws = wb.active

    error_string = ""

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):

        kommune = row[0].value
        kommunenr = row[1].value
        archiveCreator = row[2].value
        birthDate = row[3].value
        personnr = row[4].value  # Index 4 corresponds to column E
        lastName = row[5].value
        firstName = row[6].value
        middleName = row[7].value
        noOfDir = row[8].value
        box = row[9].value
        dirType = row[10].value
        morsDate = row[11].value
        dirSharedWith = row[12].value



        error_string += validateKommune(kommune=kommune, kommunenr=kommunenr, row=row[0].row)

        if(archiveCreator is None):
            error_string += f'Manglende personnummer på linje {row[0].row}\n'

        error_string += validateBirthDate(birthDate=birthDate, row=row[0].row)
        # error_string += validatePersonnr(personnr=personnr, row=row[0].row)
        
    return error_string



def validateKommune(kommune, kommunenr, row):

    valid = True

    text = ""

    if kommune not in kommuneInfo.values():
        text += f'Feil eller manglende kommune på rad: {row}\n'
        valid = False

    if kommunenr not in kommuneInfo.keys():
        text += f'Feil eller manglende kommunenummer på rad: {row}\n'
        valid = False

    if not valid:
        return text

    if (kommune != kommuneInfo.get(kommunenr)):
        text += f'Kommune har feil kommunenummer på rad: {row}\n'

    return text


def validateBirthDate(birthDate, row):

    if(isinstance(birthDate, datetime.datetime)):
        birthDate = birthDate.strftime('%d%m%Y')

    if(birthDate is not None):
        birthDate = str(birthDate).strip(" ")

    if birthDate is None or len(birthDate) == 0:
        return f'Manglende fødseldato på rad: {row}\n'
        

    elif not re.match(r'^(0[1-9]|[12][0-9]|3[01])(0[1-9]|1[0-2])\d{4}$', birthDate):
        return f'Feil format på fødselsdato på rad: {row}\n'
    
    return ""

def validatePersonnr(personnr, row):
    if(personnr is None):
        return f'Manglende personnummer på linje {row}\n'
    elif not re.match(r'^\d{5}$', str(personnr)):
        return f'Feil personnummer på linje {row} Verdi: {personnr}\n'
    
    return ""




# print(find_errors('D:/Viktor/Bodø kommune. Barnehagekontoret. Fa 1-45. AKS_23_157_7.xlsx'))
# find_errors('D:/Viktor/Narvik kommune. Skolestyre.Fa 1-180. AKS_20_137.xlsx')
# find_errors('D:/Viktor/Vefsn Kommune HR Avdeling Personal sortert stigende på etternavn.xlsx')
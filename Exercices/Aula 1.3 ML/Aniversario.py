from datetime import date, datetime
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR')

aniversarios = ['01/02/1990', '22 de Maio de 1991', '04/Abr/1995', '1995-Outubro-10', '12 Julho 1989',
                '16 de Junho de 1987', '04/07/1990', '25/03/2020']
# Addicionei uma data teste a mais para o aniversario: 25/03/2020

aniversariosTratados = []


def tratarData(txt):
    for fmt in ('%d de %B de %Y', '%d/%m/%Y', '%d/%b/%Y', '%Y-%B-%d', '%d %B %Y'):
        try:
            return datetime.strptime(txt, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')


for x in aniversarios:
    aniversariosTratados.append(tratarData(x))

aniversariosTratados = sorted(
    aniversariosTratados, key=lambda x: (x.month, x.day))

hoje = datetime(datetime.now().year, datetime.now().month, datetime.now().day)

for x in aniversariosTratados:
    if(hoje.day == x.day and hoje.month == x.month):
        print(hoje.strftime("Hoje, %A %d de %B de %Y, Tem Aniversario!"))
        break

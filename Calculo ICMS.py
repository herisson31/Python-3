print('='*30)
print(f'{"*** CALCULO DE ICMS ***":^30}')
print('='*30)

#ICMSori = ('AC': 17,'AL': 18,'AM': 18,'AP':18,'BA':18,
#           'CE':18, 'DF': 18,'ES': 17,'GO': 17,'MA':18,
#           'MT': 17,'MS': 17,'MG': 18,'PA': 17,'PB': 18)

icmsor = int(input('ICMS: '))
estado = str(input('Estado: ')).strip().upper()
nota = float(input('Valor da nota: '))
calcicms = nota * icmsor/100

print(f'O valor do ICMS é R$ {calcicms:.2f} em {estado}')

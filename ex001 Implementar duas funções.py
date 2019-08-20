'''Implementar duas funções:
   * Uma que converta temperatura em graus Celsius para Fahrenheit.
   * Outra que converta temperatura em graus Fahrenheit para Celsius.
   Lembrando que:

   f = 9/8 * c + 32'''

def fahrenheit():
    c = int(input('Digite em graus Celsius: '))
    f = (c * 9/5)  + 32
    print(f'{f:.0f}Fº')

def celsius():
    f = int(input('Digite em graus fahrenheit: '))
    c = (f - 32) * 5/9
    print(f'{c:.0f}Cº')

fahrenheit()
celsius()
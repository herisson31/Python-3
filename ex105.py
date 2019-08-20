'''Ex105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um
   dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
'''

def nota(*n, sit = False):

    '''
    --> Função que permite cadastrar varias notas
    :param n: cadastra as notas
    :param sit: verifica a situação de cada aluno.
    :return: returna o resultado de todos os dados
    '''
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    return r
# Programa Principal
resp = nota(8.8,10,10, sit=True)
print(resp)
#help(nota)
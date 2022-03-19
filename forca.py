# Jogo da forca

from random import choice
from string import ascii_lowercase as alfabeto

banco = ['casa','massa','tribo','vaga','plano','astronomia','bolo',]
    
def troca(n,f):
    if n == 1:
        f[2] = f[2][:-2] + 'o' + f[2][-1:]
    if n == 2:
        f[3] = f[3][:-1] + '\\'
    if n == 3:
        f[3] = f[3][:-2] + '|' + f[3][-1]
    if n == 4:
        f[3] = f[3][:-3] + '/' + f[3][-2:]
    if n == 5:
        f[4] = f[4][:-1] + '\\'
    if n == 6:
        f[4] = f[4][:-3] + '/' + f[4][-2::1]
    return f
    
def subs(p,h,l):
    new = []
    for i,j in zip(p,h):
        if l == i:
            new.append(i)
        else:
            new.append(j)
    new = ''.join(new)
    return new

def jogo():
    palavra = choice(banco)
    hidden = '_'*len(palavra)
    used = []
    chances = 0
    forca = [' ___  ',\
             '|   | ',\
             '|     ',\
             '|     ',\
             '|     ',\
             '|     ',\
             '------']
    try:
        while chances < 6:
            for linha in forca:
                print(linha)
            print('\nPalavra: {}\n'.format(hidden))
            print('Usadas: {}'.format(','.join(used)))
            letra = input('Informe uma letra: ')
            if letra in used:
                print('\nVoce ja usou essa letra!')
                continue
            elif (letra in alfabeto) and (letra in palavra):
                used.append(letra)
                hidden = subs(palavra,hidden,letra)
                if hidden == palavra:
                    print('\n---> {} <---'.format(palavra.upper()))
                    print('\nParabens!!! Voce conseguiu!')
                    break
                print('\nVoce encontrou uma letra!')
            elif (letra in alfabeto) and (letra not in palavra):
                used.append(letra)
                chances += 1
                forca = troca(chances,forca)
                if chances > 5:
                    for i in forca:
                        print(i)
                    print('\nGame over! Mais sorte da proxima vez...')
                    print('A palavra era {}.'.format(palavra))
                    break
                print('\nHmmm, essa letra nao pertence a palavra')
            else:
                print('\nPor favor, informe uma letra valida')
    except:
        print('Algo nao esta certo :/')

jogo()
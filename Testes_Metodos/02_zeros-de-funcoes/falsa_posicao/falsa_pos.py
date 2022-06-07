from cmath import sqrt
from random import randint
import numpy as np
from tqdm import tqdm
import math

# O método da falsa posição (também chamado de método regula falsi ou de interpolação linear) é um método de confinamento usado para se obter a solução de uma equação na forma f(x) = 0 quando se sabe que, dentro de um dado intervalo [a, b], f(x) é contínua e a equação possui uma solução.
# A solução tem início com a obtenção de um intervalo [a 1, b 1] que confine a solução.
# Os valores da função nos pontos finais são f(a1 ) e f(b1 )
# Os pontos finais são então conectados por uma linha reta, e a primeira estimativa da solução numérica, xNS1 , é o ponto onde a linha reta cruza o eixo x.
# Isso contrasta com o método da bisseção, onde o ponto central do intervalo foi escolhido como solução.
# Para a segunda iteração, define-se um novo intervalo [a 2 , b2 ].
# Esse novo intervalo corresponde à subseção do primeiro intervalo que contém a solução.
# Ele é – [a1  , xNS1 ], a1  atribuído a a2  e xNS1 a b2  ou – [xNS1 , b1  ], xNS1 atribuído a a 2 e b1  a b2
# Os pontos finais do segundo intervalo são em seguida conectados por uma linha reta, e o ponto onde essa nova reta cruza o eixo x se torna a segunda solução estimada, xNS2
# Para a terceira iteração, um novo subintervalo [a 3 , b 3] é selecionado, e as iterações continuam da mesma forma até que a solução numérica seja considerada suficientemente precisa.
# Para um dado intervalo [a, b], a equação da linha reta que conecta os pontos (b, f(b)) e (a, f(a)) é dada por:
#   y = (x-b)(f(a)-f(b))/(b-a)+f(b)
# O ponto xNS onde a reta cruza o eixo x é determinado pela substituição de y = 0 na equação e a solução dessa equação para x:
#   Xns = (af(b) - bf(a))/(f(b)-f(a))

## metodo
# 1. Escolha o primeiro intervalo encontrando os pontos a e b entre os quais existe uma solução Isso significa que f(a) e f(b) têm sinais diferentes, de forma que f(a)*f(b) < 0 Os pontos podem ser determinados a partir de um gráfico de f(x) versus x
# 2. Calcule a primeira estimativa da solução numérica x NS1 usando 
#   Xns = (af(b) - bf(a))/(f(b)-f(a))
# 3. Determine se a solução exata está entre a e xNS1 , ou entre xNS1 e b. Isso é feito com a verificação do sinal do produto f(a) * f(xNS1 ):
#   Se f(a) * f(xNS1 ) < 0, a solução exata está entre a e xNS1
#   Se f(a) * f(xNS1 ) > 0, a solução exata está entre xNS1 e b
# 4. Selecione o subintervalo que contém a solução (a até xNS1 , ou xNS1 até b) como o novo intervalo [a, b] e volte para o passo 2
# Critério de parada:
# |xn  – x(n-1)| <= erro , ou | f(xn ) | <= erro
# Os passos 2 a 4 são repetidos até que uma tolerância especificada ou um determinado limite de erro sejam atingidos.


def _calc_fx(a,b,c,d,x):
    return a*(x**3) + b*(x**2) + c*x +d

def _get_initial_guess(a,b,c,d):
    x1 = randint(-100,100)
    x2 = randint(-100,100)
    fx = _calc_fx(a,b,c,d,x1)*_calc_fx(a,b,c,d,x2)
    while(fx>0):
        x1 = randint(-100,100)
        x2 = randint(-100,100)
        fx = _calc_fx(a,b,c,d,x1)*_calc_fx(a,b,c,d,x2)
    if(x1<x2):
        return x1,x2
    else:
        return x2,x1

def find_root_regula_falsi(a,b,c,d,ini_guess,eps):
    print(ini_guess)
    x1,x2 = ini_guess
    xn_ant = x1
    # |xn  – x(n-1)| <= erro , ou | f(xn ) | <= erro
    
    print('    N° de iteração     |     x     |        Tolerância alcançada        |')
    its = 0
    while(True):
        #   Xns = (af(b) - bf(a))/(f(b)-f(a))
        xns = (x1*_calc_fx(a,b,c,d,x2)-x2*_calc_fx(a,b,c,d,x1))/(_calc_fx(a,b,c,d,x2)-_calc_fx(a,b,c,d,x1))
        if(_calc_fx(a,b,c,d,x1)*_calc_fx(a,b,c,d,xns)<0):
            x2 = xns
        else:
            x1 = xns
        
        err = f'{abs((xns - xn_ant)):.4f} ou {abs((_calc_fx(a,b,c,d,xns))):.4f}'
        its+=1
        out = "   "
        n_i = len(str(its))
        sp_c = 20 - n_i
        out = out + str(its)
        for i in range(sp_c):
            out = out + " "
        out = out + f'|  {xns:.4f}   |'
        n_t = len((err))
        sp_c = 12
        out = out + "        " + f'{err}'
        for i in range(sp_c):
            out = out + " "
        out = out+"|"
        print(out)
        if(abs((xns - xn_ant))<= eps or abs((_calc_fx(a,b,c,d,xns)))<=eps):
            
            xn_ant = xns
            break
        xn_ant = xns
        
        
    
    print(f'\n\nNúmero de iterações efetuadas: {its}')
    print(f'Intervalo considerado: [{ini_guess}]')
    print(f'Resultado final x`: {xn_ant:.4f}')
    print(f'f(x`): {_calc_fx(a,b,c,d,xn_ant):.4f}')
    return xn_ant
if __name__ == "__main__":
    print("Digite os parametros da equação a ser analisada no molde ax3 + bx2 + cx + d")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    d = float(input("d = "))
    err = float(input("erro maximo = "))
    is_guess = str(input("Deseja fornecer os valores iniciais? s/n ")).lower()
    ## a partir de 3o grau n funciona mais esse chute automatizado
    if(is_guess == "n"):
        x1,x2 = _get_initial_guess(a,b,c,d)
    else:
        x1 = float(input("x1 = "))
        x2 = float(input("x2 = "))
    root = find_root_regula_falsi(a,b,c,d,(x1,x2),err)

# Exemplo 3:
# Calcular a raiz positiva da equação f(x) = x3 –9*x + 3, com ε <= 0,001
# Exemplo 4:
# Calcular a raiz positiva da equação f(x) = x4 – 26*x2 + 24*x + 21, com ε <= 0,01
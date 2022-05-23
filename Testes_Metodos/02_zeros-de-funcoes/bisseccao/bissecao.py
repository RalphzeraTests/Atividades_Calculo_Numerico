from random import randint
import re
import numpy as np
from tqdm import tqdm

# O método da bisseção é um método de confinamento usado para se obter a solução de uma equação na forma f(x) = 0 quando se sabe que dentro de um dado intervalo [a, b]:
# – f(x) é contínua
# – a equação possui uma solução
# Quando esse é o caso, f(x) tem sinais opostos nos pontos finais do intervalo
# Se f(x) é contínua e tem uma solução entre os pontos x = a e x = b, então ou f(a) > 0 e f(b) < 0 ou f(a) < 0 e f(b) > 0
# Em outras palavras, se há uma solução entre x = a e x = b, então f(a) f(b) < 0
# Solução de f(x) = 0 entre x = a e x = b
# O processo de solução começa com a determinação dos pontos a e b que definem um intervalo onde existe uma solução.
# Tal intervalo é encontrado ou com o traçado de um gráfico de f(x) ou com o exame da função buscando uma mudança de sinal.
# O ponto central do intervalo, x NS1 , é então tomado como sendo a primeira estimativa da solução numérica.
# A solução exata está contida ou na seção entre a e xNS1 ou na seção entre os pontos xNS1 e b
# Se a solução numérica não for suficientemente precisa, define-se um novo intervalo que contenha a solução exata, e seu ponto central é escolhido como a nova (segunda) estimativa da solução numérica.
# O processo continua até que a solução numérica seja suficientemente precisa de acordo com o critério selecionado.



def _calc_fx(a,b,c,x):
    return a*x*x + b*x + c

def _get_initial_guess(a,b,c):
    x1 = randint(-100,100)
    x2 = randint(-100,100)
    fx = _calc_fx(a,b,c,x1)*_calc_fx(a,b,c,x2)
    while(fx>0):
        x1 = randint(-100,100)
        x2 = randint(-100,100)
        fx = _calc_fx(a,b,c,x1)*_calc_fx(a,b,c,x2)
        
    
    if(x1<x2):
        return x1,x2
    else:
        return x2,x1
# Entradas a,b,c são definidas pela equação:
# a*x^2 + b*x + c
def find_root_bissec(a,b,c,ini_guess,err):
    x1,x2 = ini_guess
    print(x1,x2)
    eps = (x2-x1)/2
    while(eps>err):
        x_ns1 =(x1+x2)/2
        if(_calc_fx(a,b,c,x1)*_calc_fx(a,b,c,x_ns1)<0):
            x2 = x_ns1
        else:
            x1 = x_ns1
        eps = (x2-x1)/2
    
    x_ns1 =(x1+x2)/2
    return x_ns1

if __name__ =="__main__":
    print("Digite os parametros da equação a ser analisada no molde ax2 + bx + x")
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    err = float(input("erro maximo = "))
    is_guess = str(input("Deseja fornecer os valores iniciais? s/n ")).lower()
    if(is_guess == "n"):
        x1,x2 = _get_initial_guess(1,0,-3)
    else:
        x1 = float(input("x1 = "))
        x2 = float(input("x2 = "))
    x_r = find_root_bissec(a,b,c,(x1,x2),err)
    print(f'Raiz aproximada: {x_r}')
# Exemplo 1:
# Calcular a raiz positiva da equação f(x) = x2 – 3, com ε <= 0,01
#       1.73638916015625
# ● Exemplo 2:
# Calcular a raiz da equação f(x) = x3 – 10, com ε <= 0,05
#       3.203125
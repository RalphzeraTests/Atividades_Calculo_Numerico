# E um caso particular do método do Ponto Fixo. ´
# Ideia: construir φ(x) que satisfaça as condições do Teorema do Ponto Fixo.
# Linearizar: substituir f(x) pela reta tangente.
# Vamos impor que φ'(x∗) = 0. Como φ'(x) deve ser contínua, existe I tal que k = max_x∈I |φ'(x)| < 1.
# De forma geral, x = φ(x) equivalente a f(x) = 0 é dada por:
# f(x) = 0 ⇒ A(x)f(x) = x − x ⇒ x = x + A(x)f(x) = φ(x), sendo A(x) contínua e A(x∗) != 0.
# Vamos determinar A(x) de forma que φ'(x∗) = 0
# Temos que:
# φ'(x) = 1 + A(x)f'(x) + A'(x)f(x)
# Para x = x*
# φ'(x∗) = 1 + A(x∗)f'(x∗) + A'(x∗)f(x∗) = 0,
# j´a que queremos φ'(x∗) = 0 e supondo f'(x∗) != 0. Assim,
# φ'(x∗) = 1 + A(x∗)f'(x∗) = 0 ⇒ A(x∗) = − 1/f'(x∗)
# Portanto escolhemos,
# A(x) = − 1/f'(x)
# A função de iteração do método de Newton é
# φ(x) = x − f(x)/f'(x) ⇒ x_n+1 = x_n − f(x_n)/f'(x_n) , para i = 0, 1, ...

# O método de Newton converge mais rápido que o método do Ponto Fixo.
# Pode-se mostrar que a convergência do método de Newton é quadrática se f'(x∗) != 0 e linear, caso contrário.
# A convergência é linear quando |x_n − x∗| ≤ M|x_n−1 − x∗|
# A convergência é quadrática quando |x_n − x∗| ≤ M|x_n−1 − x∗|^2.


# Adicione no return o calculo da função que deseja ser calculada a raiz
# aqui nõ vai ser passado como parametro os coeficientes pois será definida uma finção para a derivada também, desta forma fica possivel equações não lineares
import math
import sndhdr


def f(x):
    return (x**3 - x -1)

def df(x):
    return 3*(x**2) - 1


def get_root_newton(ini_pos,eps):
    x1,x2 = ini_pos
    its = 0
    xn = x1
    
    print('    N° de iteração     |       x       |   Tolerância alcançada   |')
    while(True):
        xn1 = xn -f(xn)/df(xn)
        err = abs(f(xn1))
        its+=1
        out = "   "
        n_i = len(str(its))
        sp_c = 20 - n_i
        out = out + str(its)
        for i in range(sp_c):
            out = out + " "

        s_xn = f'{xn:.4f}'
        sp_c = 12 - len(s_xn)
        out = out + "|   " + s_xn
        for i in range(sp_c):
            out = out + " "
        s_err = f'{err:.4f}'
        n_t = len((s_err))
        sp_c = 18 - n_t
        out = out + "|        " + s_err
        for i in range(sp_c):
            out = out + " "
        out = out+"|"
        print(out)
        if(err<eps):
            break
        xn = xn1
    


    
    print(f'\n\nf`(x): 3x^2 - 1')
    print(f'f``(x): 6x')
    print(f'Número de iterações efetuadas: {its}')
    print(f'Valor Inicial: {ini_pos[0]}')
    print(f'Resultado final x`: {xn:.4f}')
    print(f'f(x`): {f(xn):.4f}')
    return xn

if __name__ == "__main__":
    get_root_newton((-5,5),0.001)



# 1. Dada a fun¸c˜ao f(x) = x^2 − 2.
# (a) Determine um intervalo I = [a, b] e uma condição x_0 != α de modo que a sequência gerada pelo método de Newton convirja para a raiz positiva.
# (b) Faça as iterações, verificando se é possível utilizar a precisão pré-fixada de δ = 0.001.
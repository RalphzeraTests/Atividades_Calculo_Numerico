import numpy as np
import math

# Também pode ser chamado de aproximações sucessivas
# A sequência de aproximações da raiz x ∗ é obtida por meio de uma fórmula de recorrência:
# x_n = φ(x_n−1), n = 1, 2, . . .
# x_0 é uma aproximação (“chute”) inicial.
# A função φ(x) é uma função que tem x∗ como ponto fixo, ou seja, φ(x∗) = x∗.
# Como obter φ(x)?
# A partir da expressão f(x) = 0 escrevemos x = φ(x).
# Exemplo: f(x) = x^2 + 0.96x − 2.08 possui as raízes x1 = 1.04 e x2 = −2.
# De fato, f(x) troca de sinal, f(0) = −2.08 e f(2) = 3.84. Além disso, f'(x) > 0, ∀x ∈ [0, 2], ou seja, f(x) é crescente em [0, 2]. Portanto, existe uma única raiz no intervalo [0, 2]. Vamos considerar x_0 = 1.5.
# Fazendo x^2 + 0.96x − 2.08 = 0 podemos obter x = (2.08 − x^2)/ 0.96
# x^2 + 0.96x − 2.08 = 0 ⇒ φ(x) = x

# Algumas funções φ forneceram sequências convergentes. Outras não.
# Como saber se φ fornece uma sequência de aproximações convergente?

# Teorema:
# Seja x∗ uma raiz de uma função f(x), isolada em um intervalo I e φ(x) uma função tal que x∗ = φ(x∗). Se: 
#   1. φ e φ' são contínuas em I, 
#   2. k = max_x∈I |φ' (x)| < 1, 
#   3. x_0 ∈ I e x_n = φ(x_n−1) ∈ I, n = 1, 2, . . .; 
# então a sequência x_n converge para x∗ .


# isso aqui envolve derivada... as nem fodendo que tem como fazer no pc isso bixo kkkk

# Coloque no retorno o calculo da função a ser aproximada
def calc_func(x):
    return 2*x * math.cos(x)

def get_root_fix_point(ini_pos,eps):
    return

if __name__ == "__main__":
    get_root_fix_point((0,1),0.001)



# Determine uma aproximação para a raiz da função f(x) = 2x − cos(x), usando o método do ponto fixo.

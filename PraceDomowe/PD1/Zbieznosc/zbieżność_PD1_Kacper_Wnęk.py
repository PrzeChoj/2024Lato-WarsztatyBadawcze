import numpy as np
import matplotlib.pyplot as plt

# Funkcja obliczająca ciąg Qn dla danej wartości początkowej Q1, ciągu alpha oraz ciągu R
def calculate_Qn(Q1, alpha, R):
    Qn = np.zeros_like(R)
    Qn[0] = Q1
    for i in range(1, len(R)):
        Qn[i] = Qn[i - 1] + alpha[i - 1] * (R[i - 1] - Qn[i - 1])
    return Qn

# Generowanie ciągu R z rozkładu normalnego
R = np.random.normal(size=10000)

# Wartość początkowa Q1
Q1_values = [0, 10]

# Ciągi alpha dla różnych przypadków, można na 1 plocie, ale nic nie widać, więc warto zakomentować :))
alphas = {
    'a': lambda n: 1 / np.arange(1, n + 1),
    # 'f': lambda n: 1 / np.arange(2,n+2)*np.log(np.arange(2, n + 2)),
    # 'g': lambda n: 1 / (np.arange(1,n+1))^(2/3)
    # 'b': lambda n: 1 / np.square(np.arange(1, n + 1)),
    # 'c': lambda n: 1 / np.sqrt(np.arange(1, n + 1)),
    # 'd': lambda n: np.ones(n),
    # 'e': lambda n: 1 / np.log(np.arange(2, n + 2))  
}

# Sprawdzenie zbieżności lub rozbieżności dla każdego ciągu alpha
for Q1 in Q1_values:
    print(f'Wartość początkowa Q1: {Q1}')
    for key, alpha_func in alphas.items():
        alpha = alpha_func(len(R))
        
        Qn = calculate_Qn(Q1, alpha, R)
    
    
        plt.plot(Qn, label=f'Alpha ({key})')
    

    plt.axhline(np.mean(R), color='red', linestyle='--', label='E[R1]')
    plt.xlabel('n')
    plt.ylabel('Wartość Qn')
    plt.title(f'Zbieżność ciągu Qn dla Q1 = {Q1}')
    plt.legend()
    plt.ylim(-0.6, 0.6)
    plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Set the expected value E[R_1] to 0
E_R_1 = 0
std_dev = 1

# Create a range of n values
n = np.arange(2, 1000)
print(n)

# Define the step size sequences
alpha_n1 = 1 / n
alpha_n2 = 1 / (n * np.log(n))
alpha_n3 = 1 / n**(2/3)
print(alpha_n2)

# Initialize the Q_n arrays to store the estimate values
Q_n1 = np.zeros_like(n, dtype=float)
Q_n2 = np.zeros_like(n, dtype=float)
Q_n3 = np.zeros_like(n, dtype=float)

# Simulate R_n as random variables from a normal distribution centered around E[R_1]
np.random.seed(4)  # Seed for reproducibility
R_n = np.random.normal(E_R_1, std_dev, size=n.shape)

# Update the Q_n estimates using the step size sequences
for i in range(1, len(n)):
    Q_n1[i] = Q_n1[i-1] + alpha_n1[i-1] * (R_n[i-1] - Q_n1[i-1])
    Q_n2[i] = Q_n2[i-1] + alpha_n2[i-1] * (R_n[i-1] - Q_n2[i-1])
    Q_n3[i] = Q_n3[i-1] + alpha_n3[i-1] * (R_n[i-1] - Q_n3[i-1])

# Plot the convergence of the Q_n estimates to E[R_1] for each step size sequence
plt.figure(figsize=(14, 6))

# Plot for alpha_n = 1/n
plt.subplot(1, 3, 1)
plt.plot(n, Q_n1, label=r'$Q_n$ with $\alpha_n = \frac{1}{n}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Convergence of $Q_n$ with $\alpha_n = \frac{1}{n}$')
plt.ylim(-1,1)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

# Plot for alpha_n = 1/(nlogn)
plt.subplot(1, 3, 2)
plt.plot(n, Q_n2, label=r'$Q_n$ with $\alpha_n = \frac{1}{n\log(n)}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Convergence of $Q_n$ with $\alpha_n = \frac{1}{n\log(n)}$')
plt.ylim(-1,1)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

# Plot for alpha_n = 1/n^(2/3)
plt.subplot(1, 3, 3)
plt.plot(n, Q_n3, label=r'$Q_n$ with $\alpha_n = \frac{1}{n^{2/3}}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Convergence of $Q_n$ with $\alpha_n = \frac{1}{n^{2/3}}$')
plt.ylim(-1,1)
plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import numpy as np

# Set to true if you want to set Q[0] = 10
set_Q_0_to_10 = True

# Set the expected value E[R_1] to 0
E_R_1 = 0
std_dev = 1

# Create a range of n values
n = np.arange(2, 100000)

# Define the step size sequences
alpha_n1 = 1 / n
alpha_n2 = 1 / (n * np.log(n))
alpha_n3 = 1 / n ** (2 / 3)
alpha_n4 = 1 / n ** 2
alpha_n5 = 1 / n ** (1 / 2)
alpha_n6 = np.full(100000, 0.05)
alpha_n7 = np.full(100000, 0.2)
alpha_n8 = 1 / n ** 3

# Initialize the Q_n arrays to store the estimate values
Q_n1 = np.zeros_like(n, dtype=float)
Q_n2 = np.zeros_like(n, dtype=float)
Q_n3 = np.zeros_like(n, dtype=float)
Q_n4 = np.zeros_like(n, dtype=float)
Q_n5 = np.zeros_like(n, dtype=float)
Q_n6 = np.zeros_like(n, dtype=float)
Q_n7 = np.zeros_like(n, dtype=float)
Q_n8 = np.zeros_like(n, dtype=float)

if set_Q_0_to_10:
    # Modify the first element of each array
    Q_n1[0] = 10
    Q_n2[0] = 10
    Q_n3[0] = 10
    Q_n4[0] = 10
    Q_n5[0] = 10
    Q_n6[0] = 10
    Q_n7[0] = 10
    Q_n8[0] = 10

# Simulate R_n as random variables from a normal distribution centered around E[R_1]
np.random.seed(4)  # Seed for reproducibility
R_n = np.random.normal(E_R_1, std_dev, size=n.shape)

# Update the Q_n estimates using the step size sequences
for i in range(1, len(n)):
    Q_n1[i] = Q_n1[i - 1] + alpha_n1[i - 1] * (R_n[i - 1] - Q_n1[i - 1])
    Q_n2[i] = Q_n2[i - 1] + alpha_n2[i - 1] * (R_n[i - 1] - Q_n2[i - 1])
    Q_n3[i] = Q_n3[i - 1] + alpha_n3[i - 1] * (R_n[i - 1] - Q_n3[i - 1])
    Q_n4[i] = Q_n4[i - 1] + alpha_n4[i - 1] * (R_n[i - 1] - Q_n4[i - 1])
    Q_n5[i] = Q_n5[i - 1] + alpha_n5[i - 1] * (R_n[i - 1] - Q_n5[i - 1])
    Q_n6[i] = Q_n6[i - 1] + alpha_n6[i - 1] * (R_n[i - 1] - Q_n6[i - 1])
    Q_n7[i] = Q_n7[i - 1] + alpha_n7[i - 1] * (R_n[i - 1] - Q_n7[i - 1])
    Q_n8[i] = Q_n8[i - 1] + alpha_n8[i - 1] * (R_n[i - 1] - Q_n8[i - 1])

y_lim = (-10, 10) if set_Q_0_to_10 else (-1, 1)

# Plot the convergence of the Q_n estimates to E[R_1] for each step size sequence
plt.figure(figsize=(14, 6))

# Plot for alpha_n = 1/n
plt.subplot(1, 3, 1)
plt.plot(n, Q_n1, label=r'$Q_n$ with $\alpha_n = \frac{1}{n}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Convergence of $Q_n$ with $\alpha_n = \frac{1}{n}$')
plt.ylim(y_lim)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

# Plot for alpha_n = 1/(nlogn)
plt.subplot(1, 3, 2)
plt.plot(n, Q_n2, label=r'$Q_n$ with $\alpha_n = \frac{1}{n\log(n)}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Convergence of $Q_n$ with $\alpha_n = \frac{1}{n\log(n)}$')
plt.ylim(y_lim)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

# Plot for alpha_n = 1/n^(2/3)
plt.subplot(1, 3, 3)
plt.plot(n, Q_n3, label=r'$Q_n$ with $\alpha_n = \frac{1}{n^{2/3}}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Convergence of $Q_n$ with $\alpha_n = \frac{1}{n^{2/3}}$')
plt.ylim(y_lim)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

plt.tight_layout()
plt.show()

# Plot the divergence of the Q_n estimates to E[R_1] for each step size sequence
# Important Note: For some alpha_n for certain selection of Q[0] Q_n will not appear to be divergent, set
# Q[0] to the other value, and you should see the divergence
plt.figure(figsize=(14, 6))

# Plot for alpha_n = 1/n^2
plt.subplot(1, 3, 1)
plt.plot(n, Q_n4, label=r'$Q_n$ with $\alpha_n = \frac{1}{n^2}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Divergence of $Q_n$ with $\alpha_n = \frac{1}{n^2}$')
plt.ylim(y_lim)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

# Plot for alpha_n = 1/sqrt(n)
plt.subplot(1, 3, 2)
plt.plot(n, Q_n5, label=r'$Q_n$ with $\alpha_n = \frac{1}{sqrt(n)}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Divergence of $Q_n$ with $\alpha_n = \frac{1}{sqrt(n)}$')
plt.ylim(y_lim)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

# Plot for alpha_n = 0.05
plt.subplot(1, 3, 3)
plt.plot(n, Q_n6, label=r'$Q_n$ with $\alpha_n = 0.05$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Divergence of $Q_n$ with $\alpha_n = 0.05$')
plt.ylim(y_lim)
plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 6))

# Plot for alpha_n = 0.02
plt.subplot(1, 2, 1)
plt.plot(n, Q_n7, label=r'$Q_n$ with $\alpha_n = 0.02$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Divergence of $Q_n$ with $\alpha_n = 0.02$')
plt.ylim(y_lim)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

# Plot for alpha_n = 1/n^3
plt.subplot(1, 2, 2)
plt.plot(n, Q_n8, label=r'$Q_n$ with $\alpha_n = \frac{1}{n^{3}}$')
plt.hlines(E_R_1, xmin=n[0], xmax=n[-1], colors='r', linestyles='dashed', label=r'$E[R_1]$')
plt.title(r'Divergence of $Q_n$ with $\alpha_n = \frac{1}{n^{3}}$')
plt.ylim(y_lim)

plt.xlabel('n')
plt.ylabel(r'$Q_n$')
plt.legend()

plt.tight_layout()
plt.show()

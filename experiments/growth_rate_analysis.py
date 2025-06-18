import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import numpy as np
from constrained_sequences import ConstrainedSequenceEnumerator
import matplotlib.pyplot as plt

def empirical_growth_rate(K=2, U=10, R=3, n_max=20):
    values = []
    ns = range(5, n_max+1)
    for n in ns:
        enumerator = ConstrainedSequenceEnumerator(n, K, U, R)
        count, _ = enumerator.compute()
        values.append(count)
        print(f"n={n}: f({n},{K},{U},{R})={count}")
    alphas = [values[i]**(1.0/(ns[i])) for i in range(len(values))]
    plt.plot(list(ns), alphas, marker='o')
    plt.xlabel('n')
    plt.ylabel('Empirical growth rate alpha')
    plt.title(f'Empirical growth rate for (K={K}, U={U}, R={R})')
    plt.grid()
    plt.savefig('growth_rate_plot.png')
    plt.show()

if __name__ == '__main__':
    empirical_growth_rate()

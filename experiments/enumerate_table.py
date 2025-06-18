import csv
from src.constrained_sequences import ConstrainedSequenceEnumerator

def main():
    table = []
    # Example: binary, ternary, quaternary alphabets
    for K in [2, 3, 4]:
        for n in range(1, 11):
            U = min(n, 3)
            R = 2
            enumerator = ConstrainedSequenceEnumerator(n, K, U, R)
            count, _ = enumerator.compute()
            table.append({'n': n, 'K': K, 'U': U, 'R': R, 'count': count})
            print(f"K={K}, n={n}, U={U}, R={R}: {count}")
    with open('enumeration_table.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=table[0].keys())
        writer.writeheader()
        writer.writerows(table)

if __name__ == '__main__':
    main()

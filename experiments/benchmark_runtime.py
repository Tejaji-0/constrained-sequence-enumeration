import time
import tracemalloc
import csv
from src.constrained_sequences import ConstrainedSequenceEnumerator

PARAMS = [
    # (n, K, U, R)
    (5, 2, 3, 2),
    (8, 2, 4, 2),
    (10, 3, 4, 2),
    (12, 2, 6, 3),
    (15, 2, 8, 3),
    (18, 3, 6, 2),
    (20, 2, 10, 4)
]

def benchmark():
    rows = []
    for n, K, U, R in PARAMS:
        tracemalloc.start()
        start = time.time()
        enumerator = ConstrainedSequenceEnumerator(n, K, U, R)
        count, states = enumerator.compute()
        end = time.time()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        rows.append({
            'n': n, 'K': K, 'U': U, 'R': R,
            'count': count,
            'states_explored': states,
            'time_ms': int(1000 * (end - start)),
            'memory_MB': int(peak / (1024 * 1024))
        })
        print(f"n={n}, K={K}, U={U}, R={R}: {count} sequences, {rows[-1]['time_ms']} ms, {rows[-1]['memory_MB']} MB")
    # Write CSV
    with open('runtime_results.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

if __name__ == '__main__':
    benchmark()

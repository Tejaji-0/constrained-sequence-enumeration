import functools

class ConstrainedSequenceEnumerator:
    def __init__(self, n, K, U, R):
        self.n, self.K, self.U, self.R = n, K, U, R
        self.states_explored = 0

    @functools.lru_cache(maxsize=None)
    def count_sequences(self, pos=0, counts=None, last=-1, run=0):
        if counts is None:
            counts = tuple([0] * self.K)
        self.states_explored += 1
        if pos == self.n:
            return 1
        # Early pruning
        remaining = self.n - pos
        max_possible = sum(min(c + remaining, self.U) for c in counts)
        if max_possible < remaining:
            return 0
        total = 0
        for symbol in range(self.K):
            if counts[symbol] < self.U:
                new_counts = list(counts)
                new_counts[symbol] += 1
                new_counts = tuple(new_counts)
                if symbol == last:
                    if run + 1 <= self.R:
                        total += self.count_sequences(
                            pos + 1, new_counts, symbol, run + 1
                        )
                else:
                    total += self.count_sequences(
                        pos + 1, new_counts, symbol, 1
                    )
        return total

    def compute(self):
        result = self.count_sequences()
        return result, self.states_explored
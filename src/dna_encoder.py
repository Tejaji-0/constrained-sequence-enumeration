from constrained_sequences import ConstrainedSequenceEnumerator
import numpy as np

class DNAConstrainedEncoder:
    def __init__(self, max_length=150, max_freq=45, max_run=3):
        self.n = max_length
        self.K = 4  # A, C, G, T
        self.U = max_freq
        self.R = max_run
        self.alphabet = ['A', 'C', 'G', 'T']
        self.enumerator = ConstrainedSequenceEnumerator(self.n, self.K, self.U, self.R)
        self.total_sequences, _ = self.enumerator.compute()
        self.code_rate = np.log2(self.total_sequences) / (self.n * 2)

    def encode_data(self, data_bits):
        data_int = int(data_bits, 2)
        if data_int >= self.total_sequences:
            raise ValueError("Data exceeds code capacity")
        return self.index_to_sequence(data_int)

    def index_to_sequence(self, index):
        # Greedy lexicographic unranking (for demonstration; see paper for full details)
        sequence = []
        remaining_index = index
        counts = [0] * self.K
        last = -1
        run = 0
        for pos in range(self.n):
            for symbol in range(self.K):
                if counts[symbol] < self.U:
                    if symbol == last:
                        if run + 1 > self.R:
                            continue
                        run_next = run + 1
                    else:
                        run_next = 1
                    next_counts = list(counts)
                    next_counts[symbol] += 1
                    # Count how many sequences with this prefix
                    seq_enum = ConstrainedSequenceEnumerator(self.n, self.K, self.U, self.R)
                    left = seq_enum.count_sequences(
                        pos + 1, tuple(next_counts), symbol, run_next)
                    if remaining_index < left:
                        sequence.append(symbol)
                        counts[symbol] += 1
                        last = symbol
                        run = run_next
                        break
                    remaining_index -= left
        return ''.join(self.alphabet[s] for s in sequence)
# Enumeration of K-ary Sequences with Bounded Symbol Frequency and Run-Length Constraints

This repository contains the source code, data, and documentation for the paper:

**"Enumeration of K-ary Sequences with Bounded Symbol Frequency and Run-Length Constraints"**  
*Sri Narayana Tejaji Panda, St Paul's English School, Bangalore, India*

## Overview

We introduce and analyze the enumeration function $f(n, K, U, R)$, which counts sequences of length $n$ over a $K$-symbol alphabet subject to dual constraints:

- **Frequency constraint**: Each symbol appears at most $U$ times globally.
- **Run-length constraint**: No symbol appears more than $R$ times consecutively.

The project unifies frequency-bounded and run-length limited sequence analysis, presenting efficient algorithms, theoretical bounds, transfer matrix methods, and quantified applications in DNA storage, flash memory, and communication theory.

## Features

- **Dynamic Programming Algorithms**: Efficient computation for $n \leq 20$ (larger via approximation).
- **Asymptotic Analysis**: Growth rates $f(n,K,U,R) \sim c \cdot \alpha^n$ with explicit spectral methods.
- **Transfer Matrix Methods**: Connections to symbolic dynamics and spectral graph theory.
- **Quantified Applications**: 
  - DNA storage: up to 15% error reduction.
  - Flash memory: up to 23% lifespan extension.
- **Approximation Methods**: Monte Carlo, inclusion-exclusion, and reduced transfer matrix techniques.

## Getting Started

### Prerequisites

- Python 3.8+
- NumPy
- (Optional) Numba for JIT acceleration
- Jupyter for running notebooks

### Repository Structure

- `src/constrained_sequences.py` &rarr; Core algorithms and classes.
- `src/dna_encoder.py` &rarr; Application code for DNA storage.
- `src/flash_coding.py` &rarr; Application code for flash memory.
- `experiments/` &rarr; Scripts, datasets, and performance benchmarks.
- `notebooks/` &rarr; Jupyter notebooks for reproducing results and figures.
- `LICENSE` &rarr; CC0 1.0 Universal License.
- `README.md` &rarr; This file.

## Usage

### Counting Constrained Sequences

```python
from src.constrained_sequences import ConstrainedSequenceEnumerator

n, K, U, R = 10, 3, 4, 2
enumerator = ConstrainedSequenceEnumerator(n, K, U, R)
count, states = enumerator.compute()
print(f"f({n},{K},{U},{R}) = {count} (explored {states} states)")
```

### DNA Storage Encoder

```python
from src.dna_encoder import DNAConstrainedEncoder

encoder = DNAConstrainedEncoder(max_length=150, max_freq=45, max_run=3)
dna_seq = encoder.encode_data('1100101010...')  # use your binary string
print("Constrained DNA sequence:", dna_seq)
```

### Flash Memory Coding

```python
from src.flash_coding import FlashMemoryConstrainedCoding

coder = FlashMemoryConstrainedCoding(page_size=2048, symbol_bits=8)
encoded = coder.encode_page(data_bytes)
print("Encoded page with constraints:", encoded)
```

## Reproducibility

- All tables and figures in the paper are reproducible using notebooks in `notebooks/`.
- Complete datasets and benchmarks are in `experiments/`.

## Citing

If you use this code or results in your work, please cite:

```
@article{panda2025enumeration,
  title={Enumeration of K-ary Sequences with Bounded Symbol Frequency and Run-Length Constraints},
  author={Panda, Sri Narayana Tejaji},
  year={2025},
  url={https://github.com/tejaj-kumar/constrained-sequence-enumeration}
}
```

## License

MIT License

## Contact

Sri Narayana Tejaji Panda  
psntejaji@gmail.com

---
**Project repository:** [https://github.com/Tejaj-0/constrained-sequence-enumeration](https://github.com/tejaj-kumar/constrained-sequence-enumeration)

from constrained_sequences import ConstrainedSequenceEnumerator

def main():
    n = int(input("Enter n (sequence length): "))
    K = int(input("Enter K (number of symbols): "))
    U = int(input("Enter U (max usage per symbol): "))
    R = int(input("Enter R (max run length): "))

    enumerator = ConstrainedSequenceEnumerator(n, K, U, R)
    count, states = enumerator.compute()
    print(f"Number of valid sequences: {count}")
    print(f"States explored: {states}")

if __name__ == "__main__":
    main()
def generate_fibonacci(n):
    if n <= 0:
        return "❌ Please enter a positive integer greater than 0."

    fib_sequence = []

    a, b = 0, 1

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    return fib_sequence

def main():
    try:
        terms = int(input("Enter the number of Fibonacci terms to generate: "))
        result = generate_fibonacci(terms)
        print("🌀 Fibonacci Sequence:", result)
    except ValueError:
        print("❌ Invalid input! Please enter an integer.")

main()

#Enter the number of Fibonacci terms to generate: 7
#🌀 Fibonacci Sequence: [0, 1, 1, 2, 3, 5, 8]


import sys

def factorize(num):
    for j in range(2, num // 2 + 1):
        if num % j == 0:
            return f"{num}={j}*{num // j}"

def main(filename):
    with open(filename, 'r') as file:
        num = [int(line.strip()) for line in file.readlines()]

    for num in num:
        result = factorize(num)
        print(result)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    filename = sys.argv[1]
    main(filename)

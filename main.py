from math import gcd as gcd
import matplotlib.pyplot as plt

def coprime(a, b):
    return gcd(a, b) == 1

def function(minP, maxP, n):
    return (n * minP) % maxP

def getCoprimes(min, max):
    i = j = min
    coprimes = []

    while i <= max:
        while j <= max:
            if coprime(i, j):
                coprimes.append([i, j])
            j += 1
        i += 1
        j = 0

    return coprimes

def generate_values(min, max, minN, maxN):
    coprimes = getCoprimes(min, max)
    n = minN
    output = []

    while n <= maxN:
        for item in coprimes:
            output.append([item[0], item[1], function(item[0], item[1], n)])
        n += 1

    unique_set = {tuple(item) for item in output}

    return sorted(list(item) for item in unique_set)

def plot(input, filename = "plot"):
    x = [item[0] for item in input]
    y = [item[1] for item in input]
    values = [item[2] for item in input]

    plt.scatter(x, y, c=values, cmap='viridis', s=100)

    plt.colorbar(label='Value')

    plt.xlabel('coprime 1')
    plt.ylabel('coprime 2')
    plt.title('Scatter plot of [coprime 1, coprime 2, value]')

    plt.savefig(filename + '.png')

    plt.show()

def main():
    min = int(input("Input min coprime value: "))
    max = int(input("Input max coprime value: "))
    minN = int(input("Input min n value: "))
    maxN = int(input("Input max n value: "))

    print("Generating coprimes...")

    coprimes = generate_values(min, max, minN, maxN)

    filename = f"coprimes-{min}-to-{max}_n-{minN}-to-{maxN}.png"

    with open(filename + '.csv', mode='w') as file:
        file.write("c1, c2, result\n")
        for sublist in coprimes:
            file.write(f"{sublist[0]}, {sublist[1]}, {sublist[2]}\n")
        file.close()

    print("Done!\nPlotting results...")

    plot(coprimes, filename)

    print("Done!")

if __name__ == '__main__':
    main()
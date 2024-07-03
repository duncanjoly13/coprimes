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
        j = 1

    return coprimes

def generate_values(min, max, minN, maxN):
    coprimes = getCoprimes(min, max)
    n = minN
    output = []

    while n <= maxN:
        for item in coprimes:
            output.append([item[0], item[1], function(item[0], item[1], n)])
        n += 1

    # TODO: make sure no results we want are deleted

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
    min = input("Input min coprime value: ")
    try:
        min = int(min)
    except ValueError:
        print("Invalid input!")
        return

    max = input("Input max coprime value: ")
    try:
        max = int(max)
    except ValueError:
        print("Invalid input!")
        return

    minN = input("Input min n value: ")
    try:
        minN = int(minN)
    except ValueError:
        print("Invalid input!")
        return

    maxN = input("Input max n value: ")
    try:
        maxN = int(maxN)
    except ValueError:
        print("Invalid input!")
        return

    print("\nGenerating coprimes...")

    coprimes = generate_values(min, max, minN, maxN)

    filename = f"coprimes-{min}-to-{max}_n-{minN}-to-{maxN}"

    with open(filename + '.csv', mode='w') as file:
        file.write(f"min: {min} \n")
        file.write(f"max: {max} \n")
        file.write(f"min n: {minN} \n")
        file.write(f"max n: {maxN} \n")
        file.write("c1, c2, result\n")
        for sublist in coprimes:
            file.write(f"{sublist[0]}, {sublist[1]}, {sublist[2]}\n")
        file.close()

    print("Done!\nPlotting results...")

    plot(coprimes, filename)

    print("Done!")

if __name__ == '__main__':
    main()
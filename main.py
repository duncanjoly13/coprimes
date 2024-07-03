from math import gcd as gcd
import matplotlib.pyplot as plt
import numpy as np

def coprime(a, b):
    return gcd(a, b) == 1


def function(minP, maxP, n):
    return (n * minP) % maxP


def getCoprimes(minP, maxP):
    i = j = minP
    coprimes = []

    while i <= maxP:
        while j <= maxP:
            if coprime(i, j):
                coprimes.append([min(i, j), max(i, j)])
                # TODO: add values here to reduce time complexity
            j += 1
        i += 1
        j = 2

    return np.unique(np.array([np.sort(sub) for sub in coprimes]), axis=0)


def generateResults(minP, maxP, minN, maxN):
    coprimes = getCoprimes(minP, maxP)
    output = []

    for pair in coprimes:
        n = minN
        while n <= maxN:
            output.append([pair[0], pair[1], function(pair[0], pair[1], n)])
            n += 1

    return sorted(list(set(map(lambda i: tuple(i), output))))

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
    minP = input("Input min coprime value: ")
    try:
        minP = int(minP)
    except ValueError:
        print("Invalid input!")
        return

    maxP = input("Input max coprime value: ")
    try:
        maxP = int(maxP)
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

    makePlot = input("Generate plot? (y/[n]): ")
    if makePlot.lower() == "y":
        makePlot = True
        print("Will generate plot")
    elif makePlot.lower() == "n":
        makePlot = False
        print("Will not generate plot")
    else:
        print("Invalid input!")
        return

    print("\nGenerating coprimes...")

    coprimes = generateResults(minP, maxP, minN, maxN)

    filename = f"coprimes-{minP}-to-{maxP}_n-{minN}-to-{maxN}"

    with open(filename + '.csv', mode='w') as file:
        file.write(f"min: {minP} \n")
        file.write(f"max: {maxP} \n")
        file.write(f"min n: {minN} \n")
        file.write(f"max n: {maxN} \n\n")
        file.write("c1, c2, result\n")
        for sublist in coprimes:
            file.write(f"{sublist[0]}, {sublist[1]}, {sublist[2]}\n")
        file.close()

    if makePlot:
        print("\nDone!\nPlotting results...")
        plot(coprimes, filename)
    else:
        print("\nDone!")


if __name__ == '__main__':
    main()
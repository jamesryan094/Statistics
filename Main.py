import math

def main():
    sample = []
    getSample(sample)
    average = getAverage(sample)
    median = getMedian(sample)
    sDeviation = stdDev(sample, average)
    print(sample)
    print(sorted(sample))
    print("Mean: ", average)
    print("Median: ", median)
    print("Standard Deviation: ", sDeviation)


def getSample(sample):
    print("Press 'Q' to quit")
    while True:
        unit = input("Enter value >>>")
        if unit == 'Q' or unit == 'q':
            return
        unit = float(unit)
        sample.append(unit)


def stdDev(sample, average):
    count = 0
    i = 0
    for unit in sample:
        count += (sample[i] - average)**2
        i += 1
    variance = count / len(sample)
    sigma = math.sqrt(variance)
    return sigma


def getAverage(sample):
    return sum(sample)/len(sample)

def getMedian(sample):
    ordered = sorted(sample)
    if len(sample)%2 == 0:
        median = (ordered[(len(ordered)//2)]+ ordered[((len(ordered)//2)+1)])/2
        return median
    return ordered[(len(ordered)//2)]

main()
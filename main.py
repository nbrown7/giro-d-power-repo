import csv
from node import Node
from dll import DoubleLinkedList

# function to compute power zones
def calculateZoneSeven(functionalpt):
    print("Zone 1: <" + str(round(functionalpt * 0.60)) + " watts")
    print("Zone 2: " + str(round(functionalpt * 0.55)) + ' watts - ' + str(round(functionalpt * 0.75)) + " watts")
    print("Zone 3: " + str(round(functionalpt * 0.75)) + ' watts - ' + str(round(functionalpt * 0.90)) + " watts")
    print("Zone 4: " + str(round(functionalpt * 0.90)) + ' watts - ' + str(round(functionalpt * 1.05)) + " watts")
    print("Zone 5: " + str(round(functionalpt * 1.05)) + ' watts - ' + str(round(functionalpt * 1.20)) + " watts")
    print("Zone 6: " + str(round(functionalpt * 1.20)) + ' watts - ' + str(round(functionalpt * 1.30)) + " watts")
    print("Zone 7: >" + str(round(functionalpt * 1.30)) + " watts")


# reading csv file
def calculateXMinPower(minutes):
    minutes_val = float(minutes)
    with open('Avant_race.CSV') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0  # counts the number of lines
        max_pow = 0  # variable to store highest x minute power
        pow_tot = 0  # variable to store total power
        list1 = DoubleLinkedList()

        for row in csv_reader:
            if line_count <= 2:
                pass
            elif (minutes_val * 60) + 3 > line_count:
                node = Node(row[10])
                list1.addToFront(node)
                if line_count == (minutes_val * 60) + 2:
                    max_pow = float(list1.averageList())
                pow_tot += int(row[10])
            else:
                node = Node(row[10])
                list1.addToFront(node)
                list1.removeFromBack()
                newAve = list1.averageList()
                if float(newAve) > max_pow:
                    max_pow = float(newAve)
                pow_tot += int(row[10])

            line_count += 1

        averagePow = 2 * pow_tot / (line_count - 2)
        print(f'Processed {line_count - 1} lines. Average power: {round(averagePow)}\n')
        print(f'Maximum {minutes_val} minute power: {round(max_pow * 2)}\n')

    if minutes_val == 20:
        ftp = max_pow * 2 * 0.95
        print(f'functional threshold power: {round(ftp)}\n')
        calculateZoneSeven(ftp)


if __name__ == '__main__':
    numMin = input("enter the number of minutes to max out on <= 60\n")
    calculateXMinPower(numMin)

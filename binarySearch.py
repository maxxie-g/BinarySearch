# TODO: Finish implementing Error / out of bounds cases handling

# Function for opening and sorting lists

def fileToList():
    f = open("/Users/maximiliangrimmsmann/PythonProjects/BinarySearch/numSetRaw.txt","r")
    tempList = []

    tempList = f.read().split(" ")
    numList = [int(i) for i in tempList]

    f.close()
    return numList

# Iterative implementation of binary search

def iterBinSearch(a_list, item):
    # Performs iterative binary search to find the position of an integer in a given sorted list
    # a_list: sorted list of integers
    # item: integer that is being searched for
    first = 0
    last = len(a_list)

    while first <= last:
        i = (first + last) // 2
        if a_list[i] == item:
            return '{} found at position {}'.format(item, i)
        elif a_list[i] > item:
            last = i - 1
        elif a_list[i] < item:
            first = i + 1
        else:
            return '{} not found in the list'.format(item)

# Recursive implementation of binary search

def recurBinSearch(a_list, item):
    # Performs recursive binary search of an integer in a given sorted list
    # a_list: sort list of integers
    # item: integer that is being searched for

    first = 0
    last = len(a_list)

    if len(a_list) == 0:
        return '{} was not found in the list'.format(item)
    else:
        i = (first + last) // 2
        if item == a_list[i]:
            return '{} found.'.format(item)
        elif item < a_list[i]:
            return recurBinSearch(a_list[:i], item)
        else:
            return recurBinSearch(a_list[i+1:], item)

# Menu

def menu():
    print("Welcome to Binary Search Incorporated!")
    method = input("[R]ecursive or [I]terative search?  ")
    numList = fileToList()
    numListMin = numList[0]
    numListMax = numList[-1]

    while method.lower() == 'r' or method.lower() == 'i':
        try:
            value = input("What value needs to be found? (Between {} and {}, inclusive)  ").format(numListMin,numListMax)
            if int(value) < numList[0] or int(value) > numList[-1]:
                raise ValueError("Please guess a number within the given range.")
            if method.lower() == 'r':
                print(recurBinSearch(numList, int(value)))
            else:
                print(iterBinSearch(numList, int(value)))
        except ValueError as err:
            print("Oh no! That is not a valid value. Try again...")
            print("({})".format(err))
    else:
        print("You entered the wrong letter, dumbass")

if __name__ == "__main__":
    menu() 
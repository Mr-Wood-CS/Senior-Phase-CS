import random

numbers = []

def random20numbers ():
    for x in range(20):
        numbers.append(random.randint(1,51))
    return numbers

def getSearchNumber():
    search_number = int(input("Enter the number to search for -  "))
    return search_number

def linearSearch (search_number, numbers):
    found = bool(0)
    position = int (0)
    while found == 0 and position <=19:
        if numbers[position] == search_number:
            found = 1
            print ("The number", search_number,"was found at position",position+1,".")
        else:
            position += 1
    if found == 0:
        print ("The number is not in the list.")
    
def main():
    numbers = random20numbers()
    search_number = getSearchNumber()
    linearSearch(search_number, numbers)
    
main()








from dataclasses import dataclass

def catInformation():

    @dataclass

    class cat:
        name: str
        age: int
        length: float
        outdoor: bool

    cat1 = cat("Fluffy", 4, 0.56, bool(1))
    cat2 = cat("Tiddles", 2, 0.34, bool(0))
    cat3 = cat("Mr Meows", 9, 0.83, bool(0))
    
    return cat,cat1,cat2,cat3

def showCatRecords(cat,cat1,cat2,cat3):
    
    print()
    print (cat1.name)
    print()
    print ("Cat info:",cat2.name,"Outdoor",cat2.outdoor)

    cat4 = cat("Misty", 5, 0.49, bool(1))

    print ("Years old",cat4.age,"Size",cat4.length)

def main():
    cat,cat1,cat2,cat3 = catInformation()
    showCatRecords(cat,cat1,cat2,cat3)

main()
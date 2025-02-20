# Working with .csv Files

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Glazing-Company.py](../Static/5.2-Glazing-Company.py){:download="Glazing-Company.py"}
</div>

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Glazing-Company.csv](../Static/Glazing_Company_Program.csv){:download="Glazing-Company.csv"}
</div>

## Explanation

CSV stands for Comma Separated Values and is a format usually associated with importing and exporting from spreadsheets and databases.

It allows greater control over the data than a simple text file, as each row is split up into identifiable columns. 

Below is an example of how the data is stored:
	
| Name  | Age | Reg Number |
| :---: | :--:| :----------:
| Peter | 17  | r1         |
| Laura | 16  | r1         |
| Marie | 16  | r1         |	

A .csv file would store the above data as:

```txt
	Peter, 17, r1
	Laura, 17, r1
	Marie, 16, r1
```
It may be easier to think of the data as being separated into columns and rows that use an index to identify them:

|     | Name  | Age | Reg Number |
| :-: | :---: | :--:| :----------:
| 0   | Peter | 17  | r1         |
| 1   | Laura | 16  | r1         |
| 2   | Marie | 16  | r1         |

##  Options (modes)

When opening a .csv file to use, you must first specify how that file will be used.

The options are:

#### `Write Mode`

:   __"w" (write Mode)__ creates a new file and writes to that file. If the file already exists, a new file will be created, overwriting the existing file.

	!!! example
	
		```Python
			# This must be at the top of your program to allow Python to use the csv libary of commands.
			import csv
			
			# Create a new file called "School-Reg.csv", overwriting any previous files of the same name.
			file = open("School-Reg.csv", "w")
			
			# Add 3 new records to the file
			newRecord1 = ("Peter,17,r1 \n")
			newRecord2 = ("Laura,17,r1 \n")
			newRecord3 = ("Marie,16,r1 \n")
		```

#### `Read Mode`

:   __"r" (Read Mode)__ opens for reading and will not allow you to make changes.

	!!! example
	
		```Python
			import csv
			
			# Open "School-Reg.csv" in read mode.
			file = open("School-Reg.csv", "r")
			
			# Display the records one row at a time.
			for row in file:
			    print(row)
			           
			file.close()
		```

#### `Append Mode`

:   __"a" (Append Mode)__ used to add new data to the end of the file.

	!!! example
	
		```Python
			import csv

			# Open "School-Reg.csv" in append mode.
			file = open("School-Reg.csv", "a")
			
			# Ask user to enter name, age and reg
			name = str(input("Enter Name: "))
			age = int(input("Enter Age: "))
			regNumber = str(input("Enter Reg: "))
		```

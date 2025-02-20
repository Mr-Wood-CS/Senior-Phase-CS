# Working with Files

## Program Files

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Glazing-Company](../Static/5.2-Glazing-Company.py){:download="Glazing-Company.py"}
- :fontawesome-brands-python: [Golf Championship](../Static/Golf-Championship.py){:download="Golf-Championship.py"}
</div>

## Explanation

In this lesson, we will learn about file handling, which allows our programs to manage large amounts of data efficiently, similar to how real-world systems work.

While it’s useful to create lists, make changes, and add new data, if your program resets every time it runs and your changes are lost, it’s not very practical. That’s why it’s sometimes necessary to save data outside the program, so it can be stored and any changes you make are saved.

In real-world systems that handle huge amounts of data, such as millions of inputs, this data is usually provided to the program through a file. 

File handling is often called sequential file processing because the program reads the data in the same order it appears in the file, and writes it back in a similar sequence. This ensures that data is saved and retrieved in an organized and efficient way.

The easiest way to start learning about saving and loading data is by using a text file. 

##  Options (modes)

#### `Write Mode`

:   __"w" (write Mode)__ creates a new file and writes to that file. If the file already exists, a new file will be created, overwriting the existing file.

	!!! example
	
		```Python
			# Before using a file in a program, it must first be opened.
			# To do this, link the file to an object by assigning it a reference name.
			# The open function, written as open(“file name”, “access type”), locates the file. 
			file = open("School-Reg.txt", "w")
			
			# Use the file object’s .write(string) method to insert string data into the file
			# The string being written can either be a direct string or a string variable.
			file.write("Name: Peter, Age: 17, Reg: R1 \n")
			file.write("Name: Laura, Age: 17, Reg: R1 \n")
		```

#### `Read Mode`

:   __"r" (Read Mode)__ opens for reading and will not allow you to make changes.

	!!! example
	
		```Python
			# Open the School-Reg file in 'read mode'. 
			file = open("School-Reg.txt", "r")
			
			# Display the entire file.
			print(file.read())
			
			# Close files once the program has finished using it.
			file.close()
		```
	!!! tip
		Note: you can also use file.readline() to read a file. Readline reads a single line of characters from the current position of the file and returns the data as a string. Readline however is not required at __Higher__

#### `Append Mode`

:   __"a" (Append Mode)__ used to add new data to the end of the file.

	!!! example
	
		```Python
			# Open the School-Reg file in 'append mode'
			file = open("School-Reg.txt", "a")
			
			# Add another line to the file
			file.write("Name: Karl, Age: 16, Reg: R1 \n")
			
			# Close file once the program has finished using it. 
			# Note: if the file.close() line is not included, the changes will not be saved to the txt file.
			file.close()
		```

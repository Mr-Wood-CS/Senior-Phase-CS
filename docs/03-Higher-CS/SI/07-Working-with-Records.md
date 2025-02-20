# Working with Records

## Lesson Files

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Cat Records](../Static/07-Working-With-Records/Cat-Records-Program.py){:download="Cat-Records-Program.py"}
</div>

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Address Book](../Static/07-Working-With-Records/Address-Book.py){:download="Address-Book.py"}
</div>

!!! info "What you need to know"

	You must be able to describe, exemplify and implement records 

## Explanation

So far, we’ve used only one type of data structure to store multiple values: the array. 

Remember, an array is like a list of related variables that all share the same data type. For example, an array could store a list of numbers or a list of names, but not both.

While arrays can only hold one type of data, records allow us to store different types of data together in a single structure. For example, one record can store a name (string), an age (integer), and a status (Boolean) all in one place.

Just like in a database, records help us organize related information more efficiently.

By using records, we can keep all related data about a single person or object together in one structure, and we can use real-world names for each category (called fields) to make the data easier to understand and manage. 

__This is especially useful because most systems we work with, like databases, organize data in this way.__

## Record Structures

A record structure is like creating your own custom data type. 

As a programmer, you define a record with a name that represents something real, like "Student" or "Product" and specify different categories (fields) for storing information. 

Each field has a name and a specific data type (e.g., string, integer, Boolean), so the program knows how to store and handle each piece of data. 

This way, when the program creates actual records, it knows exactly what kind of information to expect in each field.

## Creating a Single Record Structure

### Part One

=== "Python"

    ``` python linenums="1"
	from dataclasses import dataclass
	
	@dataclass
    ```

=== "Explanation"

	__Line 1 - from dataclasses import Dataclass__
	This line is like getting a special helper from a toolbox. It brings in something called dataclass, which makes it easier to create a class that stores information.
	
	__Line 3 - @dataclass__
	This is a special tag that tells Python, "I want to make the next class a dataclass." This means Python will automatically help us with things like creating the class and keeping track of data inside it.

### Part Two

=== "Python"

    ``` python linenums="1"
		from dataclasses import dataclass
		
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
    ```

=== "Explanation"

	__Line 5 - class SchoolReg__
	Here, we are creating a class called SchoolReg. A class is like a blueprint or recipe. In this case, it helps us create something to store information about a school registration, like a student's name, age, and registration number.
 
	__Line 6 - Name: str = ""__
	Inside the class, we create a variable called Name. This will hold the student's name, and it's a string, which means it's a word or group of letters (like "Peter"). The empty quotes " " mean that we are starting with no name yet.
 
	__Line 7 - Age: int = 0__
	This is another variable called Age. It will hold the student's age, and it's an integer (which means a whole number like 17). Right now, we start it at 0.
 
	__Line 8 - Reg: str = ""__
	This variable is called Reg, which stands for "registration number." It’s also a string (a group of letters or numbers). At first, it's an empty string "", but we will fill it in later.

### Part Three

=== "Python"

    ``` python linenums="1"
		from dataclasses import dataclass
		
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = SchoolReg()
		pupilRecord.Name = "Peter"
		pupilRecord.Age = 17
		pupilRecord.Reg = "r1"
    ```

=== "Explanation"

	__Line 10 -  pupilRecord = SchoolReg()__
	Now we create an object called pupilRecord from the SchoolReg class. Think of the class as a cookie cutter, and this object is a cookie made from it. This object will store a student's name, age, and registration number.
 
	__Line 11 - pupilRecord.Name = "Peter"__
	Here, we set the Name of the pupilRecord object to "Peter". Before it was empty (""), but now it's filled with the name "Peter".
	
 	__Line 12 - pupilRecord.Age = 17__
	Next, we set the Age for pupilRecord to 17. Before, it was 0, but now we know Peter is 17 years old.
	
 	__Line 13 - pupilRecord.Reg = "r1"_
	Here, we set the registration number (Reg) to "r1". Now, the student Peter has a registration number "r1".

### Part Four

=== "Python"

    ``` python linenums="1"
		from dataclasses import dataclass
	
		@dataclass
		
		class SchoolReg:
		    Name : str = ""
		    Age : int = 0
		    Reg : str = ""
		
		pupilRecord = SchoolReg()
		pupilRecord.Name = "Peter"
		pupilRecord.Age = 17
		pupilRecord.Reg = "r1"
		
		print (pupilRecord.Name) 
		print (pupilRecord.Age) 
		print (pupilRecord.Reg) 
    ```

=== "Explanation"

	__Line 15 - print(pupilRecord.Name)__
	This line tells the computer to print (show) the name of the student, which is "Peter". The computer will display "Peter" on the screen.
	
 	__Line 16 - print(pupilRecord.Age)__
	This prints the student's age, which is 17. The computer will show 17 on the screen.
 
	__Line 17 - print(pupilRecord.Reg)__
	Finally, this prints the student's registration number, which is "r1". The computer will show "r1".

# Sub-program Procedures

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Glazing-Company](../Static/5.2-Glazing-Company.py){:download="Glazing-Company.py"}
</div>

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Glazing-Company](../Static/5.2-Glazing-Company.py){:download="Glazing-Company.py"}
</div>

## Local & Global Variables

During National 5 you worked with variables throughout the entire scope of a program as well as accessing, using and changing their data values anywhere in the code, this is known as a Global Variable.

A __global__ variable is created in the main part of the program and can be passed/accessed by other parts of the program.

A __local__ variable however is only used within a single block of code and cannot be seen or accessed from other parts of the program.

The scope of a variable defines which part of the program can see the variable and change its value. 

__For example the scope of a local variable is the subroutine it is in.__

!!! example

	```Python
		totalAppDownloads = 2305651
	
		def downloadsForMonth():
	
		    print "Current download amount: ", totalAppDownloads,"downloads"
		
		    monthDownloads = int(raw_input("How many downloads did the App have this month?  "))
		
		    return monthDownloads
	
		def newTotalDownloads(monthDownloads):
		
		    totalAppDownloads = totalAppDownloads + monthDownloads
		
		    return
	```

## Parameter Passing

A parameter is a value that is being passed in or out of a subprogram.  In the example below you can see two parameters being passed into the calculate sub-program. 
In all the software development we do we are going to follow the “good practice” of using Local Variables within our sub-programs. This means we need to implement Parameter Passing to get the required data in and out of a module and so that it can used elsewhere in a program.
In the example below you can see two parameters being passed into the calculate sub-program on line 6
!!! example
	```Python
	def input_lunch_info():
		lunch_cost = float(input("Enter the cost of lunch - "))
		years_member = int(input("Enter the years of membership - "))
		return lunch_cost, years_member
	
	def calculate_final_cost (lunch_cost, years_member):
		if lunch_cost >= 55 or years_member > 3:
		print ("£{:.2f}".format(lunch_cost - 10)) 
		else:
		print ("£{:.2f}".format(lunch_cost)) 
	```
## Formal Parameters

Formal parameters are placeholders within a subprogram for the values received from main program’s actual parameters. 
In the example below there is a ‘validate’ sub program. This has min, max and number as its parameters. The lines of code with the arrow pointing to it show different values are passed into the ‘validate’ sub program when it runs. 
Within the validate sub-program the values that are passed in are known as min, max and number. This is why they are called placeholders for the values that are received from the main program.

## Actual Parameters

This is the actual data sent to a subprogram. It's found in the line of code that you call the function. In the example below you can see checkAnswer(userAnswer). Within that, userAnswer would be the actual parameter.



By replacing a stack of instructions with one single statement, it makes code easier to read and debug. A procedure does not return a value.

In Python we give a procedure a name, this is done by giving them a name after the, “def” instruction. The brackets after the procedure name are used to pass in data that will be used in that block of code. This is known as parameter passing. 

!!! info
	A procedure literally just executes commands.

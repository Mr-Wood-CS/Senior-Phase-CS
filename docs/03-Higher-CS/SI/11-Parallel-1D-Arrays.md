# Parrllel 1D Arrays

!!! info "What you need to Know"

	__You must be able to describe, exemplify and implement parallel 1D arrays.__

## Explanation

You already know that an array is a list of related values, called elements, that can be referred to by number, e.g. temperature[0], temperature[5] etc. 

<figure markdown="span">
  ![img 1](../Images/Parallel-1D-Arrays-1.png){ width="800" }
</figure>


This example below now adds a second array that records the date on which the temperature was taken.

We can look up the temperature on the 8th of June, by looking for that date, and reading the corresponding temperature __(14°)__. 

__These are parallel arrays, because we can look up corresponding values, like a table.__

<figure markdown="span">
  ![img 2](../Images/Parallel-1D-Arrays-2.png){ width="800" }
</figure>

<!---{ width="300" }-->

In this example, pupil marks are stored in one array, and pupil names are stored in another. 

__We can see that Jack scored 23, and Lucy scored 24, by looking at the two arrays side-by-side, as if they were a table.__

<figure markdown="span">
  ![img 3](../Images/Parallel-1D-Arrays-3.png){ width="800" }
</figure>

There is no special syntax or different way to write these.

__We just declare two arrays.__

!!! example
	
	```Python
 
	          # Two *parallel* arrays of pupil names and marks
	          pupil_name = ["Peter", "Laura", "Marie"]
	          pupil_mark = [20, 21, 23]
	          
	          # If we want to find the name and mark of the third pupil in the list, we would say:
	          print(pupil_name[2])
	          print(pupil_mark[2])
	  
	```

## Working with Files

This example is based on the Schools-Reg.csv file from earlier

<figure markdown="span">
  ![img 4](../Images/Parallel-1D-Arrays-4.png){ width="800" }
</figure>

We would implement this program with three parallel arrays - __one for name, age and reg group__.

This program reads the Schools.csv file, and produces an array of lines - __each line of the file__. 

We then split each line into parts __(comma separated values)__, e.g.:

<figure markdown="span">
  ![img 5](../Images/Parallel-1D-Arrays-5.png){ width="800" }
</figure>

!!! example
	
	```Python
		import csv
		
		# Open the file for reading
		file = open("School-Reg.csv", "r")
		    
		# Assign Parallel arrays for school reg data
		name = [str] * 3
		age = [int] * 3
		regGroup = [str] * 3
		
		# Loop through the array of lines
		for line in range(0, 3):
		    data = file.readline()
		    # Strip characters that are not required
		    data = data.strip("\n")
		    # Split the data on the comma
		    data = data.split(",")
		    
		   # Store the 'data' in the parallel arrays
		    name[line] = data[0]
		    age[line] = data[1]
		    regGroup[line] = data[2]
		    
		# Display the arrays
		for i in range (0,3):
		  print("Name: " + name[i] + " Age: " + str(age[i]) + " Reg: " + regGroup[i])
		    
		# Close the file
		file.close()
	```

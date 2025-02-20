# Count Occurrences

!!! info "What you need to know"

	You must be able to describe, exemplify and implement arrays of records 

## Explanation

Count occurrences are very similar to linear search:

* The user enters a target/search-term.
  
* The algorithm then searches the array. 

* If the target is found, instead of recording position, it adds +1 to a total/counter. 

By doing this, it counts how often a particular condition is met.

It could also be used to check for an exact match - for example, in a list of names, how many people are called Bob?

However, we could also use it with other conditions:

* In a list of percentages, how many are above 75%?

* In a list of integers, how many are even?

* In a list of letters, how many are upper-case?

!!! warning "Important"

    * Do not confuse __counting occurrences__ with __keeping a running total__: one counts how many of something there are, the other adds them all together.  
    
    * __There might be times when you are asked to do both on the same question.__
    
    * Do not confuse ‘__count__’ or ‘__counter__’ with the loop counter. 
    
    * Your loop counter (e.g. for counter in range...) might use a similar name, e.g. you call one count and the other counter. 
    
    * You could call your loop counter something like “for index in range(0,9)”  to make sure you don’t get confused.

The example below  asks the user to enter a target. It loops through a list of ten names. It checks if each element matches the target. If so, it adds 1 to the count. At the end, it displays how many were found.

=== "__Algorithm Example__"

    ```pseudocode linenums="1"
       Set count to 0
       
       Input target
       
       For index from 0 to 9
       
		If names(index) == target then
  
			Set count to count + 1
   
		End if
  
       End for loop
       
       Display count

    ```

=== "__SQA-style Marking Scheme for a Linear Search (4 marks)__"

    * Initialise the count variable  (__1 mark__)
 
    * Loop through the elements of the array (__1 mark__)
		
    * Check if the element matches target (__1 mark__)
		
    * Add 1 to the count variable (__1 mark__)

    The final mark in the example (__setting the variable to true__) might be replaced with something else, depending on the question. 
    
    For example, you might be asked to find the position of the element.


## Example 1 - Using == Sign

=== "Python"

	``` python linenums="1"
		# A list of cars spotted on a road, recorded by make
		cars = ["Ford", "Ford", "Toyota", "Volkswagen", "Kia", "Nissan", "Honda"]
		
		# Ask the user to enter a target
		make = input("Please enter a make:")
		count = 0
		
		for index in range(0, 7):
		  if cars[index] == make:
		    count = count + 1
		
		# Display how many
		print("There were", count, "matching cars")
	```

=== "Explanation"

    This program contains data for cars spotted going down a road at a particular time. 
    
    The programmer wants to be able to find how many Fords, Nissans or Hondas were recorded.

    The user enters a make.

    The program then searches through the list of cars, and if the make matches, it adds 1 to the counter.

    At the end of the program, it shows how many of that make were found.


## Example 2 - Using >= Sign

=== "Python"

	``` python linenums="1"
		# A list of percentages
		percentages = [99.7, 100.0, 52.6, 13.9, 15.2, 88.1, 64.7, 22.5, 71.8]
		
		# How many are at least 50%?
		target = 50.0
		count = 0
		
		for index in range(0, 9):
		  if percentages[index] >= target:
		    count = count + 1
		
		# Show results
		print("There were", count, "values of 50% or more")

	```

=== "Explanation"

    This program contains data for cars spotted going down a road at a particular time. 
    
    The program sets a target of 50.0, and counts how many of the percentages are greater than or equal to the target.

## Example 3 - Odd or Even

=== "Python"

	``` python linenums="1"
		# A list of integers
		numbers = [99, 44, 55, 12, 19, 72, 60, 54, 13, 18, 2, 75]
		
		# Are these odd or even?
		odd_count = 0
		even_count = 0
		
		for index in range(0, 12):
		  if (numbers[index] % 2) == 0:
		    even_count = even_count + 1
		  else:
		    odd_count = odd_count + 1
		
		print("There were", even_count, "even numbers")
		print("and", odd_count, "odd numbers in the list")
	```

=== "Explanation"

    This program has a list of numbers, and counts how many are odd and how many are even, using two counters:



# Linear Searching

<div class="grid cards" markdown>
- :fontawesome-brands-python: [Linear-Number-Search.py](../Static/09-Standard-Algorithms-(Linear-Search)/Linear-Number-Search.py){:download="Linear-Number-Search.py"}
</div>

!!! info "What you need to know"

	You must be able to describe, exemplify and implement arrays of records 

## Explanation

You learned three standard algorithms for National 5:

* Input validation
* Running total in a loop
* Traversing an array (simply, looping through each item in the array, one at a time)

For Higher, we add three more standard algorithms:

* Linear search
* Count occurrences
* Find minimum/maximum

__All of the above require you to be able to traverse an array.__

For each algorithm, you must be able to:

* Write it in pseudocode
* Write a memorised example in program code, then:
* Write it in the context of a question you’re given, in the exam or assignment

__The first step is to learn/memorise the algorithms; then, you can apply them to unfamiliar contexts.__

## Linear Search 

A linear search is used with one or more arrays of items. We traverse (loop through) the array, looking for a particular value. 

If one of the items in the array matches the search value, we do something.
There are two variations of the algorithm: one simply records if something is found; the other records where in the list it is found. 

It should be clear from a question which one you’re expected to use.

The example below asks for a target (search term the user is looking for). 

* It loops through 10 names. 
* If each name matches the target, it switches the ‘found’ variable to true. 
* At the end of the program, we could know if the name was in the list by checking the value of the found variable.

=== "__Algorithm Example__"

    ``` pseudocode linenums="1"
	Set found to false
	
	Input target
 
  	For counter from 0 to 9
    
    		If names(counter) == target then

			Set found to true
 
		End if

	End for loop
    ```

=== "__SQA-style Marking Scheme for a Linear Search (4 marks)__"

    * Initialise the variable (__1 mark__)
 
    * Loop through the elements of the array (__1 mark__)
		
    * Check if the element matches target (__1 mark__)
		
    * Set variable to true (__1 mark__)

    The final mark in the example (__setting the variable to true__) might be replaced with something else, depending on the question. 
    
    For example, you might be asked to find the position of the element.




## Example 1 - Using Found

=== "Python"

	``` python linenums="1"
		# An array of seven names
		names = ["Dopey", "Grumpy", "Doc", "Bashful", "Sneezy", "Sleepy", "Happy"]
		 
		target = input("Enter a name to look for")
		found = False
		
		# Loop through each item
		for counter in range(0,7):
		  # Check each item against the target
		  if names[counter] == target:
		    found = True
		
		# Is the target in the list?
		print("Item was found:", found)

	```

=== "Explanation"

    This program contains a list of names. It asks the user to enter a search target. Then it searches the list of names to see if any of them match the target. 
    
    If they do, it confirms that the target was found.

    At the end of the program, the console should show a message confirming whether the target was in the list.
    
## Example 2 - Using Posistion

=== "Python"

	``` python linenums="1"
		# An array of seven names
		names = ["Dopey", "Grumpy", "Doc", "Bashful", "Sneezy", "Sleepy", "Happy"]
		 
		target = input("Enter a name to look for")
		position = -1
		
		# Loop through each item
		for counter in range(0,7):
		  # Check each item against the target
		  if names[counter] == target:
		    position = counter
		
		# Is the target in the list?
		print("Item was found at position:", position)
	```

=== "Explanation"

    Sometimes, we want to know the position of an element in the array - for instance, the target was found at position 5. This example uses the same basic program as the one above, but instead of reporting whether the name is found, it reports its position.

    We set the starting position to -1. This is because it isn’t possible to be at position -1 in the array. That way, we know that anything other than -1 must mean the item was found, so the position was changed.

    __If, at the end of the program, the value of position was still -1, we would know that the target hadn’t been found.__

## Example 3 - Using Posistion with Parallel Arrays

=== "Python"

	``` python linenums="1"
	# An array of pupil names, and a *parallel* array of marks
	pupils = ["Bob", "Bart", "Krusty", "Mel", "Lisa"]
	marks = [10, 2, 1, 8, 9]
	
	# Ask for a person's name, and print their mark
	target_name = input("Please enter a name:")
	position = -1
	
	# Loop through names
	for counter in range(0, 5):
	  if pupils[counter] == target_name:
	    position = counter
	
	# If we found their name at [position], their mark must also be there
	their_mark = marks[position]

	```

=== "Explanation"

    This program has two arrays: one of pupil names, and one of marks. 
    
    Both arrays have the same number of elements. 
    
    Looking at a name, we can find their mark by going to the corresponding element in the marks array (so the third name corresponds to the third mark). 
    
    The program asks for a target name. 
    
    It loops through the first array, and finds the position where that name is in the list. Later, we can find the corresponding mark, because if the name was found at pupils[position], their mark must be stored at marks[position].



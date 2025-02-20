# Storing NNegative Numbers (Two's Complement) 

Sign bits
Negative numbers have a ‘sign bit’ - the first digit of the binary number (closest to the left) is used to show whether the number is positive or negative.
The method for representing negative numbers is called Two’s Complement.


We use twos complement to store negative numbers in a computer. In this course you only need to know 8-bit twos complement. 

So how does it work? 

Note that in binary adding 1 and 1 together gives 0 and you will carry the 1 onto the next column to the left.

Let's start with the number we want to represent, -10.

Represent 10 in binary.

0000 1010 = 10
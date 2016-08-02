# Name:
# Section:
# hw2.py

##### Template for Homework 2, exercises 2.0 - 2.5  ######

# **********  Exercise 2.0 ********** 

#def f1(x):
#    print x + 1

#def f2(x):
#    return x + 1

# **********  Exercise 2.1 ********** 

# Define your function here
##### YOUR CODE HERE #####

# Test Cases for Exercise 2.1
##### YOUR CODE HERE #####

# ********** Exercise 2.2 ********** 

# Define is_divisible function here
#Problem statement: Write a method is divisible that takes two integers, m and n. The method returns True if m is divisible by n, and returns False otherwise. Test cases for this function are included for you; look at the conditions that they test and try to make sure your future test cases are comprehensive.
##### YOUR CODE HERE #####

#request input of variables
m = raw_input("Enter a number. ")
n = raw_input("Enter another number. ")

#determine if n is divisible by n
remainder = m % n
if remainder  == 0:
    print "True"
#else remainder != 0:
else:
    print "False"



#2. Imagine that Python doesn’t have the != operator built in. Write a method not equal that takes two parameters and gives the same result as the != operator. Obviously, you cannot use != within your function! Test if your code works by thinking of examples and making sure the output is the same for your new method as != gives you.



# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?


# Define not_equal function here
##### YOUR CODE HERE #####

# Test cases for not_equal
##### YOUR CODE HERE #####

# ********** Exercise 2.3 ********** 

## 1 - multadd function
##### YOUR CODE HERE #####

## 2 - Equations
##### YOUR CODE HERE #####


# Test Cases
# angle_test =
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test

# ceiling_test =
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test

## 3 - yikes function
##### YOUR CODE HERE #####


# Test Cases
# x = 5
# print "yikes(5) =", yikes(x)

# ********** Exercise 2.4 **********

## 1 - rand_divis_3 function
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####

## 2 - roll_dice function - remember that a die's lowest number is 1;
                            #its highest is the number of sides it has
##### YOUR CODE HERE #####

# Test Cases
##### YOUR CODE HERE #####                            


# ********** Exercise 2.5 **********

# code for roots function
##### YOUR CODE HERE #####   

# Test Cases
##### YOUR CODE HERE #####   

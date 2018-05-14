"""Q. 12

Write a Single line Python program that takes two inputs: "String" and "Num".
And then prints the input string given number of times, separated by a single space (Trailing spaces are allowed, but a plus if you remove them as well)

Egs.
Input:
String: A
Num: 5
Output:
A A A A A
 
Input:
String: ABC
Num: 3
Output:
ABC ABC ABC 
 
Input:
String: A      B   !
Num: 7
Output:
A      B   ! A      B   ! A      B   ! A      B   ! A      B   ! A      B   ! A      B   !
"""

print ((raw_input("String: ") + " ") * input("Num: ")).strip()


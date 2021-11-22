"""
Write a program that asks a user for two integers. Print "YES" if they're both odd and print "NO" otherwise. Hint use AND or OR
"""
print("Give me two integers, and I will determine wether both are odd or not ")
firstInteger = int(input(" Enter the first integer. "))
secondInteger = int(input("Enter the second Integer. "))
#asks user for integers
if firstInteger % 2 == 1 and secondInteger % 2 == 1:
  print ("They are both odd ")
else:
  print("They aren't both odds")
#Compares integers to see if they are integers

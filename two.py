'''
Write a program that reads the length of the base and the height of a right-angled triangle and prints the area.
every number is given on a separate line.
'''

base = int(input("enter the first value:"))
height = int(input("enter the second value:"))
area = base * height // 2
print(area)
print(f"the area is {area}")
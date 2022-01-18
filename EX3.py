# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]

def print_factor(y):
	print(y)

# EX1
# Find the all factors of x using a loop and the operator % 
# % means find remainder, for example 10 % 2 = 0; 10% 3 = 1
def find_factor(x):
	for i in range(1,x+1):
		if(x%i==0):
			print_factor(i)

for i in range (0,len(l)):
	print("Question: " + str(l[i]))
	print("Answer: ")
	find_factor(l[i])
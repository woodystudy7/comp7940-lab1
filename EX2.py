# EX2
# Write a function that prints all factors of the given parameter x
def print_factor(y):
	print(y)

x = 52633
for i in range(1,x+1):
	if(x%i==0):
		print_factor(i)


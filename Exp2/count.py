string = input("Enter a string : ")
count = 0
s=0
for c in string :
	if c.isspace() != True:
		count = count + 1
	elif c.isspace() == True:
		s=s+1
print("Total number of characters : ",count)
print("Total number of space : ",s)
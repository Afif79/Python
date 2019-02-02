a=[]
high= 0
low= 1000
#------------------------------------------------------------
for i in range(4):
	n=int(input("Enter Number:"))
	a.append(n)
print(a)
#------------------------------------------------------------
for i in a:
	if i > high:
		high=i
print(high)
#------------------------------------------------------------
for i in a:
	num=int(i)
	if num < low:
		low =num
print(low)
#------------------------------------------------------------
print("Greatest Number in the list:",max(a))
#------------------------------------------------------------
print("Lowest Number in the list:",min(a))


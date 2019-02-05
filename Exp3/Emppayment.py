def salary(b,d):
    b=b-d*(b/30)
    return b+b*0.10+b*0.15
def salary1(b,d,h):
	b=b-d*(b/30)
	h=h*100
	return b+b*0.10+b*0.15+h
print("HRA:10%  DA:15%")
b=int(input("Enter Basic salary:-"))
d=int(input("Enter number of days absent:-"))
i=input("\nEnter Y if done overtime:")
if i=='Y' or i=='y':
	h=int(input("\nEnter how many days done overtime in a month:"))
	if h>15:
		print("You got incintive of 1000 ₹")
		print("salary:-",(salary1(b,d,h))+1000,"₹")
	elif h<=15:
		print("salary:-",salary1(b,d,h),"₹")
else:
	print("salary:-",salary(b,d),"₹")

def fine(d):
	if d<=15:
		print("\nYou can return the book without fine")
		return 0
	elif d<=25 :
		return 5*(d-15)
	else :
		return 7.5*(d-15)
        
def fine2(d1):
	if d1<=20:
		print("\nYou can return the book without fine")
		return 0
	elif d1<=30:
		return 6*(d1-15)
	else:
		return 8*(d1-15)
		
print("\t\t\t*****Library Management*****\n\n 1.Return Book\n\n 2.Lost Book")
opt=int(input("\nSelect option:"))
if opt==1:
	c=input("\nEnter Category of book(E for Engineering/M for Management):")
	if c=='E' or 'e':
		d=int(input("\nEnter number of Days from book issued:"))
		print("fine: ",fine(d),"₹")
	elif c=='M' or 'm':
		d1=int(input("\nEnter number of Days from book issued:"))
		print("fine: ",fine2(d1),"₹")
elif opt==2:
    print("\nStudent should pay cost of book")
    cost=input("\nEnter cost of book:")
    print("fine: ",cost)
else :
    print("Invalid Option")

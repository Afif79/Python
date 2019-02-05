def dist(d1,d2):	
	return d1+d2
print("Select operation.")
print("1.Enter distance in feet")
print("2.Enter distance in inches")
choice = input("Enter choice(1/2):")
if choice ==('1'or '2'):
	d1=float(input("Enter Distance 1:"))
	d2=float(input("Enter Distance 2:"))
	if (d1 or d2) < 0:	
		print ("Invalid distance")
	else:
		td=dist(d1,d2)
		if choice == '1':
			print ("Total distance is ",dist(d1,d2),"feet.")
			print ("Total distance is ",td*12,"inches.")
		elif choice == '2':
			print ("Total distance is ",dist(d1,d2),"inches.")
			print ("Total distance is ",td/12,"feet.")
else:
	print("Invalid choice")

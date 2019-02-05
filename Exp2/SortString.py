while True:
	a = input("\nEnter y for yes/n for no to continue: ")
	if a=='y' or a=='Y':
		print("\n\n\t\t\t*****Sort*****\n\n 1.Strings\n\n 2.Numbers")
		opt=int(input("\nSelect option:"))
		if opt==1:
			s=[x.lower() for x in input("\nEnter String into list(space after each string): ").split()]
			s.sort()
			print("\n",s)
		elif opt==2:	
			s=[x for x in input("\nEnter Numbers into list(space after each number): ").split()]
			s = [int(x) for x in s]
			s.sort()
			print(s)
			continue
	elif a=='n' or a=='N':
		break
	else:
		print("\nEnter either y or n: ")
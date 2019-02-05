while True:
	a = input("\nEnter y for yes/n for no to continue: ")
	if a=='y' or a=='Y':
		print("\n\t\t\t\t*********List Operation*********")
		#l = [x for x in input("\nEnter data into list: ").split()]
		l2=[]
		print("\nSelect operation.")
		print("1.Create & Print list \t 2.Append \t 3.Copy \t 4.Length \t 5.Search \n6.Pop \t\t 7.Sort \t 8.Reverse \t 9.Join \t 	10.Remove")
		c= int(input("Enter choice:"))
		if c==1:
			l = [x for x in input("\nEnter data into list: ").split()]
			print("Print List ",l)
		elif c==2:
			a= input("Enter data to append:")
			l.append(a)
			print("Appended list:",l)
		elif c==3:
			l2=l.copy()
			print("Original list l1:",l)
			print("Copied list l2:",l2)
		elif c==4:
			print("length:",len(l))
		elif c==5:
			v= input("Enter data to search:")
			if v not in l:
				print(v," is not present in the list")
			else:		
				print(v," is on location ",l.index(v))
		elif c==6:
			p= int(input("Enter Position to pop:"))
			if p>len(l):
				print("Enter valid position")
			else:
				print("Pop: ", l.pop(p))
		elif c==7:
			l.sort()
			print("Sorted List: ",l)
		elif c==8:
			l2=l.copy()
			l.reverse()
			print("Original list :",l2)
			print("Reversed list: ",l)
		elif c==9:
			j=",".join(l)
			print("9.Join",j)	
		elif c==10:
			r= input("Enter Data to Remove:")
			if r not in l:
				print(r," is not present in the list")
			else:	
				l.remove(r)
				print(r," is removed")
				print("Updated List",l)	
		continue
	elif a=='n' or a=='N':
		break
	else:
		print("\nEnter either y or n: ")				
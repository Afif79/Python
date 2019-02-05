def fibo(n):
	if n<=1:
		return n
	else:
	       return(fibo(n-1) + fibo(n-2))
x=int(input("Enter Number for fibonacci Series"))
if x<=0:
	print("Plese enter a positive integer")
else:
	print("Fibonacci series:")
	for i in range(x):
		print(fibo(i))

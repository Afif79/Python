l = [x for x in input("\nEnter data into list: ").split()]
print(l[:])# a copy of the whole list
n=slice(1,3)# items start through 1 till 2
print(l[n])
n=slice(0,10,2)# items start through 0 till 10 by step 1
print(l[n])
print(l[2:])# items start through 2 till rest of the list
print(l[:1])# items from the beginning through 1
print(l[:-2])# everything except the last two items
print(l[-1:])# last one item
print(l[::-1])# all items in the list reversed
print(l[1::-1])# the first two items, reversed
print(l[:-3:-1])# the last two items, reversed
print(l[-3::-1])# everything except the last two items, reversed
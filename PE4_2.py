
n = []

n.append(2)
n.append(4)


print("List after adding 2 and 4:", n)


n.insert(0, 0)  
n.insert(1, 1)  
n.insert(3, 3)  


print("List after adding 0, 1, and 3 in order:", n)


n.append(5)


print("List after adding 5:", n)


n.remove(0)


print("List after removing 0:", n)


removed_2 = n.pop(n.index(2))
print("Removed 2:", removed_2)


print("List after removing 2:", n)


removed_4 = n.pop(n.index(4))
print("Removed 4:", removed_4)

print("List after removing 4:", n)


sum_removed = removed_2 + removed_4 + 0  
print("Sum of removed numbers:", sum_removed)


n[0] = 100
n[-1] = 9.9


newNum = n.copy()


n.clear()


print("Original list after clearing:", n)
print("New list (newNum):", newNum)

del n

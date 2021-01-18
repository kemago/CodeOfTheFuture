my_list1 = [1, 2, 3, 4, 5, 6]
print(my_list1)
# my_list2 = list(range(1, 6))
# print(my_list2)

# Műveletek listákkal
# A lista 3. eleme
print(my_list1[2])
# A lista utolsó eleme
print(my_list1[-1])

# Szeletelés (slice) a 2. elemtől a 4. elemig
print(my_list1[1:4])

# Lista hossza
print(len(my_list1))

# Lista legnagyobb és legkisebb eleme
print(min(my_list1))
print(max(my_list1))

# Elem hozzáadása a listánkhoz
my_list1.append(-10)
print(my_list1)

# Lista megfordítása
my_list1.reverse()
print(my_list1)

# Másik lista generálása és a két lista összefűzése
my_list2 = [10, 20, 30, 40, 50, 60]

print(my_list1+my_list2)
print(my_list2+my_list1)
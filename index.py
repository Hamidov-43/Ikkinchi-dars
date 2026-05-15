fruits = ["apple", "banana", "orange"]
print(type(fruits))  # <class 'list'>
fruits.append("grape")
print(fruits)  # ['apple', 'banana', 'orange', 'grape']
fruits.remove("banana")
print(fruits)  # ['apple', 'orange', 'grape']
fruits.pop(1)
print(fruits)  # ['apple', 'grape']
admin_users = ["admin1", "admin2", "admin3"]
print("admin1" in admin_users)
print("admin7" in admin_users)

coordinates = (10.0, 20.0)
print(type(coordinates))  # <class 'tuple'>
print(coordinates)  # (10.0, 20.0)

# Set example
unique_numbers = {1,1, 2, 3, 4, 5}
print(type(unique_numbers))  # <class 'set'>
print(unique_numbers)  # {1, 2, 3, 4, 5}
unique_numbers.add(6)
print(unique_numbers)  # {1, 2, 3, 4, 5, 6}
unique_numbers.remove(2)
print(unique_numbers)  # {1, 3, 4, 5, 6}
langs = set()
langs.add("Python")
langs.add("Java")      
print(langs)  # {'Python', 'Java'}
nums1 = {1, 2, 3}
nums2 = {3, 4, 5}
print(nums1 & nums2)  # {3}
print(nums1 | nums2)  # {1, 2, 3, 4, 5}
print(nums1 - nums2)  # {1, 2}
print(nums2 - nums1)  # {4, 5}
print(nums1 ^ nums2)  # {1, 2, 4, 5}
set = {1, 2, 3, 4, 5}
print(set)  # {1, 2, 3, 4, 5}
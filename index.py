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

# Dictionary example
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}
print(type(person))  # <class 'dict'>
print(person)  # {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(person["name"])  # Alice
print(person.get("age"))  # 30      
person["age"] = 31

counter = {
    "apple": 3,
    "banana": 5,
    "orange": 2,
    "grape": 4
}
print(counter["apple"])  # 3
print(counter.keys())
print(counter.values())
print(counter.items())  
counter["melon"] = 6
print(counter)  # {'apple': 3, 'banana': 5, 'orange': 2, 'grape': 4, 'melon': 6}

cities = {
    "New York": {"population": 8000000, "area": 783.8},
    "Los Angeles": {"population": 4000000, "area": 1214.9},
    "Chicago": {"population": 2700000, "area": 589.6}
}
print(cities["New York"]["population"])  # 8000000
print(cities["Los Angeles"]["area"])  # 1214.9      
print(cities["Chicago"]["population"])  # 2700000
print(cities["New York"].items())  # 589.6
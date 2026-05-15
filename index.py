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

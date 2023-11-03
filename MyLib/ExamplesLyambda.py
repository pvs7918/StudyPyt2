a = [3, 4, 5, 2, 7, 8]
b = [7, 9, 2, 4, 5, 1]
c = [5, 7, 3, 4, 5, 9]

dict_a = [{'name': 'python', 'points': 10}, {'name': 'java', 'points': 8}]

print(list(map(lambda x, y, z: x + y + z, a, b, c)))
print(list(map(lambda x, y, z: 2 * x + 2.5 * y + z, a, b, c)))
print(list(map(lambda x: x['name'], dict_a)))
print(list(map(lambda x: x['points'] * 10, dict_a)))
print(list(map(lambda x: x['name'] == "python", dict_a)))
lambda x: x[:-1], royalty
print(list(filter(lambda x: x > 5, c)))
print(list(filter(lambda x: x % 2 == 0, a)))
print(list(filter(lambda x: x['name'] == 'python', dict_a)))

names = ["Abram", "Arib", "Bob", "Shawn",
         "Aria", "Cicilia", "John", "Reema",
         "Alice", "Craig", "Aaron", "Simi"]

print(list(filter(lambda x: x[0] != "A", names)))

dict_b = [{"name": "John", "age": 12},
          {"name": "Sonia", "age": 10},
          {"name": "Steven", "age": 13},
          {"name": "Natasha", "age": 9}]

print(sorted(names, key=lambda x: x.endswith("ia")))
print(sorted(list(map(lambda x: x["age"], dict_b))))
print(sorted(dict_b, key=lambda x: x["age"], reverse=True))
print()
print()

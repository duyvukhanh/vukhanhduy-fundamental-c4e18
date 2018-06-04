# person = ["Quý", 20, 0, "Vĩnh Phúc", 2, ["Manga","Coding"], 3, 20]


#dictionary
person = {
    "name": "Quy",
    "Age": 20,
    "ex": 0,
    "favs": ["Manga","Coding"]
}

# print(person)

# name = person["favs"]
# print(name)

person["length"] = 20

# print(person)

person["length"] = 10
# print(person)
# key = "length"

# del person["length"]
# if key in person:
#     print(person[key])
# else:
#     print("Not Found")

for k in person:
    print(k) #duyet key

for v in person.values():
    print(v)          #duyet value

for k,v in person.items():
    print(k, ":", v)


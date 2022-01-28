
person = {"first_name":"John", "last_name":"Green", "birth_year":" 1980", "country_of_birth":"Canada"}

print (person["first_name"])
person["birth_year"] = 1979
print (person)
person["marital_status"] = "Married"
print (person)
person["children"] = ["Nathalie", "Ethan"]
print(person)
person["children"].append("Anna")
print(person)
print (person.get("age", "Invalid property"))
print (person.get("children", "Invalid property"))
Key = "first_name"
print(person[Key])
#person.clear()
print(person)






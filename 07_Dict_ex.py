
person={"name":"Mike","gender":"Male","age":"50","address":"12 leaf street","phone":"955588"}

user_input = input("Enter ,Name, Gender, Age, Address or Phone of the person you want to know").lower

result = person.get(user_input, "Not available")

print (result)

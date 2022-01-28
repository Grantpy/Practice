blog_posts = ["The top 10", "HTTP requests", "Tutorial", "", "DATA", ""]

for post in blog_posts:
    if post == "":
        continue
    else:
        print(post)

print("----------------------------")

myString = "this is a string"

for char in myString:
    print(char)

print("------------------------------")

person = {"Name": "Karen Smith", "Age": 25, "Gender": "Female"}

for key in person:
    print(key, ":", person[key])

print("-----------------------------")

blog_posts = {"Python":["The top 10", "HTTP requests", "Tutorial", "", "DATA", ""], "Java":["1", "2"]}

for category in blog_posts:
             print("Posts about", category)
             for post in blog_posts[category]:\
             print(post)
             

import random
people= []

for x in range(0,8):
    person = input("type a name:")
    people.append(person)
index = random.randint(0,7)
random_person = people[index]

print("Random: ", random_person)






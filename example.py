
f = open("input/a_an_example.in.txt", "r")

inp = f.readlines()

inp = [i.strip() for i in inp]
inp = [i.split(" ") for i in inp]

contributors = inp[0][0]
projects = inp[0][1]
inp.pop(0)

users = []
skills = {}

for i in range(contributors):
    users.append(inp[0][0])
    skills[users[i]] = []
    for i in range()



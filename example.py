
f = open("input/a_an_example.in.txt", "r")

inp = f.readlines()

inp = [i.strip() for i in inp]
inp = [i.split(" ") for i in inp]

projects = inp[0][1]






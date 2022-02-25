from os import system

fName = "f_find_great_mentors.in.txt"
f = open("input/" + fName, "r")

inp = f.readlines()

inp = [i.strip() for i in inp]
inp = [i.split(" ") for i in inp]

contributors = int(inp[0][0])
projects = int(inp[0][1])
inp.pop(0)

users = []
skills = {}
sortedskills = {}
projectskills = {}
projectlist = []
totalDays = []
score = []
due = []

assignconprojects = {}

" Role : "


def getContributors():
    global sortedskills, contributors, projects, users, skills, projectskills, projectlist, totalDays, score, due, assignconprojects
    for i in range(contributors):
        users.append(inp[0][0])
        skill = []
        for j in range(int(inp[0][1])):
            j += 1
            skill.append(inp[j])
        skills[users[i]] = skill
        temp = int(inp[0][1])
        for i in range(temp + 1):
            inp.pop(0)


def getProjects():
    for i in range(projects):
        totalDays.append(int(inp[0][1]))
        score.append(int(inp[0][2]))
        due.append(int(inp[0][3]))
        roles = []
        for i in range(int(inp[0][4])):
            i += 1
            roles.append([inp[i][0], int(inp[i][1])])
        projectlist.append(inp[0][0])
        projectskills[inp[0][0]] = roles
        for i in range(1 + int(inp[0][4])):
            inp.pop(0)


def sortskills():
    for i in skills.keys():
        for j in skills.get(i):
            prev = sortedskills.get(j[0], [])
            prev.append(i)
            sortedskills[j[0]] = prev


def assignContributors():
    for i in projectlist:
        reqSkills = projectskills.get(i)
        for rskill in reqSkills:
            lvl = rskill[1]
            elcons = sortedskills.get(rskill[0])
            for k in elcons:
                for j in skills.get(k):
                    if j[0] == rskill[0] and int(j[1]) >= lvl:
                        temp = assignconprojects.get(i, [])
                        if k not in temp:
                            temp.append(k)
                        assignconprojects[i] = temp
                        if temp != assignconprojects.get(i, []):
                            break
                if temp != assignconprojects.get(i, []):
                    break
        if assignconprojects.get(i):
            if len(assignconprojects.get(i, [])) != len(reqSkills):
                assignconprojects.pop(i)


def writeOutput():
    file = open("output/" + fName, "w+")
    p = [i for i in assignconprojects.keys()]
    p = [i + "\n" for i in p]
    nop = str(len(p)) + "\n"
    ass = [" ".join(i) for i in assignconprojects.values()]
    ass = [i + "\n" for i in ass]
    ass[-1] = ass[-1].strip()
    total = [nop]
    for i, j in zip(p, ass):
        total.append(i)
        total.append(j)

    file.writelines(total)

    file.close()


if __name__ == "__main__":
    system("clear")
    getContributors()
    getProjects()
    sortskills()
    assignContributors()
    writeOutput()

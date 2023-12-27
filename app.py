from index import ind

with open("assets/about.log") as f:
    lines = f.readlines()   
with open("assets/login.log") as k:
    line = k.readlines()
lt = line[-1].split(" | ")
user = lt[-1]
name = ''
pri = ''
for a in lines:
    cred = a.split(" | ")
    if cred[0] == user:
        name += cred[1]
        pri += cred[-1]
        break
    else:
        pass
ind(name, user, pri)
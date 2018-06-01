e = open('export.txt', 'w')
f = open('index.html', 'r')
a = 0
f = f.readlines()
export = ""
while a != len(f):
    f[a] = f[a].replace("\n", "")
    export += 'page += ' + '"' + f[a] + '"' + ';' +'\n'
    a += 1
print(export)
e.write(export)
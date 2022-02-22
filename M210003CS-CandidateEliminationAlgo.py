import pandas as pd

data=[]

A = pd.read_csv(r"C:\\Users\\ksake\\2nd Sem ML Lab Code\\ACRegulation.csv", nrows = 8)

for index, rows in A.iterrows():
    data.append(list(rows))

s = data[0][:-1]
print(s)
g = [['?' for i in range(len(s))] for j in range(len(s))]

for i in data:
    if i[-1] == "Yes":
        for j in range(len(s)):
            if i[j] != s[j]:
                s[j] = '?'
                g[j][j] = '?'
    elif i[-1] == "No":
        for j in range(len(s)):
            if i[j] != s[j]:
                g[j][j] = s[j]
            else:
                g[j][j] = "?"

    print("\Iteration Number : ", data.index(i) + 1)
    print(s)
    print(g)

gh = []
for i in g:
    for j in i:
        if j != '?':
            gh.append(i)
            break
print("\nFinal specific hypothesis : ", s)

print("\nFinal general hypothesis : ", gh)
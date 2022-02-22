import pandas as pd

a=[]

A = pd.read_csv(r"C:\\Users\\ksake\\2nd Sem ML Lab Code\\ACRegulation.csv", nrows = 6)

for index, rows in A.iterrows():
    a.append(list(rows))

ncols = len(a[0])-1

print("\n The initial h_val is : ", end = " ")
h_val = ['0']*ncols
print(h_val)

for i in range(0, len(a)):
    if a[i][ncols] == 'Yes':
        for j in range(0, ncols):
            if h_val[j] == '0' or h_val[j] == a[i][j]:
                h_val[j] = a[i][j]
            else:
                h_val[j] = '?'
    print("\n The h_val for the row {} is :" .format(i+1),h_val)

print("\n\n The Most specific hypothesis for the training instance is :")
print(h_val)
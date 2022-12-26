import pandas as pd
import pyperclip as pc

data = pd.read_csv(r'D://Data//Tech_Upgrade//Friends_Report.csv')
df = pd.DataFrame(data)

print(df)

lis = df.Account_Email.to_list()
e = []
st = ''

for i in range(0,1000):
    if 'twdev'+str(i)+'@gmail.com' not in lis:
        e.append('twdev'+str(i)+'@gmail.com')
        st += 'twdev'+str(i)+'@gmail.com\n'


Input = input('Do you want to copy the result?\n1 OR Y For Yes\
                \nN or anthing else for No.')

if Input == 'Y' or '1':
    pc.copy(st)

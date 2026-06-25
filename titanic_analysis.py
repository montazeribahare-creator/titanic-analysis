import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

filtered = df[(df['Sex'] == 'female') & (df['Pclass'] == 3) & (df['Survived'] == 0)]

print("تعداد زنان کلاس ۳ که فوت کردند:", len(filtered))
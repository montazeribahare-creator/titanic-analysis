import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# تعداد نجات‌یافتگان بر اساس جنسیت
survived_by_sex = df[df['Survived'] == 1]['Sex'].value_counts()

# رسم نمودار میله‌ای
survived_by_sex.plot(kind='bar', color=['blue', 'pink'])
plt.title('تعداد نجات‌یافتگان تایتانیک بر اساس جنسیت')
plt.xlabel('جنسیت')
plt.ylabel('تعداد')
plt.show()
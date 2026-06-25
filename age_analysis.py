import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ایجاد ستون جدید برای گروه‌های سنی
df['Age_Group'] = df['Age'].apply(lambda x: 'کودک (زیر ۱۸)' if x < 18 else ('بزرگسال (۱۸+)' if x >= 18 else 'نامشخص'))

# تعداد نجات‌یافتگان بر اساس گروه سنی
survived_by_age = df[df['Survived'] == 1]['Age_Group'].value_counts()

# رسم نمودار
survived_by_age.plot(kind='bar', color=['green', 'blue'])
plt.title('تعداد نجات‌یافتگان تایتانیک بر اساس گروه سنی')
plt.xlabel('گروه سنی')
plt.ylabel('تعداد نجات‌یافتگان')
plt.xticks(rotation=0)
plt.show()

print("تعداد نجات‌یافتگان در هر گروه سنی:")
print(survived_by_age)
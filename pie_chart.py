import pandas as pd
import matplotlib.pyplot as plt

# خواندن دیتاست
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ================== نمودار دایره‌ای جنسیت ==================
survived_by_sex = df[df['Survived'] == 1]['Sex'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(survived_by_sex, labels=survived_by_sex.index, autopct='%1.1f%%', 
        colors=['lightblue', 'pink'], startangle=90)
plt.title('درصد نجات‌یافتگان تایتانیک بر اساس جنسیت')
plt.show()

# ================== نمودار دایره‌ای کلاس مسافرتی ==================
survived_by_class = df[df['Survived'] == 1]['Pclass'].value_counts().sort_index()

plt.figure(figsize=(6,6))
plt.pie(survived_by_class, labels=['کلاس ۱', 'کلاس ۲', 'کلاس ۳'], 
        autopct='%1.1f%%', colors=['gold', 'silver', 'brown'], startangle=90)
plt.title('درصد نجات‌یافتگان تایتانیک بر اساس کلاس مسافرتی')
plt.show()

# ================== چاپ اعداد دقیق ==================
print("=== اعداد دقیق نجات‌یافتگان ===")
print("\nبر اساس جنسیت:")
print(survived_by_sex)
print("\nبر اساس کلاس مسافرتی:")
print(survived_by_class)
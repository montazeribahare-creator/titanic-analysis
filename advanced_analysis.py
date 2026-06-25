import pandas as pd
import matplotlib.pyplot as plt

# خواندن دیتاست
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# ایجاد ستون گروه سنی
df['Age_Group'] = df['Age'].apply(lambda x: 'کودک' if x < 18 else ('بزرگسال' if x >= 18 else 'نامشخص'))

# ================== تحلیل ترکیبی: کلاس + جنسیت + سن ==================

# ۱. تعداد کل مسافران در هر گروه
total_passengers = df.groupby(['Pclass', 'Sex', 'Age_Group']).size().unstack(fill_value=0)

# ۲. تعداد نجات‌یافتگان در هر گروه
survived_passengers = df[df['Survived'] == 1].groupby(['Pclass', 'Sex', 'Age_Group']).size().unstack(fill_value=0)

# ۳. درصد نجات در هر گروه
survival_rate = (survived_passengers / total_passengers * 100).round(1)

print("=== تعداد کل مسافران در هر کلاس، جنسیت و گروه سنی ===")
print(total_passengers)
print("\n=== تعداد نجات‌یافتگان در هر گروه ===")
print(survived_passengers)
print("\n=== درصد نجات در هر گروه ===")
print(survival_rate)

# ================== رسم نمودار مقایسه‌ای ==================

# نمودار میله‌ای برای درصد نجات زنان در هر کلاس
plt.figure(figsize=(10, 6))
women_survival = survival_rate['بزرگسال'].loc[:, 'female']  # درصد نجات زنان بزرگسال در هر کلاس
plt.bar(['کلاس ۱', 'کلاس ۲', 'کلاس ۳'], women_survival, color=['gold', 'silver', 'brown'])
plt.title('درصد نجات زنان بزرگسال در هر کلاس مسافرتی')
plt.xlabel('کلاس مسافرتی')
plt.ylabel('درصد نجات')
plt.ylim(0, 100)
for i, v in enumerate(women_survival):
    plt.text(i, v + 2, f'{v}%', ha='center')
plt.show()

# نمودار میله‌ای برای درصد نجات کودکان در هر کلاس
plt.figure(figsize=(10, 6))
children_survival = survival_rate['کودک'].loc[:, 'female'] + survival_rate['کودک'].loc[:, 'male']  # جمع کودکان (پسر و دختر)
plt.bar(['کلاس ۱', 'کلاس ۲', 'کلاس ۳'], children_survival, color=['gold', 'silver', 'brown'])
plt.title('درصد نجات کودکان در هر کلاس مسافرتی')
plt.xlabel('کلاس مسافرتی')
plt.ylabel('درصد نجات')
plt.ylim(0, 100)
for i, v in enumerate(children_survival):
    plt.text(i, v + 2, f'{v}%', ha='center')
plt.show()
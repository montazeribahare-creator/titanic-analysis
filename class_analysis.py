import pandas as pd
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# تعداد نجات‌یافتگان بر اساس کلاس
survived_by_class = df[df['Survived'] == 1]['Pclass'].value_counts().sort_index()

# رسم نمودار
survived_by_class.plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title('تعداد نجات‌یافتگان تایتانیک بر اساس کلاس مسافرتی')
plt.xlabel('کلاس مسافرتی')
plt.ylabel('تعداد نجات‌یافتگان')
plt.xticks(rotation=0)
plt.show()

# چاپ اعداد دقیق
print("تعداد نجات‌یافتگان در هر کلاس:")
print(survived_by_class)
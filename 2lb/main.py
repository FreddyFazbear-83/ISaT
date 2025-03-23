import xml.etree.ElementTree as ET
import json
import random
import matplotlib.pyplot as plt
import pandas as pd

tree = ET.parse('feed.xml')
root = tree.getroot()

sales_data = {}
months = [f'Месяц {i+1}' for i in range(12)]


for offer in root.findall('.//offer'):
    name = offer.find('name').text
    sales = [random.randint(0, 100) for _ in range(12)]
    sales_data[name] = sales


shop_name = root.find('.//shop/name').text
json_data = {
    "shop": {
        "name": shop_name,
        "sales": sales_data
    }
}

with open('cat.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=4)

df = pd.DataFrame(sales_data, index=months)

df.plot(kind='bar', figsize=(12, 6))
plt.title('Динамика продаж диванов по месяцам')
plt.xlabel('Месяцы')
plt.ylabel('Количество продаж')
plt.xticks(rotation=45)
plt.legend(title='Модели диванов')
plt.tight_layout()
plt.show()

print(df)

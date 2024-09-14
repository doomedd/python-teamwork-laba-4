# Вихідний текст обсягом до 100 слів
text = "Pudge is a well-known hero in Dota 2, famous for his (Meat Hook) ability, which pulls enemies from a distance. He is a tanky character with high health, making him difficult to kill. Pudge also uses (Rot) to deal damage to nearby enemies, and his (Dismember) can disable and damage opponents, making him a feared presence in the game."

# 1. Функція len() для підрахунку кількості символів у тексті
length_of_text = len(text)
print(f"Length of the text: {length_of_text} characters")

# 2. Функція lower() для перетворення тексту у нижній регістр
lowercase_text = text.lower()
print(f"Text in lowercase: {lowercase_text}")

# 3. Функція count() для підрахунку кількості слова 'is' у тексті
count_is = text.count('is')
print(f"The word 'is' appears {count_is} times in the text")

# Руденко Данііл (КН-33/2), рядки 16-33.
# 4. # Функція count() для підрахунку кількості слова 'his' у тексті.

count_his = text.count('his')
print(f"The word 'his' appears {count_his} times in the text")

# 5. Функція split() для розділення тексту на окремі слова.

words = text.split()
print(f"List of words: {words}")

# 6. Функція find() для знаходження індексу першого входження певного слова.

index_of_meat_hook = text.find("Meat Hook")
print(f"Index of 'Meat Hook': {index_of_meat_hook}")

# Ці функції надають різні можливості для роботи з текстом і відповідають вимогам щодо новизни двох функцій.
# Передаю далі завдання Вікторії Чорномаз - використати три функції, дві з яких будуть відрізнятися від попередніх, наприклад startswith() та endswith().
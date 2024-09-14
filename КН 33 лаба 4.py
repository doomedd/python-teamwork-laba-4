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

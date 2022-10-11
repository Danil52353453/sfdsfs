lst="Напишите программу, удаляющую из текста все слова, содержащие ""абв""."
text=list(filter(lambda x: "абв" not in x ,lst.split()))
result = " ".join(text)
print(f"Исходный текст:  {lst}")
print(f"Готовый текст :  {result}")

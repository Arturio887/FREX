while True:
    try:
        # Запитуємо користувача про дані вкладу
        сума_депозиту = float(input("Введіть суму депозиту: "))
        відсоткова_ставка = float(input("Введіть річну відсоткову ставку (у відсотках): "))
        тривалість_депозиту_місяці = int(input("Введіть тривалість депозиту у місяцях: "))

        # Перевірка валідності даних
        if сума_депозиту <= 0 or відсоткова_ставка < 0 or тривалість_депозиту_місяці <= 0:
            raise ValueError("Введені дані некоректні. Будь ласка, введіть додатні значення.")

        break  # Виходимо з циклу, якщо дані є валідними
    except ValueError as e:
        print(f"Помилка: {e}")
        continue

# Перетворюємо річну відсоткову ставку в місячну
місячна_ставка = (відсоткова_ставка / 100) / 12

# Ініціалізуємо змінні для ведення обліку
загальна_сума = сума_депозиту

# Виводимо заголовок
print("Місяць | Загальна сума | Нараховані відсотки")

# Обчислюємо і виводимо дані для кожного місяця
for місяць in range(1, тривалість_депозиту_місяці + 1):
    # Обчислюємо нараховані відсотки за цей місяць
    нараховані_відсотки = загальна_сума * місячна_ставка
    
    # Оновлюємо загальну суму
    загальна_сума += нараховані_відсотки
    
    # Виводимо дані для поточного місяця
    print(f"{місяць:6} | {загальна_сума:13.2f} | {нараховані_відсотки:15.2f}")

0


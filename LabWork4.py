class Smartphone:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def years_since_release(self, current_year):
        return current_year - self.release_year

class Store:
    def __init__(self):
        self.smartphones = []  # Створення пустого списку

    def add_smartphone(self, smartphone):
        self.smartphones.append(smartphone)

    def remove_smartphone(self, smartphone):
        if smartphone in self.smartphones:
            self.smartphones.remove(smartphone)
        else:
            print(f"{smartphone.name} не продається.")

    def get_smartphones_released_after_year(self, year):
        return [smartphone for smartphone in self.smartphones if smartphone.release_year > year]

    def list_all_smartphones(self):
        if self.smartphones:
            print("Список доступних смартфонів:")
            for smartphone in self.smartphones:
                print(f"{smartphone.name} ({smartphone.release_year})")
        else:
            print("Магазин порожній.")

if __name__ == "__main__":
    store = Store()

    while True:
        print("\nМеню:")
        print("1. Додати смартфон")
        print("2. Видалити смартфон")
        print("3. Вивести смартфони, випущені після певного року")
        print("4. Вивести список усіх смартфонів")
        print("5. Вийти з програми")

        choice = input("Виберіть опцію: ")

        if choice == "1":
            name = input("Введіть назву смартфону: ")
            while True:
                release_year = input("Введіть рік випуску смартфону: ")
                if release_year.isdigit():
                    release_year = int(release_year)
                    break
                else:
                    print("Помилка: Рік повинен бути цілим числом.")

            smartphone = Smartphone(name, release_year)
            store.add_smartphone(smartphone)
            print(f"Смартфон {name} додано в магазин.")

        elif choice == "2":
            name = input("Введіть назву смартфону для видалення: ")
            for smartphone in store.smartphones:
                if smartphone.name == name:
                    store.remove_smartphone(smartphone)
                    break
            else:
                print(f"{name} не знайдено в магазині.")

        elif choice == "3":
            while True:
                try:
                    year_filter = int(input("Введіть рік фільтрації: "))
                    filtered_smartphones = store.get_smartphones_released_after_year(year_filter)
                    print(f"Смартфони, випущені після {year_filter} року:")
                    for smartphone in filtered_smartphones:
                        print(f"{smartphone.name} ({smartphone.release_year}) - {smartphone.years_since_release(2023)} років з випуску")
                    break
                except ValueError:
                    print("Помилка: Рік повинен бути цілим числом.")

        elif choice == "4":
            store.list_all_smartphones()

        elif choice == "5":
            print("Програма завершена.")
            break

        else:
            print("Помилка: Невірний вибір. Виберіть опцію від 1 до 5.")

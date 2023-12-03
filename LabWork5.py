total_price = 0.0
file = open('shop.txt', 'r', encoding='utf-8')

for line in file:
    stripped_line = line.strip()
    print(stripped_line)

    try:
        price = float(stripped_line.split(' -- ')[1])
        total_price += price
    except:
        print(f"Некоректно вказана ціна: {stripped_line}")

file.close()

print(f"Сума: {total_price:.2f}")

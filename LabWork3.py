import random


def малюнок_масив(rows, cols):
    масив = [[random.randint(1, 99) for _ in range(cols)] for _ in range(rows)]
    return масив


def print_масив(масив, значення):
    for row in масив:
        for value in row:
            if value > значення:
                print(f"*{value:02d}*", end="  ")
            else:
                print(f"-{value:02d}-", end="  ")
        print()


значення = int(input("Введіть значення: "))


rows, cols = 5, 5  
масив = малюнок_масив(rows, cols)


print("\nМасив з виділеними значеннями:")
print_масив(масив, значення)

    
    
    
    



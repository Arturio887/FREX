
#Чилік Артур КІ-1

file_name = input("Введіть ім'я текстового файлу: ")
word = input("Введіть слово для пошуку: ")

print(f"Читається файл: {file_name}")

#UTF-8 для читання укр символів
with open(file_name, 'r', encoding='utf-8') as file:
    
    file_content = file.read()

    abzatss = file_content.split('\n\n')

    words = 0

    
    for abzats in abzatss:
        
        if word.lower() in abzats.lower():
            
            words += abzats.lower().count(word.lower())
            
            highlighted_word = abzats.replace(word, word.upper())
            print(highlighted_word)
            print('*' * 20)  

    
    print(f"Знайдено {words} слова(слів)")


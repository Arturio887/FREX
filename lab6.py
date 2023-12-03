#Підключення модулів
from watchdog.observers import Observer
import os
import time
from watchdog.events import FileSystemEventHandler

# Клас для відслідковування змін
class Handler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.quit_flag = False  # Прапорець для виходу q

    def on_created(self, event):  # для тільки створених файлів
        if not event.is_directory and not self.quit_flag:
            filename = os.path.basename(event.src_path)
            src_path = os.path.join(folder_track, filename)
            dest_path = os.path.join(folder_dest, filename)

            if not os.path.exists(dest_path):
                os.rename(src_path, dest_path)
                print(f"Файл {filename} переміщено до {folder_dest}")

# Шляхи до папок
folder_track = '/Users/Asus/Desktop'
folder_dest = '/Users/Asus/Desktop/downloads'

#запуск всього для відслідковування
handle = Handler()
observer = Observer()
observer.schedule(handle, folder_track, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10) #кожні 10 мілісекунд
        user_input = input("Введіть 'q' для завершення програми: ")
        if user_input.lower() == 'q':
            handle.quit_flag = True  
            break
except KeyboardInterrupt:
    observer.stop()

observer.join()







            
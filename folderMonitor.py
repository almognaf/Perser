import time
import xlsxtojson
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


# TODO: Make event handle parsing,Check for edge cases


class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        file_name = str(event.src_path)
        xlsxtojson.xlsx_to_json(file_name)
        return print("Created")
        # http request with result's json


path = 'C:/Users/alnaf/Perser/Reports'
print(path)
event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

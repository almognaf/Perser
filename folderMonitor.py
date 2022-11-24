import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


# TODO: Make event handle parsing,Check for edge cases
from Main_Perser import *


class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        file_name = str(event.src_path)
        initiate = MainPerser(file_name)
        print(initiate.filename)


path = 'C:/Users/alnaf/Perser/perses-main-data-new CEF/data/test'
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

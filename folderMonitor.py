import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler
import fileNameParse
from datetime import datetime
import parsecef

#TODO: Make event handle parsing,Check for edge cases

class MyEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        fileName = str(event.src_path)
        name = fileName.split('\\')
        # TODO: Check if name is valid
        fixedName = (name[4])[0:len(name[4])-1]
        print(fixedName)
        fileDic = fileNameParse.listDir(fixedName)
        print(fileDic)








path = sys.argv[1] if len(sys.argv) > 1 else '.'
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
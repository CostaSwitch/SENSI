import time
import os
import requests
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from queue import Queue
from threading import Thread

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, queue):
        self.queue = queue
        self.file_path = "/var/log/suricata/fast.log"

        # Try to get the size of the log file.
        try:
            self.last_position = os.stat(self.file_path).st_size
        except Exception:
            self.last_position = 0

    def on_modified(self, event):
        if not event.is_directory and event.src_path.endswith(self.file_path): 
            new_position = os.stat(self.file_path).st_size

            with open(self.file_path, 'r') as file:
                file.seek(self.last_position)
                new_content = file.read(new_position - self.last_position)
                self.last_position = new_position
                
                new_lines = new_content.split("\n")

                for new_line in new_lines:
                    self.queue.put(new_line)

class AlertSender(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        self.chat_id = "-929537863"
        self.bot_token = "6377944402:AAHC4nC5KNLVu_qm0z9AjzYDEoMGkQgTVsI"

    def run(self):
        while True:
            message = self.queue.get()
            if message:
                self.send_message(message)

    def send_message(self, message):
        data = {"chat_id": self.chat_id, "text": message}
        while True:
            try:
                response = requests.post(f"https://api.telegram.org/bot{self.bot_token}/sendMessage", data=data)
                response.raise_for_status()
                break
            except:
                time.sleep(3.5)
                break

if __name__ == "__main__":
    path = "/var/log/suricata"
    queue = Queue()
    event_handler = LogFileHandler(queue)
    alert_sender = AlertSender(queue)
    alert_sender.start()

    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        observer.join()

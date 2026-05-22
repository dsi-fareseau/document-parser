from pathlib import Path
import time

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


WATCH_DIR = Path("./incoming")


class IncomingHandler(FileSystemEventHandler):

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = Path(event.src_path)

        print(f"[NOUVEAU FICHIER] {file_path.name}")


observer = Observer()

observer.schedule(
    IncomingHandler(),
    str(WATCH_DIR),
    recursive=False
)

observer.start()

print("Watchdog démarré sur incoming/")


try:

    while True:
        time.sleep(1)

except KeyboardInterrupt:

    observer.stop()

observer.join()
from calc.history.calculations import Calculations
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division
import pandas as pd
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Watcher:
    DIRECTORY_TO_WATCH = "data/input"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        print("Started observer.")
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            self.observer.join()
            print("Exiting.")
        except:
            self.observer.stop()
            self.observer.join()
            print("Error")


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Take any action here when a file is first created.
            print("Received created event - %s." % event.src_path)
            dataframe = pd.read_csv(event.src_path)
            if dataframe.columns[0] == 'operation':
                for index, row_data in dataframe.iterrows():
                    if row_data['operation'] == '+':
                        values = []
                        for val in row_data[1:]:
                            values.append(val)
                        addition = Addition.create(tuple(values))
                        Calculations.add_calculation(addition)


        # elif event.event_type == 'modified':
            # Take any action here when a file is modified.
            # print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()

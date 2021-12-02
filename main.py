from calc.history.calculations import Calculations
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division
import pandas as pd
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

OUTPUT_FILEPATH = "data/output.txt"
DONE_DIRECTORY = "data/done/"


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
            filename = event.src_path.split('/')[-1]
            dataframe = pd.read_csv(event.src_path)
            if dataframe.columns[0] == 'operation':
                output_file = open(OUTPUT_FILEPATH, "a")
                for index, row_data in dataframe.iterrows():
                    values = []
                    for val in row_data[1:]:
                        values.append(val)
                    if row_data['operation'] == '+':
                        calculation = Addition.create(tuple(values))
                        calculation_name = "ADDITION"
                    elif row_data['operation'] == '-':
                        calculation = Subtraction.create(tuple(values))
                        calculation_name = "SUBTRACTION"
                    elif row_data['operation'] == '*':
                        calculation = Multiplication.create(tuple(values))
                        calculation_name = "MULTIPLICATION"
                    elif row_data['operation'] == '/':
                        calculation = Division.create(tuple(values))
                        calculation_name = "DIVISION"
                    else:
                        print("Invalid operation symbol.")
                        return None
                    Calculations.add_calculation(calculation)
                    output_string = "%s | %s | ROW %s | %s | %s \n" % (int(time.time()), filename, index + 1,
                                                                       calculation_name,
                                                                       Calculations.get_last_calculation_result())
                    # print(output_string)
                    output_file.write(output_string)
                output_file.close()
                shutil.move(event.src_path, DONE_DIRECTORY + filename)

        # elif event.event_type == 'modified':
        # Take any action here when a file is modified.
        # print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()

""" Main calculator app entrypoint """

import time
import shutil
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from calc.history.calculations import Calculations
from calc.operations.addition import Addition
from calc.operations.subtraction import Subtraction
from calc.operations.multiplication import Multiplication
from calc.operations.division import Division

OUTPUT_FILEPATH = "data/output.txt"
LOG_FILEPATH = "data/output.log"  # for logging errors such as divide-by-zero
DONE_DIRECTORY = "data/done/"  # where to move input files after reading


class Watcher:
    # pylint: disable=broad-except,too-few-public-methods
    """ Watches for filesystem changes in specified directory """

    DIRECTORY_TO_WATCH = "data/input"

    def __init__(self):
        """ Init """
        self.observer = Observer()

    def run(self):
        """ Runs the observer loop """
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
        except Exception as exception:
            self.observer.stop()
            self.observer.join()
            print(exception)


class Handler(FileSystemEventHandler):
    # pylint: disable=no-member,inconsistent-return-statements,consider-using-with
    """ Handles events triggered by Watcher """

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        if event.event_type == 'created':
            # Take any action here when a file is first created.
            print(f"Received created event - {event.src_path}.")
            filename = event.src_path.split('/')[-1]
            dataframe = pd.read_csv(event.src_path)
            if dataframe.columns[0] == 'operation':
                output_file = open(OUTPUT_FILEPATH, "a", encoding="utf-8")
                log_file = open(LOG_FILEPATH, "a", encoding="utf-8")
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
                    result = Calculations.get_last_calculation_result()
                    if result == "error":
                        # print("Cannot divide by zero!")
                        log_string = f"{int(time.time())} | " \
                                     f"ERROR | " \
                                     f"{filename} | " \
                                     f"ROW {index + 1} | " \
                                     f"Cannot divide by zero!\n"
                        log_file.write(log_string)
                    else:
                        output_string = f"{int(time.time())} | " \
                                        f"{filename} | " \
                                        f"ROW {index + 1} | " \
                                        f"{calculation_name} | " \
                                        f"{Calculations.get_last_calculation_result()}\n"
                        output_file.write(output_string)
                output_file.close()
                log_file.close()
                shutil.move(event.src_path, DONE_DIRECTORY + filename)
            return None

        # elif event.event_type == 'modified':
        # Take any action here when a file is modified.
        # print("Received modified event - %s." % event.src_path)


if __name__ == '__main__':
    w = Watcher()
    w.run()

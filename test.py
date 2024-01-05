import threading
import queue
import msvcrt
import time

class UserInputThread(threading.Thread):
    def __init__(self, input_queue):
        super(UserInputThread, self).__init__()
        self.input_queue = input_queue

    def run(self):
        while True:
            if msvcrt.kbhit():
                user_input = msvcrt.getch().decode('utf-8')
                self.input_queue.put(user_input)

            time.sleep(0.1)

class SimulationThread(threading.Thread):
    def __init__(self, input_queue):
        super(SimulationThread, self).__init__()
        self.input_queue = input_queue
        self.previous_input = None

    def run(self):
        while True:
            try:
                user_input = self.input_queue.get_nowait()
                self.previous_input = user_input
                print(f"Symulacja obiektu dla wartości: {self.previous_input}")
            except queue.Empty:
                print("Brak nowej wartości do symulacji")

            time.sleep(0.1)

if __name__ == "__main__":
    input_queue = queue.Queue()

    user_input_thread = UserInputThread(input_queue)
    simulation_thread = SimulationThread(input_queue)

    user_input_thread.start()
    simulation_thread.start()

    user_input_thread.join()
    simulation_thread.join()

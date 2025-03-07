import threading
import math

number = float(input())
millisecond = int(input())
def for_timer(num, millisecond):
    squared = math.sqrt(num)
    print(f"Square root of {num} after {millisecond} miliseconds is {squared}")
seconds = millisecond / 1000
timer = threading.Timer(seconds, for_timer, [number, millisecond])
timer.start()
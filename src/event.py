import threading
import time

# Create an event object
event = threading.Event()

# A thread that emits an event
def event_setter():
    time.sleep(3)  # Simulate some work
    event.set()
    print("Event is set! Other threads can continue.")

# A thread that waits for an event
def event_listener():
    print("Thread is waiting for the event to be set.")
    event.wait()  # Block until the event is set
    print("Event has been set, thread continues execution.")

def run_event():
    # Create threads
    setter_thread = threading.Thread(target=event_setter)
    listener_thread = threading.Thread(target=event_listener)
    
    # Start threads
    setter_thread.start()
    listener_thread.start()
    
    # Wait for threads to complete
    setter_thread.join()
    listener_thread.join()

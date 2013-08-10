import threading
message_lock = threading.lock()

with message_lock:
    messages.add(newmessage)

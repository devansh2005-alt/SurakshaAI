import time

def interrupt_action(seconds=8):
    print("\n⛔ Security Hold Activated")
    for i in range(seconds, 0, -1):
        print(f"Please wait... {i}", end="\r")
        time.sleep(1)
    print("\n⚠ Please re-evaluate carefully before taking action.")

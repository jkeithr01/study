import os
import sys
import uuid
print(__name__)

def send_query(query: str = '0-0-0-destruct-0'):
    print(f'Issuing query {query}')

def connect(threadid: str = 'abc-easy-as-123'):
    print(f'Thread ID {threadid} connecting')

def create_thread(thread_group: str):
    print(f"Creating a thread")
    # code to spawn a single thread here - generating a uuid for now
    threadid = uuid.uuid4()
    # add thread to a thread group
    print(f"Adding thread {threadid} to thread group {thread_group}")

def doStuff():
    print("Ran main() and called doStuff()")

def create_thread_group(tg: str = None):
    return f"Thread group {tg} created."

def main():
    doStuff()
    
    tg1 = create_thread_group(f"tg1")
    print(f"{tg1}")

    connect()
    create_thread(f"tg1")
    create_thread(f"tg1")
    create_thread(f"tg2")
    create_thread(f"tg1")
    create_thread(f"tg2")
    send_query(query='1-1a')
    send_query(query='1-1a-2b')
    send_query(query='1b-2b-3')
    send_query()


if __name__ == "__main__":
    main()
else:
    sys.exit("Program is not a loadable module. Run from command line using python <thread_plate.py>")

from multiprocessing import Process, Queue, cpu_count
import random

def client(id, work_queue, res_queue, count=2):
    for i in range(count):
        work = random.randint(1, 10)
        print(f"Client {id} processing work: {work}")
        work_queue.put((id, work))

        res_id, work, res = res_queue.get()
        print(f"Client {id} received result: {res} for work: {work}")

    print(f"Client {id} finished.")

def server(work_queue, res_queue):
    while True:
        item = work_queue.get()
        if item is None: # checking if signaled to stop
            break
        client_id, work = item
        print(f"Server processing work: {work} from client {client_id}")
        result = work * work  # Example processing
        res_queue[client_id].put((client_id, work, result))

if __name__ == "__main__":
    count = cpu_count()
    work_queue = Queue()
    res_queue = [Queue() for _ in range(count-1)]
    
    p_server = Process(target=server, args=(work_queue,res_queue))
    p_server.start()

    clients = []
    for i in range(count-1):
        p = Process(target=client, args=(i, work_queue, res_queue[i]))
        clients.append(p)
        print("Starting client", i)
        p.start()

    for p in clients:
        p.join()

    work_queue.put(None)  # Signal the server to stop
    p_server.join()

    print("All clients have finished.")


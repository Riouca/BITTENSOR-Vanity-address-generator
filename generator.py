from substrateinterface import Keypair
import multiprocessing
import time

def generate_and_check_address(queue, counter):
    while True:
        keypair = Keypair.generate_mnemonic(12)
        keypair = Keypair.create_from_mnemonic(keypair)
        if is_valid_address(keypair.ss58_address):
            print(f"Valid address found ! -> {keypair.ss58_address}")
            queue.put((keypair.ss58_address, keypair.mnemonic))
        with counter.get_lock():
            counter.value += 1

def is_valid_address(address):
    valid_prefixes = ["5coffee","5dude","5etc"]
    for prefix in valid_prefixes:
        if address.lower().startswith(prefix):
            return True
    return False

def write_to_file(queue):
    while True:
        address, mnemonic = queue.get()
        with open('result.txt', 'a') as f:
            f.write(f"Address: {address}\n")
            f.write(f"Mnemonic: {mnemonic}\n\n")

def display_hash_rate(counter):
    while True:
        start_count = counter.value
        time.sleep(10)
        end_count = counter.value
        hash_rate = (end_count - start_count) / 10
        print(f"Address generation speed : {hash_rate:.2f} addresses/s")

if __name__ == '__main__':
    print("Up and running, speed updates every 10 seconds")
    queue = multiprocessing.Queue()
    counter = multiprocessing.Value('i', 0)
    
    writer_process = multiprocessing.Process(target=write_to_file, args=(queue,))
    writer_process.start()
    
    hash_rate_process = multiprocessing.Process(target=display_hash_rate, args=(counter,))
    hash_rate_process.start()

    num_processes = multiprocessing.cpu_count()
    processes = []
    for _ in range(num_processes):
        p = multiprocessing.Process(target=generate_and_check_address, args=(queue, counter))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()
    writer_process.join()
    hash_rate_process.join()

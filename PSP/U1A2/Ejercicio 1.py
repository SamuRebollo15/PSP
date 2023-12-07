"""Exercise 1: Using the multiprocessing module, write a simple python program as follows:

Create a pool of workers to run parallel tasks.
The pool size should be the number of CPU cores available on your node minus 1 (8cores > pool of 7 workers).
Write a function to be running in parallel, call it my_id. The function should receive as input the task id. When called, the function will print to the screen a message in the form: “Hi, I’m worker ID (with PID)” Where ID should be replaced with the task number assigned to the worker and PID with the process ID of the running worker.
Run tasks in parallel using the map function, for a total of tasks equal to twice the number of CPU cores in your node."""


# Importing modules
import multiprocessing
import os


def my_id(task_id):
    process_id = os.getpid()
    print(f"Hi, I'm worker {task_id} (with PID {process_id})")


def main():
   
    num_cores = multiprocessing.cpu_count()
    pool_size = num_cores - 1

 
    with multiprocessing.Pool(processes=pool_size) as pool:
        task_ids = list(range(1, 2 * num_cores + 1))
        pool.map(my_id, task_ids)

if __name__ == "__main__":
    main()


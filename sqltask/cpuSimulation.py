import heapq
import sys

def run_cpu_simulation():
    priority_queue=[]
    job_counter=0

    current_job=None
    remaining_time=0
    time_slice=1

    print("cpu Simulation")

    while True:
        try:
            command = input(f"slice {time_slice} enter coimmand:").strip()
            if command.lower()=='exit':
                break
        except(IOError,KeyboardInterrupt):
            break

        if command.startswith("add job"):
            try:
                parts= command.split()
                name=parts[2]
                length=int(parts[5])
                priority=int(parts[8])

                heapq.heappush(priority_queue,(priority,job_counter,name,length))
                job_counter+=1
            except (IndexError,ValueError):
                print("invalid command")

        if current_job is None and priority_queue:
            priority,_,name,length=heapq.heappop(priority_queue)
            current_job=name
            remaining_time=length
        if current_job is not None:
            print(f"cpu running : task:{current_job}  (Remaining time:{remaining_time})")
            remaining_time-=1

            if remaining_time<=0:
                print(f"task {current_job} comppleted")
                current_job=None
        else:
            print("cpu is idle")
        time_slice+=1

if __name__ == "__main__":
    run_cpu_simulation()
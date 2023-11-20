def sjf(process_list):
    # declaring stuff to display our answer
    completed_process = {}
    gantt_chart = []
    
    # setting time to 0 initially
    t = 0
    
    # running loop till all processes are serviced
    while process_list != []:
        # finding out all the available processes in that time interval
        available = []
        for process in process_list:
            arrival_time = process[1]
            if arrival_time <= t:
                available.append(process)
        
        # before that let's address the boundary condition
        if available == []:
            gantt_chart.append(("Idle", t))
            t += 1
            continue
        else:
            available.sort()
            # this is the process with the lowest burst time
            process = available[0]
            bt, at, pname = process
            t += bt
            gantt_chart.append((pname, t))
            process_list.remove(process)
            ct = t
            tt = ct - at
            wt = tt - bt
            completed_process[pname] = {'Arrival Time': at, 'Burst Time': bt, 'Completion Time': ct, 'Turnaround Time': tt, 'Waiting Time': wt}
    
    # Print Gantt Chart
    print("Gantt Chart:")
    for entry in gantt_chart:
        print(f"| {entry[0]}", end=" ")
    print("| Done\n" + "-" * 50)
    
    # Print Process Details Table
    print("\nProcess Details:")
    print("| {:<10} | {:<15} | {:<10} | {:<18} | {:<15} | {:<15} |".format("Process", "Arrival Time", "Burst Time", "Completion Time", "Turnaround Time", "Waiting Time"))
    print("-" * 80)
    total_turnaround_time = 0
    total_waiting_time = 0
    for pname, details in completed_process.items():
        print("| {:<10} | {:<15} | {:<10} | {:<18} | {:<15} | {:<15} |".format(
            pname, details['Arrival Time'], details['Burst Time'], details['Completion Time'], details['Turnaround Time'], details['Waiting Time']))
        total_turnaround_time += details['Turnaround Time']
        total_waiting_time += details['Waiting Time']
    print("-" * 80)
    
    # Print Average Turnaround Time and Waiting Time
    num_processes = len(completed_process)
    avg_turnaround_time = total_turnaround_time / num_processes
    avg_waiting_time = total_waiting_time / num_processes
    print(f"\nAverage Turnaround Time: {avg_turnaround_time:.2f}")
    print(f"Average Waiting Time: {avg_waiting_time:.2f}")

# Example usage:
process_list = [[4, 1, "p1"], [2, 2, "p2"], [10, 3, "p3"]]
sjf(process_list)

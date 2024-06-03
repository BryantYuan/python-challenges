total_tasks = int(input())
tasks = [] # How long each task takes. Index is task, Value is time
time1 = 0 # The time it takes to do all tasks(1)
time2 = 0 # The time it takes to do all the tasks(2)

for i in range(total_tasks):
    tasks.append(int(input()))

tasks.sort() # We want to work with the two most time-consuming tasks

leftover_time = 0 # This is the time leftover after someone has done the faster task.
while tasks:
    task1 = tasks.pop() # Get the most time-consuming tasks
    if len(tasks) > 0:
        task2 = tasks.pop()
    else:
        task2 = 0

    if time1 > time2:
        time1 += task2 # Give the less to the more time spent one.
        time2 += task1
    else:
        time1 += task1
        time2 += task2

print(max(time1, time2))

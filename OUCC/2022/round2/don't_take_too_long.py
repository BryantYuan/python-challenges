total_tasks = int(input())
tasks = []  # How long each task takes. Index is task, Value is time
time1 = 0  # The time it takes to do all tasks(1)
time2 = 0  # The time it takes to do all the tasks(2)

for i in range(total_tasks):
    tasks.append(int(input()))

tasks.sort()  # We want to work with the most time-consuming task one at a time.

while tasks:
    cur_task = tasks.pop()  # Get the most time-consuming task

    if time1 > time2:
        time2 += cur_task
    else:
        time1 += cur_task

print(max(time1, time2))

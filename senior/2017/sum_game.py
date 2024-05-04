season_days = int(input())
swifts = input().split(' ')
semaphores = input().split(' ')
swifts_runs = 0
semaphores_runs = 0
same_days = 0
for i in range(season_days):
    swifts_runs += int(swifts[i])
    semaphores_runs += int(semaphores[i])
    if swifts_runs == semaphores_runs:
        same_days = i + 1

print(same_days)

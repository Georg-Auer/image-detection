

from datetime import datetime, timedelta
interval_minutes = 1
moving_time = 6
experiment_positions = [[0,0,0], [1,1,1], [2,2,2], [1,1,1], [2,2,2], [1,1,1], [2,2,2], [1,1,1], [2,2,2], [1,1,1], [2,2,2]]
schedule_start = datetime.today()
print(schedule_start)
task_seperation_increase = moving_time+1
task_seperation = 1
print(f"Task seperation increase time is assumed {task_seperation_increase} seconds") 
print(f"Task seperation time is assumed {task_seperation} seconds") 
for xyz_position in experiment_positions: 
    print(xyz_position)
    schedule_time_movement = schedule_start + timedelta(seconds=task_seperation)
    schedule_time_picture = schedule_start + timedelta(seconds=moving_time+task_seperation)
    # self.scheduler.add_job(func=motor_task_creator, trigger='date', run_date=schedule_time_movement, args=[xyz_position], id='move_start'+str(xyz_position))
    print("motor job")
    print(f"created moving job {xyz_position} running at {schedule_time_movement}")
    # self.scheduler.add_job(func=picture_task_creator, trigger='date', run_date=schedule_time_picture, args=[xyz_position], id='picture_start'+str(xyz_position))
    print("picture job")
    print(f"created picture job {xyz_position} running at {schedule_time_picture}")
    task_seperation = task_seperation + task_seperation_increase
    print(f"Task seperation increase time is {task_seperation} seconds")

# last scheduled picture time is stored
try:
    # if no schedule_time_picture is set, there might be 0 positions
    minimal_interval_minutes = schedule_time_picture
except:
    print("No Positions to start, stopping experiment")
    # self.stop_experiment()
    # return

idle_time = minimal_interval_minutes-schedule_start
print(f"Time for one experiment: {idle_time}")
# print(f"Set interval time: {interval_minutes}")
print(f"Set interval time in minutes: {timedelta(minutes=interval_minutes)}")
if(idle_time <= timedelta(minutes=interval_minutes)):
    print(f"Schedule is possible, there is time left in the schedule ({timedelta(minutes=interval_minutes)-idle_time})")
    experiment_running = True
else:
    print(f"Schedule is impossible: {idle_time-timedelta(minutes=interval_minutes)} missing; stopping and rescheduling in progress")
    # stop_experiment()
    # now add the time that was missing to the interval time and schedule again
    print(f"self.minimal_interval_minutes {minimal_interval_minutes} self.interval_minutes {(interval_minutes)} idle_time {(abs(idle_time))}")
    idle_time = (abs(idle_time.seconds) % 3600) // 60
    print(idle_time)
    print(idle_time+1)
    interval_minutes = idle_time+1
    print(f"Interval time was increased to {interval_minutes} minutes")
    # start_experiment()
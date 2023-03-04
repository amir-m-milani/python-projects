# first get input from user
import time
import winsound

# get minute and second
minute = int(input('Enter Minute: '))
second = int(input('Enter Second: '))
# caculate second
total_second = minute*60+second
# countdown func
while total_second >= 0:
    print(f'{minute}:{second}')
    if second == 0 and minute != 0:
        second = 59
        minute -= 1
        time.sleep(1)
        continue
    second -= 1
    total_second -= 1
    time.sleep(1)

freq = 2500
costum_time = 1000
winsound.Beep(freq, 1000)
print('time is up!')

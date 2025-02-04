from datetime import datetime

lines = [line.strip() for line in open('logfile.txt')]
#print(lines)
for line in lines:
    entry = line.split(', ')
    name = entry[0]
    timein = datetime.strptime(entry[1], "%H:%M")
    timeout = datetime.strptime(entry[-1], "%H:%M")
    duration = str((timeout - timein)).split(':')
#    print('login length is',duration)
    hours = int(duration[0])
    minutes = int(duration[-1])
#    print('number of hours is',hours)
    if (hours >= 1):
        print(name,'logged on for',hours,'hours and',minutes,'minutes')
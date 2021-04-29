import psutil

def convert(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

battery = psutil.sensors_battery()

print(f"Your battery percentage is {battery.percent}")
print(f"Is your battery plugged in ? {battery.power_plugged}")
print(f"Times left is {convert(battery.secsleft)}")

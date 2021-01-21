def to_mins(time):
    parts = time.replace(':', ' ').split()
    hours, mins = int(parts[0]), int(parts[1])
    noon = False

    if len(parts) > 2:
        noon = parts[2]

    if hours == 12 and noon == 'AM':
        total_mins = mins
    elif hours == 12 and noon == 'PM':
        total_mins = mins + 720
    else:
        total_mins = 60 * hours + mins
        if noon == 'PM':
            total_mins += 720

    return total_mins


def to_time(time):
    mins_in_day = 1440
    hours, mins, days_later = 0, 0, 0

    while time - mins_in_day >= 0:
        time -= mins_in_day
        days_later += 1

    while time - 60 >= 0:
        time -= 60
        hours += 1

    if hours >= 12:
        noon = 'PM'
        hours -= 12
    else:
        noon = 'AM'

    if hours == 0:
        hours = 12

    mins = time

    return hours, mins, noon, days_later


def sum_days(day, days_later):
    day = day.lower()
    days = ['monday', 'tuesday', 'wednesday',
            'thursday', 'friday', 'saturday', 'sunday']
    day_i = days.index(day)

    while days_later > 0:
        if day_i == 6:
            day_i -= 7
        day_i += 1
        days_later -= 1

    day = days[day_i].title()

    return day


def add_time(start, duration, day = False):
    start_mins = to_mins(start)
    duration_mins = to_mins(duration)

    new_mins = start_mins + duration_mins

    hours, mins, noon, days_later = to_time(new_mins)
    mins = str(mins).zfill(2)

    if day:
        day_of_week = sum_days(day, days_later)
        formatted_day = ', ' + day_of_week
    else:
        formatted_day = ''

    if days_later == 0:
        new_time = '{}:{} {}{}'.format(hours, mins, noon, formatted_day)
    elif days_later == 1:
        new_time = '{}:{} {}{} (next day)'.format(
            hours, mins, noon, formatted_day)
    else:
        new_time = '{}:{} {}{} ({} days later)'.format(
            hours, mins, noon, formatted_day, days_later)

    return new_time


# print(add_time("3:00 PM", "3:10"))
# print('# Returns: 6:10 PM')

# print(add_time("11:30 AM", "2:32", "Monday"))
# print('# Returns: 2:02 PM, Monday')

# print(add_time("11:43 AM", "00:20"))
# print('# Returns: 12:03 PM')

# print(add_time("10:10 PM", "3:30"))
# print('# Returns: 1:40 AM (next day)')

# print(add_time("11:43 PM", "24:20", "tueSday"))
# print('# Returns: 12:03 AM, Thursday (2 days later)')

# print(add_time("6:30 PM", "205:12"))
# print('# Returns: 7:42 AM (9 days later)')

# print(add_time("11:43 PM", "24:20", "tueSday"))
# print('# Returns: 12:03 AM, Thursday (2 days later)')

# print(add_time("8:16 PM", "466:02", "tuesday"))
# print('# Returns: 6:18 AM, Monday (20 days later)')

# print(add_time("11:59 PM", "24:05"))
# print("Should return: 12:04 AM (2 days later)")

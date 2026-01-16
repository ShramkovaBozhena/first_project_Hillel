my_seconds = int(input("Enter you numbers: "))

day, rest = divmod (my_seconds, 86400)
hour, rest = divmod(rest, 3600)
minute, second  = divmod(rest, 60)

hour_in_str = str(hour).zfill(2)
minute_in_str = str(minute).zfill(2)
second_in_str = str(second).zfill(2)

if 11 <= day % 100 <= 14:
    word = 'днів'
elif 2 <= day % 10 <= 4:
    word = 'дні'
elif day % 10 == 1:
    word = 'день'
else:
    word = 'днів'

print(f"{day} {word} {hour_in_str}:{minute_in_str}:{second_in_str}") 


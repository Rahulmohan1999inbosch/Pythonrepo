# Write a program using time module to greet based on time
# Here i have used time module and  to get the current time
# This is my approach of solving

import time as t
current_time=t.localtime()
time=current_time.tm_hour
if time>=4 and time<=12:
    print('Good morning')
elif time>12 and time <=16:
    print('good afternoon')
else:
    print('Good evening')


print(type(t.strftime('%H:%M:%S')))
x=t.strftime('%H--%M--%S')
print(t.strftime('%H'))


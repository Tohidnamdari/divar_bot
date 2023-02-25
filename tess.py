
jsonarray = [
    {
    'name':'email',
    'datetime':"2017-09-15 04:00:00",
    'length':70,
    'description':'Answer all the emails received today.'
    },
    {
    'name':'email',
    'datetime':"2017-09-16 08:00:00",
    'length':70,
    'description':'Answer all the emails received today.'
    },
    {
    'name':'email',
    'datetime':"2017-09-15 03:00:00",
    'length':70,
    'description':'Answer all the emails received today.'
    }
]


import datetime
import pandas as pd
df = pd.DataFrame(jsonarray)
df.datetime = pd.to_datetime(df.datetime)

printformat = """
Task Name: {}
Start time: {}
End time: {}
Description: {}
"""

def print_tasks(maskby):
    mask = df[df['datetime'].dt.date.astype(str) == maskby].sort_values(by='datetime')
    s = ['These are your tasks for {}:\n'.format(maskby)]
    for ind,row in mask.iterrows():
        name = row["name"]
        stime = row["datetime"].strftime("%H:%M")
        etime = (row["datetime"] + datetime.timedelta(minutes=row["length"])).strftime("%H:%M")
        desc = row["description"]
        s.append(printformat.format(name,stime,etime,desc))
    return ''.join(s)

print(print_tasks("2017-09-15"))


 for 2017-09-15:

Task Name: email
Start time: 03:00
End time: 04:10
Description: Answer all the emails received today.

Task Name: email
Start time: 04:00
End time: 05:10
Description: Answer all the emails received today.


array = [
    ['email', 9, 15, 2, 10, 70, 'Answer all the emails received today.'],
    ['email', 9, 15, 2, 0, 70, 'Answer all the emails received today.'],
    ['email', 9, 15, 3, 0, 70, 'Answer all the emails received today.']
]

printformat = """
Task Name: {}
Start time: {}
End time: {}
Description: {}
"""

date = [9,15]
s = ['These are your tasks for {}:\n'.format(date)]
for item in sorted(array,key=lambda x:(x[3],x[4])):
    if item[1:3] == date:
        s.append(printformat.format(item[0],item[1],item[2],item[3]))

print(''.join(s))


These are your tasks for [9, 15]:

Task Name: email
Start time: 9
End time: 15
Description: 2

Task Name: email
Start time: 9
End time: 15
Description: 2

Task Name: email
Start time: 9
End time: 15
Description: 3




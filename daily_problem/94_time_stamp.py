import random

times = [
    {"timestamp": 1, 'count': 3, "type": "enter"},
    {"timestamp": 2, 'count': 2, "type": "exit"},
    {"timestamp": 3, 'count': 3, "type": "enter"}
]

    
def most_in(times):
    current_count = 0    
    past_time = 'Start'
    period = 0
    for dict in times:
        count = dict['count']
        if dict['type'] != 'enter':
            count = -1 * count
        current_count += count
        dict['people_count'] = current_count
        dict['prev_time'] = past_time
        past_time = dict['timestamp']
    people_count = max([x['people_count'] for x in times])
    return [ ['start: ' + str(x['prev_time']),'end: ' + str(x['timestamp']), 'count: '+ str(x['people_count'])] for x in times if x['people_count'] == people_count]


    
    
    
print(most_in(times))

        
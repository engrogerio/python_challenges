"""
2 people calendar 
return free slots of the cal where they can have meetings
cal = lists of windows time [[12:00, 13:00],...]  Dailybound = [8:00, 18:00] no want meetings


2cal e 2 DB
duration 
list of availability
>>> agenda1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
>>> bounds1 = ['9:00', '20:00']
>>> agenda2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
>>> bounds2 = ['10:00', '18:30']
>>> duration = 30
>>> out = calculate_slots(agenda1, bounds1, agenda2, bounds2, duration)
>>> assert out == [['11:30', '12:00'], ['15:00', '15:30'], ['15:30', '16:00'], ['18:00', '18:30']]

"""

def list_diff(list1, list2):
    """
    >>> list_diff([1,2,3,4], [1,2,5,6])
    [3, 4]

    """
    out = []
    for ele in list1:
        if not ele in list2:
            out.append(ele)
    return out

def common_elements(list1, list2):
    """
    >>> common_elements([1,2,3,4,5], [3,5,6,7,8,9])
    [3, 5]

    """
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result

def get_full_day():
    """
    >>> get_full_day()[0], get_full_day()[-1]
    (['0:00', '0:30'], ['23:30', '0:00'])

    """
    double_hours = range(0, 49)
    hours = [hour/2.0 for hour in double_hours]
    int_days = [hours[n: n+2]  for n, hour in enumerate(hours)][:-1]
    full_day = [[str(int(hrs[0] )) + ":" + ("30" if hrs[0] % 1 > 0 else "00") , str(int(hrs[1] if hrs[1] != 24 else 0)) + ":" + ("30" if hrs[1] % 1 > 0 else "00")] for hrs in int_days]
    return full_day

def get_free_slices(slices, agendas):
    """
    >>> get_free_slices([['1:00', '1:30'], ['1:30', '2:00'], ['2:00', '3:00'], ['3:00', '3:30'], ['3:30', '4:00']], [['1:30', '2:00'], ['3:00', '3:30']])
    [['1:00', '1:30'], ['2:00', '3:00'], ['3:30', '4:00']]

    """
    to_remove = []
    for agenda in agendas: 
        starts = agenda[0]
        ends = agenda[1]
        hour_start = [d[0] for d in slices].index(starts)
        hour_end = [d[1] for d in slices].index(ends)
        for slice in slices[hour_start: hour_end+1]:
            to_remove.append(slice)
    return (list_diff(slices, to_remove))
    

def get_bounded_slices(bounds):
    """
    >>> get_bounded_slices(['18:00', '20:00'])
    [['18:00', '18:30'], ['18:30', '19:00'], ['19:00', '19:30'], ['19:30', '20:00']]

    """
    day = get_full_day()
    starts = bounds[0]
    ends = bounds[1]
    hour_start = [d[0] for d in day].index(starts)
    hour_end = [d[1] for d in day].index(ends)
    return day[hour_start: hour_end+1]

def calculate_slots(agenda1, bounds1, agenda2, bounds2, duration):
    """
    >>> agenda1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    >>> bounds1 = ['9:00', '20:00']
    >>> agenda2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    >>> bounds2 = ['10:00', '18:30']
    >>> duration = 30
    >>> out = calculate_slots(agenda1, bounds1, agenda2, bounds2, duration)
    >>> assert out == [['11:30', '12:00'], ['15:00', '15:30'], ['15:30', '16:00'], ['18:00', '18:30']] 
    
    """
    slices1 = get_bounded_slices(bounds1)
    slices2 = get_bounded_slices(bounds2)
    free_slices1 = get_free_slices(slices1, agenda1)
    free_slices2 = get_free_slices(slices2, agenda2)
    # Slices em comum
    common_slices = common_elements(free_slices1, free_slices2)
    return common_slices

if __name__ == "__main__":
    agenda1 = [['9:00', '10:30'], ['12:00', '13:00'], ['16:00', '18:00']]
    bounds1 = ['9:00', '20:00']
    agenda2 = [['10:00', '11:30'], ['12:30', '14:30'], ['14:30', '15:00'], ['16:00', '17:00']]
    bounds2 = ['10:00', '18:30']
    duration = 30
    out = calculate_slots(agenda1, bounds1, agenda2, bounds2, duration)
    print(out)

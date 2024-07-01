def reduce_one_remaindays(remaindays: list):
    for room_num, room_days in enumerate(remaindays):
        if room_days == 0:
            continue
        remaindays[room_num] = room_days - 1
        
        
def decrease_one_day(room_days:list):
    EMPTY = 0 #상수는 #for문이 길면 변수명 정확히 적어줄 것 이런식으로 표현
    for room_num in enumerate(room_days): #for문이 길면 변수명 정확히 적어줄 것

        
        

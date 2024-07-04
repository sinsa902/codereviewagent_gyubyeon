import sys


def get_award(n, strs, userdata):
    map = [[0 for _ in range(50)] for _ in range(5)]
    chance = [False] * 5
    ffirst = [0] * 5
    conCnt = 0
    sum = 0
    # 하나씩 처리
    # 26글자 for문 돌면서 퀴즈 참석자가 하나씩 시도를 하는 것
    for i in range(26):
        # 2000 달러 찬스를 얻었는지 검사
        for y in range(len(strs)):
            if not chance[y]:
                continue

            for x in range(len(strs[y])):
                if map[y][x] == 0 and strs[y][x] == userdata[i]:
                    # 획득 성공시 2000달러를 얻는다.
                    sum += 2000
                    break
            chance[y] = False
        is_passed = 0
        passCnt = 0
        # 2중 for 돌면서 정답 문자열을 하나씩 검사해서
        # 퀴즈참가자가 던진 문자가 존재하는지 검사
        for y in range(len(strs)):
            for x in range(len(strs[y])):
                if map[y][x] == 1:
                    continue
                # 만약 퀴즈참가자가 요청한 문자가,
                # 정답 문자열과 동일하다면
                if strs[y][x] == userdata[i]:
                    # lets first 점수인지 확인한다.
                    if ffirst[y] == 0 and x == 0:
                        sum += 1000
                        ffirst[y] = 1
                        chance[y] = True
                    elif ffirst[y] == 0 and x != 0:
                        ffirst[y] = 1
                    # used 배열
                    map[y][x] = 1
                    # 해당 문자를 _ 로 바꿔버린다.
                    is_passed = 1
                    # 동일한 문자 개수를 counting 한다.
                    passCnt += 1
        if is_passed == 1:
            conCnt += 1
            sum += (conCnt * 100) * passCnt
        else:
            conCnt = 0
            chance = [False] * 5
    return "$" + str(sum)

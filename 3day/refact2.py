def get_result(str_input):
    ERROR_CODE = "ERROR"
    PASS_CODE = "PASS"
    FAIL_CODE = "FAIL"

    cnt1, cnt2, found_no_digit, p1, p2 = __get_count_and_position(str_input)

    if not __is_valid(cnt1, cnt2, found_no_digit, p1, p2):
        return ERROR_CODE
    if not __is_valid2(p1, p2, str_input):
        return ERROR_CODE

    n1, n2, n3 = __get_n1n2n3(p1, p2, str_input)
    if n1 + n2 == n3:
        return PASS_CODE
    else:
        return FAIL_CODE


def __is_valid2(p1, p2, str_input):
    return p1 >= 1 and p2 >= 3 and p2 < len(str_input) - 1


def __get_count_and_position(str_input):
    found_no_digit = False
    cnt1 = 0
    cnt2 = 0
    p1 = 0
    p2 = 0
    # +와 = 개수 확인
    for i in range(len(str_input)):
        if str_input[i] == "+":
            cnt1 += 1
            p1 = i
        elif str_input[i] == "=":
            cnt2 += 1
            p2 = i
        elif not str_input[i].isdigit():
            found_no_digit = 1
            break
    return cnt1, cnt2, found_no_digit, p1, p2


def __get_n1n2n3(p1, p2, str_input):
    n1 = int(str_input[0:p1])
    n2 = int(str_input[p1 + 1 : p2])
    n3 = int(str_input[p2 + 1 :])
    return n1, n2, n3


def __is_valid(cnt1, cnt2, found_no_digit, p1, p2):
    return cnt1 == 1 and cnt2 == 1 and p1 < p2 and found_no_digit == 0


# 25+61=100
# 1 ~ 5자리수 덧셈 수식이 맞는지 확인하는 프로그램
# 띄어쓰기 없음
str_input = "25+61=86"  # PASS
# str = "12345+12345=24690" # PASS
# str = "5++5=10" # ERROR
# str = "10000+1=10002" # FAIL

print(get_result(str_input))

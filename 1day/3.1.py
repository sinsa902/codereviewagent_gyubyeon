class Node:
    def __init__(self, date_code, name):
        self.date_code = date_code
        self.name = name
        self.is_signed = False

    def do_sign(self):
        self.is_signed = True

    def print_sign(self):
        print(f"{self.date_code} : {self.name}")


class Sign:
    def make_sign(self, sign_lst: list):
        sign_lst = self.sort_sign_by_date(sign_lst)
        self.assert_error(sign_lst)
        self.do_sign(sign_lst)

    def do_sign(self, sign_lst):
        for tar in sign_lst:
            tar.do_sign()
            tar.print_sign()

    def assert_error(self, sign_lst):
        flag = False
        for tar in sign_lst:
            if 0 < tar.date_code < 10:
                continue
            flag = True
            break

        if flag is True:
            raise Exception()

    def sort_sign_by_date(self, sign_lst):
        for y in range(len(sign_lst)):
            for x in range(y + 1, len(sign_lst)):
                if sign_lst[y].date_code > sign_lst[x].date_code:
                    sign_lst[y], sign_lst[x] = sign_lst[x], sign_lst[y]
        return sign_lst


if __name__ == "__main__":
    sign = Sign()
    arr = []
    arr.append(Node(5, "KFC"))
    arr.append(Node(1, "JASON"))
    arr.append(Node(2, "LUCKY"))

    try:
        sign.make_sign(arr)
    except:
        pass

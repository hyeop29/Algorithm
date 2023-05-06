def solution(phone_book):
    sort_Pb = sorted(phone_book)
    for i in range(len(phone_book) - 1) :
        if sort_Pb[i] == sort_Pb[i + 1][:len(sort_Pb[i])] :
            return False
    return True

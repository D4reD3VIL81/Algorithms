def binarySearch(Numbers, SearchedNumber, Min, Max):

    print(Max, Min)

    if (Min == Max and Numbers[Max] != SearchedNumber):
        return False

    Mid = int((Max+Min)/2)

    if(SearchedNumber == Numbers[Mid]):
        return True
    elif (SearchedNumber > Numbers[Mid]):
        return binarySearch(Numbers, SearchedNumber, Mid+1, Max)
    else :
        return binarySearch(Numbers, SearchedNumber, Min, Mid-1)
    



if __name__ == '__main__':

    SearchedNumber = int(input())

    Numbers = [1,4,8,9,24,27,35]

    print(binarySearch(Numbers, SearchedNumber, 0, 6))

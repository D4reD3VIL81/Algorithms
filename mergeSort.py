def merge(Numbers, Min, Max):

    if (Min == Max):
        return Numbers

    Mid = int((Min+Max)/2)

    merge(Numbers, Min, Mid)
    merge(Numbers, Mid+1, Max)
    mergeSort(Numbers, Min, Mid, Max)



    

def mergeSort(Numbers, Min, Mid, Max):

    TempArray = []

    while(len(TempArray) <= Max):
        i = Min
        j = Mid + 1

        if (Numbers[i] >= Numbers[j] and i <= Mid):
            TempArray.append(i)
            i = i+1

        if(Numbers[j] > Numbers[i] and j <= Max):
            TempArray.append(j)
            j = j+1

    return TempArray



    

if __name__ == "__main__":

    List = [1,4,2,33,55,99,120,3]

    print(merge(List))
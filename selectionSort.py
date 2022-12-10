def selectionSort(Numbers):
    
    for i in range(1, len(Numbers)):
        Key = Numbers[i]
        j = i-1

        print(i, j)

        while(Numbers[j] > Key):
            Numbers[j+1] = Numbers[j]
            j = j-1

        Numbers[j+1] = Key

        print(Numbers)

    return Numbers
            


if __name__ == "__main__":

    List = [4, 70, 8, 13, 90, 23]

    print(selectionSort(List))
def bubbleSort(Numbers):
    
    for i in range(len(Numbers)):

        for j in range(i):

            if Numbers[j] > Numbers[i]:
                Temp = Numbers[i]
                Numbers[i] = Numbers[j]
                Numbers[j] = Temp

    return Numbers


if __name__ == "__main__":

    List = [9, 2, 5, 7, 1, 2, 4, 6]

    print(bubbleSort(List))
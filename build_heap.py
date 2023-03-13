# python3


def build_heap(data):
    swaps = []

    for i in range(len(data) // 2 - 1, -1, -1):
        j = i 
        while 2*j+1<len(data):
            k=2*j+1
            if k + 1 <len(data) and data[k + 1]<data[k]:
                k += 1
            if data[j] <= data[k]:
                break
            swaps.append((j, k))
            data[j], data[k] = data[k], data[j]
            j=k

    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    source = input("I or F")

    # input from keyboard
    if source == "I":
        n = int(input())
        data = list(map(int, input().split()))
    elif source == "F":
        filename = input("Enter the file name: ")
        with open(filename, "r")as x:
            n = int(x.readline())
            data = list(map(int, x.readline().split()))
    else:
        print("Error")

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    print("Nr. of swaps: ", len(swaps))
    assert len(swaps)< 4 * n


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()



#----  quiz  binary search practice  ----------

def binary_search(input_array,value):
    """returns index of value or -1 if value not found
        works on sorted  lists
        O(ln(n))
    """

    counter = 0
    lbord = 0
    rbord = len(input_array)
    while rbord - lbord > 1:
        counter += 1
        mid = lbord + len(input_array[lbord:rbord]) // 2
        if value == input_array[mid]:
            return mid
        elif  value > input_array[mid]:
            lbord = mid
        elif value < input_array[mid]:
            rbord = mid
        #print("step: {0}, lbord: {1}, rbord: {2}, subarr: {3}"
        #  .format(counter, lbord, rbord, input_array[lbord:rbord]))
    return -1



def test_binary_searh():
    il = [1,3,9,11,15,19,29]
    res = binary_search(il, 25)
    print("res", res)
    res = binary_search(il, 15)
    print("res", res)


def main():
    test_binary_searh()

if __name__ == '__main__':
        main()


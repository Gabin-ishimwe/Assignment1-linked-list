# we are going to write a function that check is element in a list
# occurs odd amount of times in the list

def odd(items):
    count = {}
    for i in items:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

    counting = len(count)
    current_count = 0
    for j in count:
        if count[j] % 2 != 0:
            current_count += 1
            if counting == current_count:
                print(True)
            else:
                continue
        else:
            print(False)
            break


odd([1, 2, 3, 5, 6, 2])

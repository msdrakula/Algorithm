arr = list(map(int, input().split()))
target = int(input())

def main():
    left_pointer = 0
    right_pointer = len(arr) - 1

    while left_pointer <= right_pointer:
        mid = (left_pointer + right_pointer) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left_pointer = mid + 1
        else:
            right_pointer = mid - 1
    return left_pointer
    

    # if num in arr:
    #     element_ind = arr.index(num)
    #     print(element_ind)
    # else:
    #     print((len(arr) + 1) - 1)

    
if __name__ == '__main__':
    print(main())




# def find_index(data, num):
#     left_pointer = 0
#     right_pointer = len(data) - 1
   
#     # граничные значения
#     if data[right_pointer] < num:
#         return len(data)
#     elif data[left_pointer] > num:
#         return 0

#     while left_pointer <= right_pointer:
#         mid = round(left_pointer + right_pointer) // 2

#         if data[mid] == num:
#             return mid
#         if data[mid] < num:
#             left_pointer = mid + 1
#         else:
#             right_pointer = mid - 1
#         #return mid + 1


# if __name__ == '__main__':

#     print(find_index(arr, num))



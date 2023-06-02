# def bubble_sort(lst: list):

#     #1. n = length of the list
#     # 2. swapped = True
#     # 3. while swapped is True:
#             # swapped = False
#             # for i from 1 to n-1:
#                 # if lst[i] > lst[i]:
#                 #       swap lst[i-1] and lst[i]
#                 #       swapped = True
#                 #end if
#             # end for
#         # end while

def bubble_sort(canvas, lst: list):
    """_summary_

    Args:
        lst (list): _description_
    
    >>> bubble_sort([1,0,0,-12,3,37,16,96,5])
    [-12,0,0,1,3,5,16,37,96]
    """
    n = len(lst)

    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if lst[i-1] > lst[i]:
                temp = lst[i]
                lst[i]= lst[i-1]
                lst[i-1] = temp
    return lst


my_list = [1,0,0,-12,3,37,16,96,5]
print(bubble_sort(my_list))

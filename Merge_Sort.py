## Program to Merge Sort

def Merge_Sort(array):
    '''This function returns the sorted Elements'''
    #to check lennghth of array is greter than 1 otherwise no need to sort
    if len(array) > 1:
        mid_element=len(array)//2
        left_element=array[:mid_element]
        right_element=array[mid_element:]
        Merge_Sort(right_element)
        i=j=k=0

        while i < len(left_element) and j < len(right_element):
            if left_element[i] < right_element[j]:
                array[k]=left_element[i]
                i+=1
            else:
                array[k]=right_element[j]
                j+=1
            k+=1

        #to check array elements left side    

        while i < len(left_element):
            array[k]=left_element[i]
            i+=1
            k+=1

        #to check array elements right side 

        while j < len(right_element):
            array[k]=right_element[j]
            j+=1
            k+=1

def print_sorted_array(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()

if __name__=='__main__':
    arry=[int(item) for item in input("Enter the list items : ").split()]
    Merge_Sort(arry)
    print_sorted_array(arry)

#sample output
# Enter the list items : 12 56 45 59 1
# 1 12 45 56 59 
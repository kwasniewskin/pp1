array = [1,2,3,4,5]

array[0] = 1 - array[0]
array[-1] = array[-1] + 4
array[len(array)//2] *= 2

print(array)
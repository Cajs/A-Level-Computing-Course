array = [50,52,51,44,23,128,92]
array_sorted_auto =[0,0,0,0,0]
array_sorted_manual = []
array_length = len(array)
counter = 0
counter_sorted = 0
while counter < array_length:
    if array[counter] >= 50:
        print(array[counter])
        array_sorted_auto[counter_sorted] = array[counter]
        counter_sorted = counter_sorted +1
    counter = counter +1
while array:
    smallest = min(array)
    index = array.index(smallest)
    array_sorted_manual.append(array.pop(index))
print("Manual sort:", array_sorted_manual)
array_sorted_auto.sort()
print("Automated sort:", array_sorted_auto)

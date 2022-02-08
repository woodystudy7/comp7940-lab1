def reverse_string(x):
    new_string = ""
    my_list = list(x)
    for i in range(len(my_list)-1,-1,-1):
        new_string += my_list[i]
    return(new_string)
        


abc = "hellooos"
new = reverse_string(abc)
print(new)
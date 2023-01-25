# after getting a clarity of function implementation i learnt about
# dictionaries how to update their values how to add elements 
# and also used specific type castinng without the help of resources
# i guess i learnt that while previous exercise and for this script 
# i surfed throught W3schools was quite heplful helped me go through some
# concepts and render some mistakes

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict={}
def get_combined_dict(dict_1,dict_2):
    temp_dict={}
    for i in dict_1:
        if i in dict_2:
            temp_dict.update({i:str(int(dict_1[i])+int(dict_2[i]))})

    return temp_dict


combined_dict = get_combined_dict(my_dict_1, my_dict_2)

print(combined_dict)
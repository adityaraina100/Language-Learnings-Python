def get_max(listt):
    max=listt[0]
    for i in listt:
        if i>max:
            max=i
    return max
listt=[12,23,45,32,1,23]
print(get_max(listt))
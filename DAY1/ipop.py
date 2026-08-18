def count_char(string,target):
    count=0
    for ch in string:
        if ch==target:
            count=count+1
    print(count)
count_char("ilamvinodini","i")
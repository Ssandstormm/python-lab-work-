import os

create = "C:/Users/smash/Desktop/aida/aidas"
os.mkdir(create)
dir = "C:/Users/smash/Desktop/aida/aidas"
dir2 = "C:/Users/smash/Desktop/aida/aidas2"

os.rename(dir,dir2)
list1 = []
for i in os.listdir(dir2):
    if os.i.isfile(os.i.join(dir2, i)):
        list1.append(i)
print(list1)
os.rmdir(dir2)
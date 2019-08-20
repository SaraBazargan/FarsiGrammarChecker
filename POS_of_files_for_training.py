import os
import fnmatch

inf = input("name the dir to search(enter a period for this dir):")           # آدرس مسير دايرکتوري حاوي فايل هاي پيکره

matches = []
for root, dirnames, filenames in os.walk(inf):
    for filename in fnmatch.filter(filenames, '*.txt'):
        matches.append(os.path.join(root, filename))            #  matches ريختن نام فايلهاي متني پيکره موجود در دايرکتوري انتهايي مسير در ليست 
        
#-------------------------------------------------------------------
        
fp1=open('list_of_POS.txt', 'w')

for i in matches:
    #print(i)
    with open(i, 'r') as fp:
        txt =fp.read().split('\n')
        for line in txt[:-1]:
            line_list = line.split()
            POS = line_list[3]
            item = POS + '\t'            # نوشتن پي او اس کلمات هر فايل در يک خط با يک تب فاصله بين هر يک از آنها
            fp1.write(item)
            fp.close()
    fp1.write('\n')             # نوشتن مجموعه پي او اس هاي کلمات هر فايل پيکره در يک خط جداگانه
fp1.close()


import nltk
from nltk.util import ngrams


#______________________________________ First Pass ___________________________________________        


fp2 = open('list_of_POS.txt', 'r')
f2 = fp2.read()
txt2 = f2.split()
fd = nltk.FreqDist(txt2)                                     # محاسبه تعداد تکرار يونيگرام ها در پيکره
ordered_dic = sorted(fd.items(), key=lambda t: t[1])         # ليستي مرتب شده از يونيگرم (پي او اس) ها بر اساس تعداد تکرار هر (پي او اس) در پيکره
print('len unigram', len(ordered_dic))
fp2.close()

temp = []
for item in ordered_dic:
    if item[1] > 200 and temp == []:                          # تعيين مقدار مينيمم ساپورت     
        temp = ordered_dic[ordered_dic.index(item)+1:]       # f1:  حذف مقادير غيرشايع يونيگرم (پي او اس) و تشکيل ليست نهايي يونيگرم ها
        print('len GSP unigrams', len(temp))


#______________________________________ Second Pass ___________________________________________        

        
bigram = nltk.bigrams(txt2)                                         #تشکيل بايگرام پي او اس هاي پيکره
fd_bi = nltk.FreqDist(bigram)                                       # محاسبه فرکانس بايگرام ها
print('len fd_bi', len(fd_bi))
bi_gram = {}
for bi in fd_bi.keys():                                             # تشکيل يک ديکشنري از بايگرام هايي که بر اساس يونيگرام هاي پرتکرار در پيکره ساخته مي شوند
    if bi[0] in [temp[i][0] for i in range(len(temp))]:
        bi_gram[bi] = fd_bi[bi]

ordered_dic2 = sorted(bi_gram.items(), key=lambda t: t[1])          # تشکيل ليستي مرتب شده بر اساس تعداد تکرار از بايگرام پي او اس ها     


temp2 = []
for item in ordered_dic2:
    if item[1] > 200 and temp2 == []:                               #  اعمال محدوديت روي بايگرم پي او اس ها: فقط درنظرگرفتن مقادير بالاتر از مينمم ساپورت 
        temp2 = ordered_dic2[ordered_dic2.index(item)+1:]          # f2:   تشکيل ليست نهايي بايگرم-پي او اس هاي پرتکرار
        print('len GSP bigrams', len(temp2))


#______________________________________ Third Pass ___________________________________________        

'''
# روش اول
tri_gram_list = []
for temp_item in temp2:                                            # استخراج ترايگرم- پي او اس هاي کانديدايي که در پيکره هم وجود خارجي داشته باشند
    for item in fd.keys():
        if temp_item[0][0]+'*'+temp_item[0][1]+'*'+item in f2:
            tri_gram_list.append((temp_item[0][0],temp_item[0][1],item))


trigram = nltk.trigrams(txt2)
fd_tri = nltk.FreqDist(trigram)
print('len fd_tri', len(fd_tri))

tri_gram_dic = {}
for i in tri_gram_list:                                            # استخراج تعداد تکرار ترايگرم-پي او اس ها 
        tri_gram_dic[i] = fd_tri[i]
'''
# روش دوم
candidate_pos_trigrams = []
for item1 in temp2:
    for item2 in temp2:
        if item1[0][1] == item2[0][0]:                            #* تشکيل ليست ترايگرم-پي او اس هاي کانديدا با استفاده از ليست نهايي بايگرم هاي پرتکرار مرحله قبل 
            candidate_pos_trigrams.append([item1[0][0],item1[0][1],item2[0][1]])  

trigram = nltk.trigrams(txt2)
fd_tri = nltk.FreqDist(trigram)
print('len fd_tri', len(fd_tri))

tri_gram_dic = {}
for t in fd_tri:
    if [t[0],t[1],t[2]] in candidate_pos_trigrams:
        tri_gram_dic[t]= fd_tri[t]

ordered_dic3 = sorted(tri_gram_dic.items(), key=lambda t: t[1])  # تشکيل ليستي مرتب شده از ترايگرام هاي موجود در پيکره بر اساس تعداد تکرار   
#print('len trigram', len(ordered_dic3))


temp3 = []
for item in ordered_dic3:
    if item[1] > 200 and temp3 == []:                            #  اعمال محدوديت روي ترايگرم پي او اس ها: فقط درنظرگرفتن مقادير بالاتر از مينمم ساپورت 
        temp3 = ordered_dic3[ordered_dic3.index(item)+1:]       # f3:   تشکيل ليست نهايي ترايگرم-پي او اس هاي پرتکرار
        print('len GSP trigrams', len(temp3))


#______________________________________ 4th Pass ___________________________________________ 


# روش اول
'''
four_gram_list = []
for temp_item in temp3:
    for item in fd.keys():
        if temp_item[0][0]+'*'+temp_item[0][1]+'*'+temp_item[0][2]+'*'+item in f2:
            four_gram_list.append((temp_item[0][0],temp_item[0][1],temp_item[0][2],item))
'''
# روش دوم
candidate_pos_quadgrams = []
for item1 in temp3:
    for item2 in temp3:
        if item1[0][1] == item2[0][0] and item1[0][2] == item2[0][1]:   #  تشکيل ليست 4-گرم_پي او اس هاي کانديدا با استفاده از ليست ترايگرم هاي پرتکرار مرحله قبل 
            candidate_pos_quadgrams.append([item1[0][0],item1[0][1],item1[0][2],item2[0][2]]) 

fourgram = ngrams(txt2, 4)                       # محاسبه 4گرم هاي پيکره
fd_four = nltk.FreqDist(fourgram)                # محاسبه تعداد تکرار 4گرم ها
print('len fd_four', len(fd_four))

four_gram_dic = {}
for q in fd_four.keys():
    if list(q) in candidate_pos_quadgrams:       # محاسبه تعداد تکرار 4گرم هايي که با استفاده از ليست ترايگرم هاي مرحله قبل ساخته شده اند
        four_gram_dic[q] = fd_four[q]
#print('four_gram_dic', len(four_gram_dic))

ordered_dic4 = sorted(four_gram_dic.items(), key=lambda t: t[1])    # تشکيل ليستي مرتب شده از 4گرم هاي بر اساس تعداد تکرار آنها 
temp4 = []
for item in ordered_dic4:
    if item[1] > 200 and temp4 == []:                                #  اعمال محدوديت روي 4گرم پي او اس ها: فقط درنظرگرفتن مقادير بالاتر از مينمم ساپورت 
        temp4 = ordered_dic4[ordered_dic4.index(item)+1:]           # f4:   تشکيل ليست نهايي 4-گرم_پي او اس هاي پرتکرار
        print('len GSP fourgrams', len(temp4))                

        
#______________________________________ 5th Pass ___________________________________________


#روش اول
'''        
five_gram_list = []
for temp_item in temp4:
    for item in fd.keys():
        if temp_item[0][0]+'*'+temp_item[0][1]+'*'+temp_item[0][2]+'*'+temp_item[0][3]+'*'+item in f2:   #  تشکيل ليست 5-گرم_پي او اس هاي کانديدا با استفاده از ليست ترايگرم هاي پرتکرار مرحله قبل 
            five_gram_list.append((temp_item[0][0],temp_item[0][1],temp_item[0][2],temp_item[0][3],item))
'''

# روش دوم
candidate_pos_fivegrams = []
for item1 in temp4:
    for item2 in temp4:
        if item1[0][1] == item2[0][0] and item1[0][2] == item2[0][1] and item1[0][3] == item2[0][2]:   #  تشکيل ليست 5-گرم_پي او اس هاي کانديدا با استفاده از ليست 4گرم هاي پرتکرار مرحله قبل 
            candidate_pos_fivegrams.append((item1[0][0],item1[0][1],item1[0][2],item1[0][3],item2[0][3])) 


fivegram = ngrams(txt2, 5)                   # محاسبه 5گرم هاي پيکره
fd_five = nltk.FreqDist(fivegram)            # محاسبه تعداد تکرار 5گرم ها
print('len fd_five', len(fd_five))           

five_gram_dic = {}
for i in candidate_pos_fivegrams:                     # محاسبه تعداد تکرار 5گرم هايي که با استفاده از ليست 4گرم هاي مرحله قبل ساخته شده اند
        five_gram_dic[i] = fd_five[i]
#print('four_gram_dic', len(four_gram_dic))

ordered_dic5 = sorted(five_gram_dic.items(), key=lambda t: t[1])      # تشکيل ليستي مرتب شده از 5گرم هاي بر اساس تعداد تکرار آنها 
temp5 = []
for item in ordered_dic5:
    if item[1] > 100 and temp5 == []:                                  #  اعمال محدوديت روي 5گرم پي او اس ها: فقط درنظرگرفتن مقادير بالاتر از مينمم ساپورت 
        temp5 = ordered_dic5[ordered_dic5.index(item)+1:]             # f5:   تشکيل ليست نهايي 5-گرم_پي او اس هاي پرتکرار
        print('len GSP fivegrams', len(temp5))

        
#______________________________________ 6th Pass ___________________________________________

        
candidate_pos_sixgrams = []
for item1 in temp5:
    for item2 in temp5:
        if item1[0][1] == item2[0][0] and item1[0][2] == item2[0][1] and item1[0][3] == item2[0][2] and item1[0][4] == item2[0][3]:   # تشکيل ليست 6-گرم_پي او اس هاي کانديدا با استفاده از ليست 5گرم هاي پرتکرار مرحله قبل 
            candidate_pos_sixgrams.append([item1[0][0],item1[0][1],item1[0][2],item1[0][3],item1[0][4],item2[0][4]]) 

sixgram = ngrams(txt2, 6)               # محاسبه 6گرم هاي پيکره
fd_six = nltk.FreqDist(sixgram)         # محاسبه تعداد تکرار 6گرم ها
print('len fd_six', len(fd_six))

six_gram_dic = {}
for q in fd_six.keys():
    if list(q) in candidate_pos_sixgrams:                         # محاسبه تعداد تکرار 6گرم هايي که با استفاده از ليست 5گرم هاي مرحله قبل ساخته شده اند
        six_gram_dic[q] = fd_six[q]
#print('six_gram_dic', len(six_gram_dic))

ordered_dic6 = sorted(six_gram_dic.items(), key=lambda t: t[1])   # تشکيل ليستي مرتب شده از 6گرم هاي بر اساس تعداد تکرار آنها 
temp6 = []
for item in ordered_dic6:
    if item[1] > 100 and temp6 == []:                              #  اعمال محدوديت روي 6گرم پي او اس ها: فقط درنظرگرفتن مقادير بالاتر از مينمم ساپورت 
        temp6 = ordered_dic6[ordered_dic6.index(item)+1:]         # f6:   تشکيل ليست نهايي 6-گرم_پي او اس هاي پرتکرار
        print('len GSP sixgrams', len(temp6))
        print()


#______________________________________ 7th Pass ___________________________________________

        
candidate_pos_sevengrams = []
for item1 in temp6:
    for item2 in temp6:
        if item1[0][1] == item2[0][0] and item1[0][2] == item2[0][1] and item1[0][3] == item2[0][2] and item1[0][4] == item2[0][3] and item1[0][5] == item2[0][4]:   #   تشکيل ليست 7-گرم_پي او اس هاي کانديدا با استفاده از ليست 6گرم هاي پرتکرار مرحله قبل 
            candidate_pos_sevengrams.append([item1[0][0],item1[0][1],item1[0][2],item1[0][3],item1[0][4],item1[0][5],item2[0][5]]) 

sevengram = ngrams(txt2, 7)               # محاسبه 7گرم هاي پيکره
fd_seven = nltk.FreqDist(sevengram)         # محاسبه تعداد تکرار 7گرم ها
print('len fd_seven', len(fd_seven))

seven_gram_dic = {}
for q in fd_seven.keys():
    if list(q) in candidate_pos_sevengrams:                         # محاسبه تعداد تکرار 7گرم هايي که با استفاده از ليست 6گرم هاي مرحله قبل ساخته شده اند
        seven_gram_dic[q] = fd_seven[q]


ordered_dic7 = sorted(seven_gram_dic.items(), key=lambda t: t[1])   # تشکيل ليستي مرتب شده از 7گرم هاي بر اساس تعداد تکرار آنها 
temp7 = []
for item in ordered_dic7:
    if item[1] > 100 and temp7 == []:                              #  اعمال محدوديت روي 7گرم پي او اس ها: فقط درنظرگرفتن مقادير بالاتر از مينمم ساپورت 
        temp7 = ordered_dic7[ordered_dic7.index(item)+1:]         # f7:   تشکيل ليست نهايي 7-گرم_پي او اس هاي پرتکرار
        print('len GSP sevengrams', len(temp7))
        print()



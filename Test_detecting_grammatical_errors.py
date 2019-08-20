
import nltk
from nltk.util import ngrams
from Train_GSP_Algorithm import *
from Test_writing_POStags_InATextFile import *

fp = open('Test_file_pos.txt')
sentences_pos_list = fp.read().split('\n')
fp.close()

sentence_pos_list = [[]for i in range(len(sentences_pos_list)-1)]
for s in range(len(sentences_pos_list)-1):
	sentence_pos_list[s]=sentences_pos_list[s].split('\t')
	sentence_pos_list[s]=sentence_pos_list[s][:-1]

errors_list = []       #کل دنباله تگ هايي که نادرست تشخيص داده مي شوند در اين ليست مي ريزيم 
for l in sentence_pos_list:
    q_errors=[]
    t_errors=[]
    b_errors=[]
    errors=0
    
    if len(l) > 5:
        sentence_pos_sixgrams = []
        sixgrams = ngrams(l, 6)
        for sixgram in sixgrams:
            sentence_pos_sixgrams.append([sixgram])    # ايجاد ليستي از 6گرم-پي او اس ها براي جملاتي که بيش از 5 کلمه دارند 


        for sq in sentence_pos_sixgrams:                       # تشخيص خطاي گرامري در جملات طولاني تر از 5 کلمه
            if sq not in temp6:
                errors += 1
                q_errors.append(sq)
                errors_list.append(sq)
        if errors != 0:
            print('There is a grammatical error in sentence number',(sentence_pos_list.index(l)+1),':')
            print(q_errors[0])
            
            

    elif len(l) == 5:
        sentence_pos_fivegrams = []
        fivegrams = ngrams(l, 5)
        for fivegram in fivegrams:
            sentence_pos_fivegrams.append([fivegram])    # ايجاد ليستي از 5گرم-پي او اس ها براي جملاتي که فقط 5 کلمه دارند 


        for sq in sentence_pos_fivegrams:                       # تشخيص خطاي گرامري براي جملات 5 کلمه اي
            if sq not in temp5:
                errors+=1
                q_errors.append(sq)
        errors_list.append(sq)
        if errors != 0:
            print('There is a grammatical error in sentence number',(sentence_pos_list.index(l)+1),':')
            print(q_errors)

            
    elif len(l) == 4:
        sentence_pos_quadgrams = []
        fourgrams = ngrams(l, 4)
        for fourgram in fourgrams:
            sentence_pos_quadgrams.append([fourgram])   # ايجاد ليستي از 4گرم-پي او اس ها براي جملاتي که فقط 4 کلمه دارند 


        for sq in sentence_pos_quadgrams:                       # تشخيص خطاي گرامري براي جملات 4 کلمه اي
            if sq not in temp4:
                errors+=1
                q_errors.append(sq)
        errors_list.append(sq)
        if errors != 0:
            print('There is a grammatical error in sentence number',(sentence_pos_list.index(l)+1),':')
            print(q_errors)
            

    elif len(l) == 3:
        sentence_pos_trigrams = []
        trigrams = nltk.trigrams(l)
        for trigram in trigrams:
            sentence_pos_trigrams.append([trigram])                                # ايجاد ليستي از ترايگرم-پي او اس ها براي جملاتي که فقط 3 کلمه دارند

        for sq in sentence_pos_trigrams:                        # تشخيص خطاي گرامري براي جملات 3 کلمه اي
            if sq not in temp3:
                errors += 1
                t_errors.append(sq)
        errors_list.append(sq)
        if errors != 0:
            print('There is a grammatical error in sentence number',(sentence_pos_list.index(l)+1),':')
            print(t_errors)

            
    elif len(l) == 2:
        sentence_pos_bigrams = []
        bigrams = nltk.bigrams(l)
        for bigram in bigrams:
            sentence_pos_bigrams.append([bigram])             # ايجاد ليستي از بايگرم-پي او اس ها براي جملاتي که فقط 2 کلمه دارند

        for sq in sentence_pos_bigrams:                         # تشخيص خطاي گرامري در جملات 2 کلمه اي
            if sq not in temp2:
                errors += 1
                b_errors.append(sq)
        errors_list.append(sq)
        if errors != 0:
            print('There is a grammatical error in sentence number',(sentence_pos_list.index(l)+1),':')
            print(b_errors)
            
            
    elif len(l)==1 and (l[0][0]!='N' or l[0][0]!='V' or l[0][0]!='ADV'):                                    # فقط جملات تک کلمه اي داراي پي او اس هاي خاصي قابل پذيرش هستند
        print('There are grammatical errors in sentence number:',(sentences_pos_list.index(l)+1))
        

    print('\n')


### calculating precision & recall
tp = 0
fp = 0
for tags in errors_list:
        string = ''
        for tag in tags[0]:
                string =string + tag + '\t'
        #print(string)
        if string in sentences_pos_list:
                tp += 1      # اگر غلط نحوي نمايش داده شده به درستي تشخيص داده شده باشد آن را مي شماريم
        else:
                fp += 1      # اگر غلط نحوي نمايش داده شده به اشتباه تشخيص داده شده باشد آن را مي شماريم     


recall = (tp / (len(sentences_pos_list)))*100
print('Recall = ', recall,'%')

precision = (tp / (tp+fp))*100
print('Precision = ', precision,'%')




                                    
                

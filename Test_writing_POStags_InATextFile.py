

fp = open('Test_Ungrammatical_Sentences.txt', 'r')

file_lines_list = fp.read().split('\n')

fp.close()

fp_w = open('Test_file_pos.txt','w')       
for line in range(len(file_lines_list)-1):
            line_list = file_lines_list[line].split()
               
            POS = line_list[2:-1]
            if len(POS)>2 and ',' not in POS[-1]:
                POS.pop(-1)
            #print(POS)   
            fp_w.write(POS[1]      # ايجاد يک فايل تکست از دنباله پي او اس هاي کلمات هر جمله از فايل تست
            fp_w.write('\t')       # جداکردن هر پي او اس از ديگري با يک تب فاصله
                                  

            if line_list[-1]== '.' or line_list[-1]== '؟' or line_list[-1]== '!':    # نوشتن مجموعه پي او اس هاي کلمات هر جمله فايل در يک خط جداگانه
                fp_w.write('\n')

            
fp_w.close()
            
        

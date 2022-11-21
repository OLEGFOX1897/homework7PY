from logger import user_logger
def calculator(input_data):
    if input_data[0]==1:
        inp_expression=input_data[1]
        inp_expression=inp_expression.replace(' ','')
        def LR_digit(ind_sign, inp_expression):
            """ Модуль возвращает в кортеже левое, правое число относительно входного индекса математич знака,
            а так же их левый и правый индексы в выражении"""
            ind=ind_sign
            while True:
                ind+=1
                if ind<=len(inp_expression)-1:
                    if inp_expression[ind].isdigit()==0 and inp_expression[ind]!='.':
                        right_dig_ind=ind-1
                        break
                elif ind>len(inp_expression)-1:
                    right_dig_ind=len(inp_expression)-1
                    break
            ind=ind_sign
            while True:
                ind-=1
                if ind==0 and inp_expression[ind].isdigit()==1:
                    left_dig_ind=0
                    break
                elif inp_expression[0]=='-' and ind==0:
                    left_dig_ind=0
                    break
                elif not inp_expression[ind].isdigit() and inp_expression[ind]!='.':
                    left_dig_ind=ind+1
                    break
            return inp_expression[left_dig_ind:ind_sign], inp_expression[ind_sign+1:right_dig_ind+1], left_dig_ind, right_dig_ind 

        def calc_mem(inp_expression):
            while True:
                if inp_expression.find('/0')!=-1:
                            print(inp_expression.find('/0'))
                            print('Делить на ноль нельзя. Перезапустите программу и исправьте выражение.')
                            user_logger('Завершение программы. В введенном выражении присутствует деление на 0')
                            break
                elif '--' in inp_expression:
                    inp_expression=inp_expression.replace('--','+')
                elif '+-' in inp_expression:
                    inp_expression=inp_expression.replace('+-','-')
                elif'(' and ')' in inp_expression:
                    list_no_dig=[x for x in inp_expression[inp_expression.find('(')+1: inp_expression.find(')')] if not x.isdigit()] # находит математ знак в скобках
                    inp_expression=new_mem(inp_expression.find(list_no_dig[0],inp_expression.find('(')), inp_expression, list_no_dig[0], 1)
                elif '*' in inp_expression:
                        inp_expression=new_mem(inp_expression.find('*'), inp_expression,'*', 0)
                elif '/' in inp_expression:
                        inp_expression=new_mem(inp_expression.find('/'), inp_expression,'/', 0)
                elif inp_expression.find('-',1)>0 or inp_expression.find('+',1)>0:
                        list_ind_s_min=[x for x in range(1,len(inp_expression)-1) if inp_expression[x]=='+' or inp_expression[x]=='-'] # создает лист с индексами всех (+) и (-) 
                        # не включая самый первый
                        ind_sign=list_ind_s_min[0] #индекс знака
                        sign=inp_expression[ind_sign] #знак в выражении + или -
                        inp_expression=new_mem(ind_sign, inp_expression, sign, 0)
                else: break
            return inp_expression
                
        def new_mem(ind_sign, inp_expression, a:str, b):
            '''Модуль возвращает новое математическое выражение после выполненого одного математ действия'''
            tut_LR_dig=LR_digit(ind_sign,inp_expression)
            if a=='*':
                new_dig=float(tut_LR_dig[0])*float(tut_LR_dig[1])
            elif a=='/':
                new_dig=float(tut_LR_dig[0])/float(tut_LR_dig[1])
            elif a=='-':
                new_dig=float(tut_LR_dig[0])-float(tut_LR_dig[1])
            elif a=='+':
                new_dig=float(tut_LR_dig[0])+float(tut_LR_dig[1])
            if b==0:    
                inp_expression=inp_expression[0:tut_LR_dig[2]]+str(new_dig)+inp_expression[tut_LR_dig[3]+1:len(inp_expression)]
            else:
                inp_expression=inp_expression[0:tut_LR_dig[2]-1]+str(new_dig)+inp_expression[tut_LR_dig[3]+2:len(inp_expression)]
            return inp_expression
        out_digit=calc_mem(inp_expression)
        return out_digit
    else:
        out_digit=eval(input_data[1])
        return out_digit

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Функция оброботки ответов
def work_at_answer(arr):
    new_arr=[]

    # Извлечение номера вопроса и варианта ответа
    for i in arr:
        j=6
        number=''

        while j<len(i):
            if i[j]!='_':
                number+=i[j]
            
            else:
                j+=1
                break

            j+=1

        column=i[j]

        # Ловушка что бы на один вопрос не отвечали дважды
        if int(number) not in new_arr:
            new_arr.append(int(number))
            new_arr.append(str(column))
    
        else:
            return 'Error'
 
    # Распределение ответов по характерам
    arr=new_arr
    count_kompromis=0
    count_izbeganie=0
    count_sopernichestvo=0
    count_prisposoblenie=0
    count_sotrudnichestvo=0

    # Цикл по всем ответам
    for i in range(0, len(arr), 2):
        if arr[i]==1:
            if arr[i+1]=='A':
                count_izbeganie+=1

            else:
                count_prisposoblenie+=1

        elif arr[i]==2:
            if arr[i+1]=='A':
                count_kompromis+=1

            else:
                count_sotrudnichestvo+=1

        elif arr[i]==3:
            if arr[i+1]=='A':
                count_sotrudnichestvo+=1

            else:
                count_prisposoblenie+=1

        elif arr[i]==4:
            if arr[i+1]=='A':
                count_kompromis+=1

            else:
                count_prisposoblenie+=1

        elif arr[i]==5:
            if arr[i+1]=='A':
                count_sotrudnichestvo+=1

            else:
                count_izbeganie+=1

        elif arr[i]==6:
            if arr[i+1]=='A':
                count_izbeganie+=1

            else:
                count_sopernichestvo+=1

        elif arr[i]==7:
            if arr[i+1]=='A':
                count_izbeganie+=1

            else:
                count_kompromis+=1

        elif arr[i]==8:
            if arr[i+1]=='A':
                count_sopernichestvo+=1

            else:
                count_sotrudnichestvo+=1

        elif arr[i]==9:
            if arr[i+1]=='A':
                count_izbeganie+=1

            else:
                count_sopernichestvo+=1

        elif arr[i]==10:
            if arr[i+1]=='A':
                count_sopernichestvo+=1

            else:
                count_kompromis+=1

        elif arr[i]==11:
            if arr[i+1]=='A':
                count_sotrudnichestvo+=1

            else:
                count_prisposoblenie+=1

        elif arr[i]==12:
            if arr[i+1]=='A':
                count_izbeganie+=1

            else:
                count_kompromis+=1

        elif arr[i]==13:
            if arr[i+1]=='A':
                count_kompromis+=1

            else:
                count_sopernichestvo+=1

        elif arr[i]==14:
            if arr[i+1]=='A':
                count_sotrudnichestvo+=1

            else:
                count_sopernichestvo+=1

        elif arr[i]==15:
            if arr[i+1]=='A':
                count_prisposoblenie+=1

            else:
                count_izbeganie+=1

        elif arr[i]==16:
            if arr[i+1]=='A':
                count_prisposoblenie+=1

            else:
                count_sopernichestvo+=1

        elif arr[i]==17:
            if arr[i+1]=='A':
                count_sopernichestvo+=1

            else:
                count_izbeganie+=1

        elif arr[i]==18:
            if arr[i+1]=='A':
                count_prisposoblenie+=1

            else:
                count_kompromis+=1

        elif arr[i]==19:
            if arr[i+1]=='A':
                count_sotrudnichestvo+=1

            else:
                count_izbeganie+=1

        elif arr[i]==20:
            if arr[i+1]=='A':
                count_sopernichestvo+=1

            else:
                count_kompromis+=1

        elif arr[i]==21:
            if arr[i+1]=='A':
                count_prisposoblenie+=1

            else:
                count_sotrudnichestvo+=1

        elif arr[i]==22:
            if arr[i+1]=='A':
                count_kompromis+=1

            else:
                count_sopernichestvo+=1

        elif arr[i]==23:
            if arr[i+1]=='A':
                count_sotrudnichestvo+=1

            else:
                count_izbeganie+=1

        elif arr[i]==24:
            if arr[i+1]=='A':
                count_prisposoblenie+=1

            else:
                count_kompromis+=1

        elif arr[i]==25:
            if arr[i+1]=='A':
                count_sopernichestvo+=1

            else:
                count_prisposoblenie+=1

        elif arr[i]==26:
            if arr[i+1]=='A':
                count_kompromis+=1

            else:
                count_sotrudnichestvo+=1

        elif arr[i]==27:
            if arr[i+1]=='A':
                count_izbeganie+=1

            else:
                count_prisposoblenie+=1

        elif arr[i]==28:
            if arr[i+1]=='A':
                count_sopernichestvo+=1

            else:
                count_sotrudnichestvo+=1

        elif arr[i]==29:
            if arr[i+1]=='A':
                count_kompromis+=1

            else:
                count_izbeganie+=1

        else:
            if arr[i+1]=='A':
                count_prisposoblenie+=1

            else:
                count_sotrudnichestvo+=1

    # Сохранение ответов для записи в бд
    arr=[]
    arr.append(count_sopernichestvo)
    arr.append(count_sotrudnichestvo)
    arr.append(count_kompromis)
    arr.append(count_izbeganie)
    arr.append(count_prisposoblenie)

    return arr

# Действия если запускается именно этот файл
if __name__=='__main__':
	pass
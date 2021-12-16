import requests
import xlwt
from xlwt import Workbook

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=BWPAC1SVA01TRJQM")
full_api_data = response.json()
dictionary = {}
daily_info = full_api_data["Time Series (Daily)"]

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

column_counter = 1
index = ""

for month in range(1,11):
    for day in range(1,32):
        
        if int(month) < 10:
            month = "0"+str(month)
        if int(day) < 10:
            day = "0"+str(day)
        try:
            date = "2021-"+str(month)+"-"+str(day)
            index_string  = "2021"+str(month)+str(day)
            index  = int(index_string)
            dictionary[index] = daily_info[date]
            column_counter += 1
            sheet1.write(column_counter, 0, date)
            sheet1.write(column_counter, 1, dictionary[index]["4 .close"])
    
            sheet1.write(column_counter, 3, dictionary[index]["1 .open"])
            sheet1.write(column_counter, 4, dictionary[index]["2 .high"])
            sheet1.write(column_counter, 5, dictionary[index]["3 .low"])
            column_counter += 1
            
        except KeyError:
            data  = -1




A_averages, B_averages, C_averages, D_averages, E_averages, F_averages , G_averages, H_averages= {},{},{},{},{},{},{},{}

# will be updated so that the user can change these MA themselves
A_days, B_days, C_days, D_days, E_days, F_days, G_days, H_days  = 2,3,4,5,6,7,8,9

A_considered, B_considered, C_considered, D_considered, E_considered, F_considered, G_considered, H_considered = 0,0,0,0,0,0,0,0
A_sum, B_sum, C_sum, D_sum, E_sum, F_sum, G_sum, H_sum = 0,0,0,0,0,0,0,0
A_values, B_values, C_values, D_values, E_values, F_values, G_values, H_values = [],[],[],[],[],[],[],[]

# try to get 20 percent matching
# try to find "two nots"

for each in dictionary:
    # moving average A
    if A_considered < A_days:
        A_sum += float(dictionary[each]["4. close"])
        A_averages[each] = float(dictionary[each]["4. close"])
        A_considered += 1
        A_values.append(dictionary[each]["4. close"])
    else:
        A_sum += float(dictionary[each]["4. close"])
        A_values.append(dictionary[each]["4. close"])
        A_sum -= float(A_values.pop(0))
        A_averages[each] = float(A_sum/A_considered)
    
    # moving average B
    if B_considered < B_days:
        B_sum += float(dictionary[each]["4. close"])
        B_averages[each] = float(dictionary[each]["4. close"])
        B_considered += 1
        B_values.append(dictionary[each]["4. close"])
    else:
        B_sum += float(dictionary[each]["4. close"])
        B_values.append(dictionary[each]["4. close"])
        B_sum -= float(B_values.pop(0))
        B_averages[each] = float(B_sum/B_considered)
        
    # moving average C 
    if C_considered < C_days:
        C_sum += float(dictionary[each]["4. close"])
        C_averages[each] = float(dictionary[each]["4. close"])
        C_considered += 1
        C_values.append(dictionary[each]["4. close"])
    else:
        C_sum += float(dictionary[each]["4. close"])
        C_values.append(dictionary[each]["4. close"])
        C_sum -= float(C_values.pop(0))
        C_averages[each] = float(C_sum/C_considered)
        
    # moving average D
    if D_considered < D_days:
        D_sum += float(dictionary[each]["4. close"])
        D_averages[each] = float(dictionary[each]["4. close"])
        D_considered += 1
        D_values.append(dictionary[each]["4. close"])
    else:
        D_sum += float(dictionary[each]["4. close"])
        D_values.append(dictionary[each]["4. close"])
        D_sum -= float(D_values.pop(0))
        D_averages[each] = float(D_sum/D_considered)
    
    # moving average E
    if E_considered < E_days:
        E_sum += float(dictionary[each]["4. close"])
        E_averages[each] = float(dictionary[each]["4. close"])
        E_considered += 1
        E_values.append(dictionary[each]["4. close"])
    else:
        E_sum += float(dictionary[each]["4. close"])
        E_values.append(dictionary[each]["4. close"])
        E_sum -= float(E_values.pop(0))
        E_averages[each] = float(E_sum/E_considered)
        
    # moving average F
    if F_considered < F_days:
        F_sum += float(dictionary[each]["4. close"])
        F_averages[each] = float(dictionary[each]["4. close"])
        F_considered += 1
        F_values.append(dictionary[each]["4. close"])
    else:
        F_sum += float(dictionary[each]["4. close"])
        F_values.append(dictionary[each]["4. close"])
        F_sum -= float(F_values.pop(0))
        F_averages[each] = float(F_sum/F_considered)
        
    # moving average G
    if G_considered < G_days:
        G_sum += float(dictionary[each]["4. close"])
        G_averages[each] = float(dictionary[each]["4. close"])
        G_considered += 1
        G_values.append(dictionary[each]["4. close"])
    else:
        G_sum += float(dictionary[each]["4. close"])
        G_values.append(dictionary[each]["4. close"])
        G_sum -= float(G_values.pop(0))
        G_averages[each] = float(G_sum/G_considered)
        
    # moving average H
    if H_considered < H_days:
        H_sum += float(dictionary[each]["4. close"])
        H_averages[each] = float(dictionary[each]["4. close"])
        H_considered += 1
        H_values.append(dictionary[each]["4. close"])
    else:
        H_sum += float(dictionary[each]["4. close"])
        H_values.append(dictionary[each]["4. close"])
        H_sum -= float(H_values.pop(0))
        H_averages[each] = float(H_sum/H_considered)




# for each in dictionary:
#     print("Date is :" + str(each))
#     print("Moving average for A is:        " +  str(A_averages[each]))
#     print("Moving average for B is:        " +  str(B_averages[each]))
#     print("Moving average for C is:        " +  str(C_averages[each]))
#     print("Moving average for D is:        " +  str(D_averages[each]))
#     print("Moving average for E is:        " +  str(E_averages[each]))
#     print("Moving average for F is:        " +  str(F_averages[each]))
#     print("Moving average for G is:        " +  str(G_averages[each]))
#     print("Moving average for H is:        " +  str(H_averages[each]))
#     print("-------------------------------------------------------------------")


        


import random

all_arrays = {}   
all_arrays_with_num = {} 

index_needs_expression = [0,1,8]
index_needs_equality = [2,5,9,12]
#index_needs_ma = [3,4,6,7,10,11,13,14]

def get_random():
    return random.randint(0, 1)

# let 0 indicate && and <
# let 1 indicate || and >


def random_ma():
    return random.randint(1, 8)


for each in dictionary:
    
    array = []
    array_with_num = []

    for expression in range (100):
        
        curr_exp = []
        curr_exp_num = []
        
        for index in range (15):
            curr_exp.append(None)
            curr_exp_num.append(None)

        for index in range (15):
            if index in index_needs_expression:
                
                if get_random() == 0:
                    curr_exp[index] = "&&"
                    curr_exp_num[index] = "&&"
                    
                else:
                    curr_exp[index] = "||"
                    curr_exp_num[index] = "||"
                    
            elif index in index_needs_equality:
                
                if get_random() == 0:
                    curr_exp[index] = "<"
                    curr_exp_num[index] = "<"
                else:
                    curr_exp[index] = ">"
                    curr_exp_num[index] = ">"
                    
            else:
                picking_random = random_ma()
                
                if picking_random == 1:
                    curr_exp[index] = "MA_2"
                    curr_exp_num[index] = round(A_averages[each],2)
                elif picking_random == 2:
                    curr_exp[index] = "MA_3"
                    curr_exp_num[index] = round(B_averages[each],2)
                elif picking_random == 3:
                    curr_exp[index] = "MA_4"
                    curr_exp_num[index] = round(C_averages[each],2)
                elif picking_random == 4:
                    curr_exp[index] = "MA_5"
                    curr_exp_num[index] = round(D_averages[each],2)
                elif picking_random == 5:
                    curr_exp[index] = "MA_6"
                    curr_exp_num[index] = round(E_averages[each],2)
                elif picking_random == 6:
                    curr_exp[index] = "MA_7"
                    curr_exp_num[index] = round(F_averages[each],2)
                elif picking_random == 7:
                    curr_exp[index] = "MA_8"
                    curr_exp_num[index] = round(G_averages[each],2)
                elif picking_random == 8:
                    curr_exp[index] = "MA_9"
                    curr_exp_num[index] = round(H_averages[each],2)
                    
        array.append(curr_exp)
        array_with_num.append(curr_exp_num)
        
    all_arrays[str(each)] = array
    all_arrays_with_num[str(each)] = array_with_num



def printArray(array):
    for each in array:
        print("-------------------------------------")
        print(each)
        for exp in array[each]:
            try:
                print(exp)
            except ValueError:
                print("Error")


# printArray(all_arrays)
# printArray(all_arrays_with_num)


# for each in all_arrays_with_num:
#     print(len(all_arrays_with_num[each]))





def check_if_less(first, second):
    if first < second:
        return True
    else:
        return False
    
def check_if_greater(first, second):
    if first > second:
        return True
    else:
        return False


for date in all_arrays_with_num:
    
    expression_num = 0
    
    for each in all_arrays_with_num[date]:
        
        if each[2] == "<":
            quarter1 = check_if_less(each[3], each[4])
        else:
            quarter1 = check_if_greater(each[3], each[4])
            
        if each[5] == "<":
            quarter2 = check_if_less(each[6], each[7])
        else:
            quarter2 = check_if_greater(each[6], each[7])
            
        
        if each[9] == "<":
            quarter3 = check_if_less(each[10], each[11])
        else:
            quarter3 = check_if_greater(each[10], each[11])
            
        if each[12] == "<":
            quarter4 = check_if_less(each[13], each[14])
        else:
            quarter4 = check_if_greater(each[13], each[14])
        
        
        
        if each[1] == "||":
            half1 = quarter1 or quarter2
        else:
            half1 = quarter1 and quarter2
            
        if each[8] == "||":
            half2 = quarter3 or quarter4
        else:
            half2 = quarter3 and quarter4
        
        
        if each[0] == "||":
            full = half1 or half2
        else:
            full = half1 and half2
        
        
        
        if full == False:
            del all_arrays_with_num[date][expression_num]
            del all_arrays[date][expression_num]
           
        
        expression_num += 1

# printArray(all_arrays)
# printArray(all_arrays_with_num)

# for each in all_arrays_with_num:
#     print(len(all_arrays_with_num[each]))
#     print(len(all_arrays[each]))
                

#

all_dates = []
for date in all_arrays:
    all_dates.append(date)

# print(all_dates)


for date in all_dates:
    
    algo_num = -1
    for algo in all_arrays[date]:
        algo_num += 1
        
        worked = 0
        tested = 0
        
        for test_date in all_dates:
            avgs = [0,0,0,0,0,0,0,0]
            
            
            # find the A value in ga expression and store into list index 0
            if algo[3] == "MA_2":
                avgs[0] = round(A_averages[int(test_date)], 2)
            elif algo[3] == "MA_3":
                avgs[0] = round(B_averages[int(test_date)], 2)
            elif algo[3] == "MA_4":
                avgs[0] = round(C_averages[int(test_date)], 2)
            elif algo[3] == "MA_5":
                avgs[0] = round(D_averages[int(test_date)], 2)
            elif algo[3] == "MA_6":
                avgs[0] = round(E_averages[int(test_date)], 2)
            elif algo[3] == "MA_7":
                avgs[0] = round(F_averages[int(test_date)], 2)
            elif algo[3] == "MA_8":
                avgs[0] = round(G_averages[int(test_date)], 2)
            elif algo[3] == "MA_9":
                avgs[0] = round(H_averages[int(test_date)], 2)
                
                
            # find the B value in ga expression and store into list index 1
            if algo[4] == "MA_2":
                avgs[1] = round(A_averages[int(test_date)], 2)
            elif algo[4] == "MA_3":
                avgs[1] = round(B_averages[int(test_date)], 2)
            elif algo[4] == "MA_4":
                avgs[1] = round(C_averages[int(test_date)], 2)
            elif algo[4] == "MA_5":
                avgs[1] = round(D_averages[int(test_date)], 2)
            elif algo[4] == "MA_6":
                avgs[1] = round(E_averages[int(test_date)], 2)
            elif algo[4] == "MA_7":
                avgs[1] = round(F_averages[int(test_date)], 2)
            elif algo[4] == "MA_8":
                avgs[1] = round(G_averages[int(test_date)], 2)
            elif algo[4] == "MA_9":
                avgs[1] = round(H_averages[int(test_date)], 2)
                
            
            # find the C value in ga expression and store into list index 2
            if algo[6] == "MA_2":
                avgs[2] = round(A_averages[int(test_date)], 2)
            elif algo[6] == "MA_3":
                avgs[2] = round(B_averages[int(test_date)], 2)
            elif algo[6] == "MA_4":
                avgs[2] = round(C_averages[int(test_date)], 2)
            elif algo[6] == "MA_5":
                avgs[2] = round(D_averages[int(test_date)], 2)
            elif algo[6] == "MA_6":
                avgs[2] = round(E_averages[int(test_date)], 2)
            elif algo[6] == "MA_7":
                avgs[2] = round(F_averages[int(test_date)], 2)
            elif algo[6] == "MA_8":
                avgs[2] = round(G_averages[int(test_date)], 2)
            elif algo[6] == "MA_9":
                avgs[2] = round(H_averages[int(test_date)], 2)
                
                
            # find the D value in ga expression and store into list index 3
            if algo[7] == "MA_2":
                avgs[3] = round(A_averages[int(test_date)], 2)
            elif algo[7] == "MA_3":
                avgs[3] = round(B_averages[int(test_date)], 2)
            elif algo[7] == "MA_4":
                avgs[3] = round(C_averages[int(test_date)], 2)
            elif algo[7] == "MA_5":
                avgs[3] = round(D_averages[int(test_date)], 2)
            elif algo[7] == "MA_6":
                avgs[3] = round(E_averages[int(test_date)], 2)
            elif algo[7] == "MA_7":
                avgs[3] = round(F_averages[int(test_date)], 2)
            elif algo[7] == "MA_8":
                avgs[3] = round(G_averages[int(test_date)], 2)
            elif algo[7] == "MA_9":
                avgs[3] = round(H_averages[int(test_date)], 2)    



            # find the E value in ga expression and store into list index 4
            if algo[10] == "MA_2":
                avgs[4] = round(A_averages[int(test_date)], 2)
            elif algo[10] == "MA_3":
                avgs[4] = round(B_averages[int(test_date)], 2)
            elif algo[10] == "MA_4":
                avgs[4] = round(C_averages[int(test_date)], 2)
            elif algo[10] == "MA_5":
                avgs[4] = round(D_averages[int(test_date)], 2)
            elif algo[10] == "MA_6":
                avgs[4] = round(E_averages[int(test_date)], 2)
            elif algo[10] == "MA_7":
                avgs[4] = round(F_averages[int(test_date)], 2)
            elif algo[10] == "MA_8":
                avgs[4] = round(G_averages[int(test_date)], 2)
            elif algo[10] == "MA_9":
                avgs[4] = round(H_averages[int(test_date)], 2)
                
                
            # find the F value in ga expression and store into list index 5
            if algo[11] == "MA_2":
                avgs[5] = round(A_averages[int(test_date)], 2)
            elif algo[11] == "MA_3":
                avgs[5] = round(B_averages[int(test_date)], 2)
            elif algo[11] == "MA_4":
                avgs[5] = round(C_averages[int(test_date)], 2)
            elif algo[11] == "MA_5":
                avgs[5] = round(D_averages[int(test_date)], 2)
            elif algo[11] == "MA_6":
                avgs[5] = round(E_averages[int(test_date)], 2)
            elif algo[11] == "MA_7":
                avgs[5] = round(F_averages[int(test_date)], 2)
            elif algo[11] == "MA_8":
                avgs[5] = round(G_averages[int(test_date)], 2)
            elif algo[11] == "MA_9":
                avgs[5] = round(H_averages[int(test_date)], 2)
                
            
            # find the G value in ga expression and store into list index 6
            if algo[13] == "MA_2":
                avgs[6] = round(A_averages[int(test_date)], 2)
            elif algo[13] == "MA_3":
                avgs[6] = round(B_averages[int(test_date)], 2)
            elif algo[13] == "MA_4":
                avgs[6] = round(C_averages[int(test_date)], 2)
            elif algo[13] == "MA_5":
                avgs[6] = round(D_averages[int(test_date)], 2)
            elif algo[13] == "MA_6":
                avgs[6] = round(E_averages[int(test_date)], 2)
            elif algo[13] == "MA_7":
                avgs[6] = round(F_averages[int(test_date)], 2)
            elif algo[13] == "MA_8":
                avgs[6] = round(G_averages[int(test_date)], 2)
            elif algo[13] == "MA_9":
                avgs[6] = round(H_averages[int(test_date)], 2)
                
            # find the H value in ga expression and store into list index 7
            if algo[14] == "MA_2":
                avgs[7] = round(A_averages[int(test_date)], 2)
            elif algo[14] == "MA_3":
                avgs[7] = round(B_averages[int(test_date)], 2)
            elif algo[14] == "MA_4":
                avgs[7] = round(C_averages[int(test_date)], 2)
            elif algo[14] == "MA_5":
                avgs[7] = round(D_averages[int(test_date)], 2)
            elif algo[14] == "MA_6":
                avgs[7] = round(E_averages[int(test_date)], 2)
            elif algo[14] == "MA_7":
                avgs[7] = round(F_averages[int(test_date)], 2)
            elif algo[14] == "MA_8":
                avgs[7] = round(G_averages[int(test_date)], 2)
            elif algo[14] == "MA_8":
                avgs[7] = round(H_averages[int(test_date)], 2)
            
            
            
            
            
            if algo[2] == "<":
                quarter1 = check_if_less(avgs[0], avgs[1])
            else:
                quarter1 = check_if_greater(avgs[0], avgs[1])
                
            if algo[5] == "<":
                quarter2 = check_if_less(avgs[2], avgs[3])
            else:
                quarter2 = check_if_greater(avgs[2], avgs[3])
                
            
            if algo[9] == "<":
                quarter3 = check_if_less(avgs[4], avgs[5])
            else:
                quarter3 = check_if_greater(avgs[4], avgs[5])
                
            if algo[12] == "<":
                quarter4 = check_if_less(avgs[6], avgs[7])
            else:
                quarter4 = check_if_greater(each[6], each[7])
            
            
            
            if each[1] == "||":
                half1 = quarter1 or quarter2
            else:
                half1 = quarter1 and quarter2
                
            if each[8] == "||":
                half2 = quarter3 or quarter4
            else:
                half2 = quarter3 and quarter4
            
            
            if each[0] == "||":
                full = half1 or half2
            else:
                full = half1 and half2
            
            
            if full == True:
                worked += 1
            tested += 1
            
        
        algo.append(worked/tested)



# for dates in all_arrays:   
#     for index in range (len(all_arrays[dates])):
#         temp = index - 1
#         while  temp != 0 and ( int(all_arrays[dates][index][15]) < int(all_arrays[dates][temp][15])):
#             curr = all_arrays[dates][index][15]
#             before = all_arrays[dates][temp][15]
#             all_arrays[dates][index] = before
#             all_arrays[dates][temp] = curr
#             temp =- 1
#             
#         
        
for dates in all_arrays:
    print("------------------------------------------------------------------------")
    print("Date is: " + dates)
    
    for each in all_arrays[dates]:
        print(each)
        
        
        
        
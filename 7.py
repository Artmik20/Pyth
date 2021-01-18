import json

with open('file1.txt', 'w') as my_f1:
    with open('file1.txt', 'r') as my_f2:
        subjects = {}
        analytics = {}
        total_profit, profitable_cmp = 0, 0
        lines = my_f2.read().split('\n')
        for company_info in lines:
            company_info = company_info.split()
            profit = int(company_info[2]) - int(company_info[3])
            subjects[company_info[0]] = profit
            if profit > 0:
                total_profit += profit
                profitable_cmp += 1
            analytics['average'] = total_profit / profitable_cmp
        all_list = [subjects, analytics]
    json.dump(all_list, my_f1)




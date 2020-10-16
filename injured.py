import re
import csv
from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup

def main():
    table_data()
    
#HTML抽出
def table_data():
    url = urlopen('https://yakyu-log.info/npb-dl-all-2019/')
    soup = BeautifulSoup(url, 'lxml')
    
    #header
    header = ["選手名", "日付", "詳細"]
    
    #表
    table = soup.findAll("tbody")
    table_data = []
    for i in table:
        for v in i.findAll("td"):
            table_data.append(v.get_text())
        
    #table_data = [s.split() for s in table_data]    
    #print(table_data)
    
    #正規表現で必要なもののみを抽出
    take_date = "\d"
    test_list = []
    for i in table_data:
        if re.match(take_date, i):
            date = i
            date_num = table_data.index(date)
            details_num = date_num + 1
            name_num = date_num -1
            details = table_data[details_num]
            name = table_data[name_num]
            test_list.append(name)
            test_list.append(date)
            test_list.append(details)
            
    n = 3
    per_list =[test_list[idx:idx + n] for idx in range(0,len(test_list), n)]
    print(per_list)

    #CSVへの書き込み
    with open('injured.csv', "wt", newline = "", encoding = 'utf-8') as  csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(header)
        csv_write.writerows(per_list)
        
if __name__ == "__main__":
    main()
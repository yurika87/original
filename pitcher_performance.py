import csv
from urllib.request import urlopen
from lxml import html
from bs4 import BeautifulSoup


def main():
    team_name(rakuten)
    
#チーム別URL
#hiroshima = 'https://baseballdata.jp/2018/6/cptop.html'
#hanshin = 'https://baseballdata.jp/2018/5/cptop.html'
#kyojin = 'https://baseballdata.jp/2018/1/cptop.html'
#yakuruto = 'https://baseballdata.jp/2018/2/cptop.html'
#chunichi = 'https://baseballdata.jp/2018/4/cptop.html'
#dena = 'https://baseballdata.jp/2018/3/cptop.html'
#seibu = 'https://baseballdata.jp/2018/7/cptop.html'
#hamu = 'https://baseballdata.jp/2018/8/cptop.html'
#rotte = 'https://baseballdata.jp/2018/9/cptop.html'
#orikkusu = 'https://baseballdata.jp/2018/11/cptop.html'
#softbank = 'https://baseballdata.jp/2018/12/cptop.html'
rakuten = 'https://baseballdata.jp/2018/376/cptop.html'

#HTML抽出
def team_name(html):
    url = urlopen(html)
    soup = BeautifulSoup(url, 'lxml')
    
    #タイトル
    thead = soup.find("thead")
    tr_title = thead.findAll("tr")
    for i in tr_title:
        title = []
        for v in i.findAll(["th"]):
            title.append(v.get_text())

    title = [s.strip() for s in title]
    del title[2]
    #print(title)
    
    
    #データ
    tbody = soup.find("tbody")
    make_data = []
    for i in tbody.findAll("tr"):
        make_data.append(i.get_text())

    data_replace = [s.replace(',', '') and s.replace(' ','') for s in make_data]
    data = [s.split() for s in data_replace]
    del data[16]
    del data[-1]
    #print(len(data3[0]))
    
    #一軍の'〇'を消す'
    for i in data:
        ichigun = len(i)
        if ichigun == 36:
            del i[2]
        #print(len(i))


    #CSVへの書き込み
    with open('rakuten.csv', "wt", newline = "", encoding = 'utf-8') as  csv_file:
        csv_write = csv.writer(csv_file)
        csv_write.writerow(title)
        csv_write.writerows(data)



if __name__ == "__main__":
    main()
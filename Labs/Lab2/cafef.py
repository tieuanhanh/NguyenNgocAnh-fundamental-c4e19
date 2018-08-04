from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html_content = urlopen(url).read().decode("utf-8")
data = html_content = urlopen(url).read()

f = open("cafef.html", "wb")
f.write(data)
f.close()

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", id = "tableContent")

tr_list = table.find_all("tr")

datas = []

for tr in tr_list:
    td_list = tr.find_all("td")
    data = {}
    if td_list and td_list[0].string is not None:
        data['title'] = (td_list[0].string)
        data['4-2017'] = (td_list[1].string)
        data['1-2018'] = (td_list[2].string)
        data['2-2018'] = (td_list[3].string)
        data['3-2018'] = (td_list[4].string)
    datas.append(data)
    
pyexcel.save_as(records = datas, dest_file_name = "cafef.xlsx")


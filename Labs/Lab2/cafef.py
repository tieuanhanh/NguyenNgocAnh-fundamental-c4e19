from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2018/1/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"

html_content = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_content, "html.parser")
tab = soup.find("table", id = "tableContent")

print (tab)
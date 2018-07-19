from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

#1. Download webpage

url = "http://dantri.com.vn/"
# #1.1 Open a connection
# conn = urlopen(url)
# # #1.2 Read data
# data = conn.read()
# # #1.3 Decode
# info = data.decode("utf-8")
# print(data)

#cach 2:
html_content = urlopen(url).read().decode("utf-8")
# print (html)

#save to file

# html_file= open("dantri.html","wb")
# html_file.write(data)
# html_file.close()

#2. Extract ROI (Region of interest)
# html, xml, xhtml
soup = BeautifulSoup(html_content,"html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew")

# print(ul.prettify())

#3. Extract info
li_list = ul.find_all("li")


# li = li_list[0]
# print(li.prettify())
# print(li_list)
# for li in li_list:
#     a = li.h4.a
#     title = a.string
#     href = url + a['href']
#     print(title)
#     print(href)

#4. Save data to excel

# a_list_of_dictionary = []
# for li in li_list:
#     a = li.h4.a
#     title = a.string
#     href = url + a['href']
#     a_list_of_dictionary.append({"title": title, "link": href})

# pyexcel.save_as(records = a_list_of_dictionary, dest_file_name = "dantri.xlsx")

# code mau:
posts =[]
for li in li_list:
    post ={}
    a = li.h4.a
    title = a.string
    href = url + a['href']
    post['title'] = title
    post['link'] = href
    posts.append(post)
pyexcel.save_as(records = posts, dest_file_name = "dantri2.xlsx")
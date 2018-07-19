from urllib.request import urlopen
url = "http://dantri.com.vn/"
html_content = urlopen(url).read()

f = open("dantri.html", "wb" )
f.write(html_content)
f.close()
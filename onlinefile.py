import urllib.request

data = urllib.request.urlopen("https://srv-store1.gofile.io/download/Wyxj9a/answers")
for line in data:
    st = str(line)
    print(st[:len(st)])

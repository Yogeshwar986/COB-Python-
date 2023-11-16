import pyshorteners
url=input("Enter a url:")
short=pyshorteners.Shortener()
short_1=short.tinyurl.short(url)
print(short_1)


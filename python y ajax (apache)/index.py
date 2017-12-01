#!C:/Program Files/Python36/python.exe
import cgi

print("Content-Type: text/html; charset=utf-8\n\r")
print("")

with open("WebPage1.html") as f:
    print(f.read())


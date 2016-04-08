import os

url = input("Give me url in \"quotation marks\": ")
phrase = input("Give me phrase in \"quotation marks\" which files contain: ")

os.system("python download-exe.py " + url + " " + phrase)
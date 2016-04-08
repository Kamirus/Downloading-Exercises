import os

url = raw_input("Give me url: ")
phrase = raw_input("Give me phrase which files contain: ")

os.system("python download-exe.py " + url + " " + phrase)
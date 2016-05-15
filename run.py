import os

url = raw_input("Give me url: ")
phrase = raw_input("Give me EXACT phrase which file addresses contain: ")

os.system("python download-exe.py " + url + " " + phrase)
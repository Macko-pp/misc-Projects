import os

fileName = input("Enter the name of the file you want to hide: \n   >>> ")

os.system("mv ~/Desktop/" + fileName + " ~/Desktop/." + fileName)

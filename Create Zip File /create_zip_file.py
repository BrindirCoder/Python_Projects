import zipfile

with zipfile.ZipFile("test.zip", "w") as file:   # test.zip it will be your zip file name 
    file.write("info.txt")   # a file that you want to make it zip file 

import zipfile

with zipfile.ZipFile("test.zip", "r") as file:
    print(file.namelist())  # Show files inside the zip
    file.extract("test.html") # it will extract only one file you write their name   
    file.extractall()  # Extract all files

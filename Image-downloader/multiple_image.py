url = (
    "https://i.pinimg.com/736x/67/b7/5e/67b75e913fd5edee102a3292298c0552.jpg",
    "https://i.pinimg.com/736x/d8/52/8a/d8528a4a64dcacb72f3b4ac969d00c29.jpg",
    "https://i.pinimg.com/736x/6c/0a/25/6c0a254bc1e6e6191cdecf6c32dccce3.jpg",
    "https://i.pinimg.com/736x/c3/47/55/c3475550db1f37bfa26a9cb6913d3ac3.jpg",
)

for img in url:
    x = img.split("/")[-1]
    data = requests.get(img)
    with open(x, "wb") as file:
        file.write(data.content

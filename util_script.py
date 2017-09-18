import sys

with open(sys.argv[1], "rb") as file:
    pdf = file.read()

img_counter = 0
pointer = 0
while True:
    pointer = pdf.find(b"stream", pointer)
    if pointer < 0:
        break

    x = pdf.find(b"\xff\xd8", pointer)
    if x < 0:
        pointer = pointer + 1
        continue
    else:
        extension = "jpg"

    limit = pdf.find(b"endstream", pointer)
    if limit < 0:
        break

    y = pdf.find(b"\xff\xd9", pointer, limit) + 2

    pointer = limit + 9
    if y < 2:
        continue        
    
    img = pdf[x:y]

    img_counter = img_counter + 1
    with open("img_" + str(img_counter) + "." + extension, "wb") as jpgfile:
        jpgfile.write(img)

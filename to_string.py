import pymongo
import os
import base64

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["medix_db"]
collection = db["pateints"]



# Assuming the image file is named 'example.jpg', modify the filename if needed
image_filename = "image.png"

# Construct the full path to the image file
image_path = os.path.join(os.getcwd(), image_filename)

# Read the image file as binary data
with open(image_path, "rb") as image_file:
    # Convert the binary data to a Base64 string
    base64_string = base64.b64encode(image_file.read()).decode("utf-8")

dictionary={
    '_id':'Image',
    'string': base64_string
}

# Print the Base64 string
collection.insert_one(dictionary)



# import base64
# with open("images/test.jpg", "rb") as imagetostring:
#     converted_string = base64.b64encode(imagetostring.read())
# print(converted_string)

# with open('encode.bin', "wb") as file:
#     file.write(converted_string)
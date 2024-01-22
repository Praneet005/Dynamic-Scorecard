import json

# Specify the path to your JSON file
json_file_path = "/Users/vishalkannan/Downloads/odis_json/64836.json"

# Open the JSON file and load its contents into a dictionary
with open(json_file_path, 'r') as file:
    data_as_dict = json.load(file)

# Now, data_as_dict contains the contents of the JSON file as a Python dictionary
print(type(data_as_dict))

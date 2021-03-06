# import json
# import requests
# from sqlalchemy import func


# INPUT_FILE_NAME = "ac_app.json"
OUTPUT_FILE_NAME = "output.py"

# input_file = open(INPUT_FILE_NAME)
output_file = open(OUTPUT_FILE_NAME, "w")

# data = json.load(input_file)

# # Import statements
# imports = """import requests\nimport json\nimport random\n\n"""
# output_file.write(imports)

# # For getting public ip
# get_public_ip = "def get_public_ip():\n"
# get_public_ip += '\tresp = requests.get("http://api.ipify.org/").content.decode()\n'
# get_public_ip += "\treturn resp\n\n"
# output_file.write(get_public_ip)

# # Storing URLs
# urls = "pub_ip = get_public_ip()\n"
# urls += 'sensor_url = f"http://{pub_ip}:5000/"\n'
# urls += 'model_url = f"http://{pub_ip}:5003/"\n'
# urls += 'controller_url = f"http://{pub_ip}:5002/"\n\n'
# output_file.write(urls)

# definition = "def get_details(name):\n"
# for function in data["function_details"]:
# # print(function)
#     details = data['function_details'][function]
#     definition += '\tif name == "'+ function +'":\n'
#     definition += '\t\t'+function+'_details = {'
#     for key, value in details.items():
#         # print(key, value)
#         definition += '"' + key + '": "' +str(value) + '",'
#     definition = definition[:-1] + '}\n'
#     definition += '\t\treturn '+function+'_details\n\n'
# output_file.write(definition)


# sensor_data = 'def get_sensor_data(name):\n'
# sensor_data += '\tdetails = get_details(name)\n'
# sensor_data += '\tjsonObj = {"sensor_type": details["sensor_type"], "sensor_location": details["sensor_location"] }\n'
# sensor_data += '\tresponse = requests.post(url=sensor_url+'+'"getSensorInstances"'+', json=jsonObj).content\n'
# sensor_data += '\tdata = json.loads(response.decode())\n'
# sensor_data += '\tall_instances = data["sensor_instances"]\n'
# sensor_data += '\tsensor_instances = random.sample(all_instances, str(details["no_of_instances"]))\n'
# sensor_data += '\tdata = []\n'
# sensor_data += '\tfor i in range(len(sensor_instances)):\n'
# sensor_data += '\t\tjsonObj = {"topic_name": sensor_instances[i]}\n'
# sensor_data += '\t\tresponse = requests.post(url=sensor_url+'+'"getSensorData"'+', json=jsonObj).content\n'
# sensor_data += '\t\tdata = json.loads(response.decode())\n'
# sensor_data += '\t\tdata = data["sensor_data"]\n'
# sensor_data += '\t\tdata.append(data[-1])\n'
# sensor_data += '\treturn data\n\n'
# # print(sensor_data)
# output_file.write(sensor_data)

# predict = 'def predict(name, data):\n'
# predict += '\tdetails = get_details(name)\n'
# predict += '\tjsonObj = {"data": data.tolist(), "model_name": details["model_name"] }\n'
# predict += '\tresponse = requests.post(url=model_url+'+'"predict"'+', json=jsonObj).content\n'
# predict += '\tdata = json.loads(response.decode())\n'
# predict += '\tprediction = data["predicted_value"]\n'
# predict += '\treturn prediction\n\n'
# # print(predict)
# output_file.write(predict)

# controller = 'def controller_action(name, data):\n'
# controller += '\tdetails = get_details(name)\n'
# controller += '\tresults = []\n'
# controller += '\tfor controller in details["controllers"]:\n'
# controller += '\t\tjsonObj = {"sensor_type": controller["controller_type"], "sensor_location": controller["controller_location"]}\n'
# controller += '\t\tresponse = requests.post(url=controller_url+'+'"getControlInstances"'+', json=jsonObj).content\n'
# controller += '\t\tdata = json.loads(response.decode())\n'
# controller += '\t\tall_instances = data["control_instances"]\n'
# controller += '\t\tinstance = all_instances[0]\n'
# controller += '\t\tjsonObj = {"sensor_type": instance["sensor_type"], "sensor_ip": instance["sensor_ip"], "sensor_port": instance["sensor_port"], "data": int(data)}\n'
# controller += '\t\tresponse = requests.post(url=controller_url+'+'"performAction"'+', json=jsonObj).content\n'
# controller += '\t\tresults.append(response.decode())\n'
# controller += '\treturn results\n\n'

# output_file.write(controller)

import imp
from io import BytesIO
import json
import pymongo
import requests
import base64
from PIL import Image
import numpy as np
import cv2

client = "mongodb://ias_mongo_user:ias_password@cluster0-shard-00-00.doy4v.mongodb.net:27017,cluster0-shard-00-01.doy4v.mongodb.net:27017,cluster0-shard-00-02.doy4v.mongodb.net:27017/ias_database?ssl=true&replicaSet=atlas-ybcxil-shard-0&authSource=admin&retryWrites=true&w=majority"
db_name = "ias_database"
client = pymongo.MongoClient(client)
mydb = client[db_name]
instancesdb = mydb["attendance_images"]

img = instancesdb.find({"id": 1})
for i in img:
    # print(i["data"])
    data = i["data"]
# print(json.dumps(data[0]))
print(type(data))

im_bytes = base64.b64decode(data)
im_file = BytesIO(im_bytes)
img = Image.open(im_file)
print(type(img))
img.show()

# im_arr = np.frombuffer(im_bytes, dtype=np.uint8)
# img = cv2.imdecode(im_arr, flags=cv2.IMREAD_COLOR)
# d = base64.b64encode(bytes(data, 'utf-8'))

# print(type(d))
# stream = BytesIO(d)
# img = Image.open(stream).convert("RGB")
# stream.close()
# print(img.shape)

# response = requests.post(url="http://20.204.64.34:40006/predict", json={
#     "data": data
# }).content


imports = """import requests\nimport json\nimport random\n\nimport pymongo\n"""
output_file.write(imports)

# For getting public ip

get_public_ip = "\n"

get_public_ip += 'client = "mongodb://ias_mongo_user:ias_password@cluster0-shard-00-00.doy4v.mongodb.net:27017,cluster0-shard-00-01.doy4v.mongodb.net:27017,cluster0-shard-00-02.doy4v.mongodb.net:27017/ias_database?ssl=true&replicaSet=atlas-ybcxil-shard-0&authSource=admin&retryWrites=true&w=majority"\n'
get_public_ip += 'db_name = "ias_database"\n'
get_public_ip += 'client = pymongo.MongoClient(client)\n'
get_public_ip += 'mydb = client[db_name]\n'


get_public_ip += "\n"

get_public_ip += "def get_public_ip():\n"
get_public_ip += '\tvm_ips_coll = mydb["vm_ips"]\n'
get_public_ip += '\tmodel_vm = vm_ips_coll.find_one({"_id": "servicevm"})\n'
get_public_ip += '\tmodel_vm_ip = model_vm["vm_ip"]\n'
get_public_ip += '\tmodel_vm_ip = model_vm_ip.replace(\'"\', "")\n'
get_public_ip += '\tmodel_vm_ip = model_vm_ip.replace("\'", "")\n'


# get_public_ip += '\tresp = requests.get("http://api.ipify.org/").content.decode()\n'
get_public_ip += "\treturn model_vm_ip\n\n"
output_file.write(get_public_ip)

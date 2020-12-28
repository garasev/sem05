import pprint
import json
json1_file = open('D:\git\p0rn\cg\Constructor3D\castle.scene')
json1_str = json1_file.read()
json1_data = json.loads(json1_str)
pprint.pprint(json1_data)

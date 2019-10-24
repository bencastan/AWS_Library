import json
from smart_open import open
from smart_open import smart_open

def get_policy_from_s3():
    with open("s3://appen-its-admin/role/pe-sftp-stage-user-scope-down-policy.json", 'r') as f:
        data = json.load(f)

    return data

#print(get_policy_from_s3())
data = ''
# stream lines from an S3 object
def get_policy_from_s3_proper_json():
    
    for line in open('s3://appen-its-admin/role/pe-sftp-stage-user-scope-down-policy.json', 'rb'):
        data.join(line.decode('utf8'))
    return data


print(get_policy_from_s3_proper_json())

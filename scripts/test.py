#/usr/bin/python3
from pprint import pprint

import requests


with open("upload_response.txt") as f:
    output = f.read()
    id_and_right = output.split('"id":"')[-1]
    id_ = id_and_right.split('","meta"')[0]
    print("Patient uploaded. Patient has id: ", id_)

    url = f"https://stu3.test.pyrohealth.net/fhir/Patient/{id_}"
    r = requests.get(url, headers={"Accept": "application/fhir+json"})
    pprint(r.json())

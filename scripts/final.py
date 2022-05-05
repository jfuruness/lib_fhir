from pathlib import Path
from subprocess import check_call
from pprint import pprint

import requests


def main():
    path = Path(__file__).parent / "upload.sh"

    print("uploading patient")
    check_call("bash " + str(path), shell=True)

    with open("/tmp/upload_response.txt") as f:
        output = f.read()
        id_and_right = output.split('"id":"')[-1]
        id_ = id_and_right.split('","meta"')[0]
        print("Patient uploaded. Patient has id: ", id_)

        print("Retrieving patient info")
        url = f"https://stu3.test.pyrohealth.net/fhir/Patient/{id_}"
        r = requests.get(url, headers={"Accept": "application/fhir+json"})
        patient_json = r.json()
        pprint(patient_json)
        print("Patient info retrieved")


        print("Updating patient info")
        patient_json["birthDate"] = "2000-01-01"
        r = requests.put(url,
                         json=patient_json,
                         headers={"Accept": "application/fhir+json",
                                  "Content-Type": "application/fhir+json"})
        patient_json = r.json()
        pprint(patient_json)
        print("Patient info updated")

        print("Deleting patient info")
        r = requests.delete(url)
        if str(r.status_code) == "204":
            print("Status code is 204, patient was deleted")

if __name__ == "__main__":
    main()

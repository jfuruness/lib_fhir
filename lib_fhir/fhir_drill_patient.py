from pathlib import Path
from subprocess import check_call

from .fhir_patient import FHIRPatient


class FHIRDrillPatient(FHIRPatient):

    def upload_patient(self) -> str:
        """Uploads patient to FHIR server, returning ID"""

        path = Path(__file__).parent.parent / "scripts" / "upload.sh"

        print("uploading patient")
        check_call("bash " + str(path), shell=True)

        with open("/tmp/upload_response.txt") as f:
            output = f.read()
            id_and_right = output.split('"id":"')[-1]
            id_ = id_and_right.split('","meta"')[0]
            print("Patient Uploaded")
            return id_

    @property
    def url(self) -> str:
        """Returns URL"""

        return "https://stu3.test.pyrohealth.net/fhir/Patient/"

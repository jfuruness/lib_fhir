from abc import abstractmethod, ABC
from pprint import pprint

import requests


class FHIRPatient(ABC):

    def __init__(self):
        self.patient_id = self.upload_patient()

    @property
    def patient_url(self) -> str:
        """Returns URL of the patient"""

        return self.url + self.patient_id

    def perform_operations(self):
        """Performs basic FHIR operations on a patient"""

        # NOTE: initial upload was done in the upload_patient abstract method
        patient_json = self.get_patient()
        self.update_patient(patient_json)
        self.delete_patient()

    def get_patient(self) -> dict:
        """Gets patient"""

        print("Retrieving patient info")
        r = requests.get(self.patient_url,
                         headers={"Accept": "application/fhir+json"})
        patient_json = r.json()
        pprint(patient_json)
        print("Patient info retrieved")
        return patient_json

    def update_patient(self, update_json) -> dict:
        """Update's patients birthday (can do any arbitrary update)"""

        update_json["birthDate"] = "2000-01-01"
        r = requests.put(self.patient_url,
                         json=update_json,
                         headers={"Accept": "application/fhir+json",
                                  "Content-Type": "application/fhir+json"})
        patient_json = r.json()
        pprint(patient_json)
        print("Patient info updated")

    def delete_patient(self):
        """Deletes patient"""

        print("Deleting patient info")
        r = requests.delete(self.patient_url)
        if str(r.status_code) == "204":
            print("Status code is 204, patient was deleted")
        print("Deleted patient")

##########################################
# Abstract Methods Requiring Inheritance #
##########################################

    @abstractmethod
    def upload_patient(self) -> str:
        """Uploads patient to FHIR server, returning ID"""

        raise NotImplementedError

    @property
    @abstractmethod
    def url(self):
        """Returns URL"""

        raise NotImplementedError

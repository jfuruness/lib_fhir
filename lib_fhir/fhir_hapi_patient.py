import requests

from .fhir_patient import FHIRPatient


class FHIRHAPIPatient(FHIRPatient):

    def upload_patient(self) -> str:
        """Uploads patient to FHIR server, returning ID"""

        # Using existing patient since server blocks upload requestss
        r = requests.get(
            "http://hapi.fhir.org/baseR4/Patient"
            "?_count=1&_format=json&_pretty=true",
            headers={
                "Accept-Charset": "utf-8",
                "Accept": ("application/fhir+json;q=1.0, "
                           "application/json+fhir;q=0.9"),
                "User-Agent": ("HAPI-FHIR/6.0.0-PRE8-SNAPSHOT "
                               "(FHIR Client; FHIR 4.0.1/R4; apache"),
                "Accept-Encoding": "gzip"})
        data = r.json()
        id_ = data["entry"][0]["resource"]["id"]
        print(f"HaPI FHIR Patient with id {id}")
        return id_

    @property
    def url(self) -> str:
        """Returns URL"""

        return "http://hapi.fhir.org/baseR4/Patient/"

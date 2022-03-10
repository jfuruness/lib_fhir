import requests


class FHIR:
    """Data manipulation with FHIR"""

    def run(self):
        """Runs FHIR"""

        self.upload_patient()
        raise NotImplementedError

    def upload_patient(self) -> str:
        """Uploads patient to FHIR"""
        headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
            'Accept': 'application/json; charset=utf-8',
            'Prefer': 'return=representation',
            'Content-Type': 'application/json',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36',
            'sec-ch-ua-platform': '"Linux"',
            'Origin': 'https://fhir-drills.github.io',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://fhir-drills.github.io/',
            'Accept-Language': 'en-US,en;q=0.9',
        }

        data = {"resourceType": "Patient",
                "maritalStatus": {"coding": [{"code": "M",
                                              "display": "Married",
                                              "system":"http://hl7.org/fhir/v3/MaritalStatus"}]},
                "text": {"status": "generated",
                         "div": "<div xmlns': '\'http://www.w3.org/1999/xhtml\'>\\n  <p>Patient: Fhirman, Sam</p>\\n</div>"},
                         "identifier": [{"system": "http://ns.electronichealth.net.au/id/hi/ihi/1.0",
                                         "value":"8003608166690503",
                                         "type": {"coding": [{"code": "NI",
                                                              "display":"National unique individual identifier",
                                                              "system": "http://hl7.org/fhir/v2/0203"}],
                                                  "text": "IHI"}},
                                        {"system": "urn:oid:1.2.36.146.595.217.0.1",
                                         "period": {"start": "2001-05-06"},
                                         "use": "usual",
                                         "type": {"coding": [{"system": "http://hl7.org/fhir/v2/0203",
                                                              "code":"MR"}]},
                                                  "assigner": {"display": "Acme Healthcare"},
                                                  "value": "6666"}],
                                         "telecom": [{"system": "phone",
                                                      "use": "mobile",
                                                      "value": " 61481059995"}],
                                         "birthDate": "1973-09-30",
                                         "gender": "male",
                                         "address": [{"postalCode": "4000",
                                                      "use": "work",
                                                      "line": ["400 George Street"],
                                                      "city": "Brisbane",
                                                      "country": "AUS",
                                                      "state": "QLD"}],
                                         "name": [{"use": "official",
                                                   "text":"Sam Fhirman",
                                                   "prefix": ["Mr"],
                                                   "family": ["Fhirman"],
                                                   "given": ["Sam"]}]}
        response = requests.post('https://stu3.test.pyrohealth.net/fhir/Patient', headers=headers, json=data)
        print(response.text)

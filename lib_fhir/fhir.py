from typing import Tuple

from .fhir_patient import FHIRPatient
from .fhir_drill_patient import FHIRDrillPatient
from .fhir_hapi_patient import FHIRHAPIPatient


class FHIR:

    def run_patients(self):
        """Runs all patient types"""

        for PatientCls in self.supported_patient_classes:
            PatientCls().perform_operations()

    @property
    def supported_patient_classes(self) -> Tuple[FHIRPatient]:
        """Returns a list of all supported FHIR patients"""

        return (FHIRHAPIPatient, FHIRDrillPatient)

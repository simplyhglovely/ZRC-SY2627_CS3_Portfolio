class Patient:
    def __init__(self, name, bill_amount):
        self.__name = name
        self.__bill_amount = bill_amount

    def get_name(self):
        return self.__name

    def get_bill_amount(self):
        return self.__bill_amount

    def set_name(self, name):
        self.__name = name

    def set_bill_amount(self, bill_amount):
        if bill_amount >= 0:
            self.__bill_amount = bill_amount
        else:
            raise ValueError("Bill Amount Cannot Be Negative.")

    def calculate_bill(self):
        return self.__bill_amount


class SeniorPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.80


class PhilHealthPatient(Patient):
    def calculate_bill(self):
        return self.get_bill_amount() * 0.85


regular_patient = Patient("Venice Nicole Gonzales", 15000)
senior_patient = SeniorPatient("Yeshua Sigue", 15000)
philhealth_patient = PhilHealthPatient("Ayni Pahamtang", 15000)

patients = [
    regular_patient, 
    senior_patient, 
    philhealth_patient
]

print("HOSPITAL BILLING SYSTEM")
print("=" * 40)
for patient in patients:
    print("Patient Name:", patient.get_name())
    print("Original Bill: PHP", format(patient.get_bill_amount(), ",.2f"))
    print("Final Bill: PHP", format(patient.calculate_bill(), ",.2f"))
    print("-" * 40)

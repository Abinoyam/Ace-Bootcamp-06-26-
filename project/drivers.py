class Driver:

    def __init__(self, driver_id, name, license_number, contact):

        self.driver_id = driver_id
        self.name = name

        self._license_number = None
        self._contact = None

        self.license_number = license_number
        self.contact = contact

    @property
    def license_number(self):
        return self._license_number

    @license_number.setter
    def license_number(self, value):

        if len(value) == 16:
            self._license_number = value
        else:
            raise ValueError("License Number must contain exactly 16 characters.")

    @property
    def contact(self):
        return self._contact

    @contact.setter
    def contact(self, value):

        if value.isdigit() and len(value) == 10:
            self._contact = value
        else:
            raise ValueError("Contact Number must contain exactly 10 digits.")

    @contact.deleter
    def contact(self):

        print("Contact deleted successfully.")
        del self._contact

    def display_info(self):

        print("-" * 45)
        print("Driver ID      :", self.driver_id)
        print("Driver Name    :", self.name)
        print("License Number :", self.license_number)

        if hasattr(self, "_contact"):
            print("Contact Number :", self.contact)
        else:
            print("Contact Number : Deleted")

        print("-" * 45)

    def __str__(self):
        return f"Driver [{self.driver_id}] - {self.name}"

    def __repr__(self):
        return (
            f"Driver(driver_id='{self.driver_id}', "
            f"name='{self.name}', "
            f"license_number='{self.license_number}')"
        )
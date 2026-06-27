class Driver:

    def __init__(self, driver_id, name, license_number, contact):
        # Public instance variables
        self.driver_id = driver_id
        self.name      = name
        # Private variables (controlled via properties)
        self._license_number = None
        self._contact        = None
        # Use setters for validation on init
        self.license_number = license_number
        self.contact        = contact

    # ==========================================
    # PROPERTY: license_number
    # ==========================================

    # GETTER - return _license_number safely
    @property
    def license_number(self):
        return self._license_number

    # SETTER - validate must be exactly 16 characters
    @license_number.setter
    def license_number(self, value):
        if not isinstance(value, str) or len(value) != 16:
            raise ValueError(
                f"  [ERROR] License number must be exactly 16 characters. "
                f"Got {len(value)} character(s)."
            )
        self._license_number = value

    # ==========================================
    # PROPERTY: contact
    # ==========================================

    # GETTER - return _contact safely
    @property
    def contact(self):
        return self._contact

    # SETTER - validate must be exactly 10 digits
    @contact.setter
    def contact(self, value):
        if not isinstance(value, str) or not value.isdigit() or len(value) != 10:
            raise ValueError(
                "  [ERROR] Contact number must be exactly 10 digits (numbers only)."
            )
        self._contact = value

    # DELETER - remove _contact with confirmation message
    @contact.deleter
    def contact(self):
        print(f"  [INFO] Contact number for driver '{self.name}' has been deleted.")
        del self._contact

    # ------------------------------------------
    # Display complete driver information
    def display_info(self):
        contact = getattr(self, '_contact', 'N/A (deleted)')
        print(f"  Driver ID      : {self.driver_id}")
        print(f"  Name           : {self.name}")
        print(f"  License Number : {self.license_number}")
        print(f"  Contact        : {contact}")

    def __str__(self):
        return f"Driver [{self.driver_id}] | {self.name} | License: {self.license_number}"

    def __repr__(self):
        return f"Driver(driver_id='{self.driver_id}', name='{self.name}')"


# ------------------------------------------
if __name__ == "__main__":
    print("=== Drivers Module Test ===\n")

    d1 = Driver("DRV001", "Ravi Kumar", "MH1234567890ABCD", "9876543210")
    d1.display_info()

    print("\n  --- Updating contact ---")
    d1.contact = "9000011111"
    print(f"  New Contact: {d1.contact}")

    print("\n  --- Deleting contact ---")
    del d1.contact

    print("\n  --- Validation Error Tests ---")
    try:
        d1.license_number = "SHORT"
    except ValueError as e:
        print(e)

    try:
        d1.contact = "12345ABC"
    except ValueError as e:
        print(e)

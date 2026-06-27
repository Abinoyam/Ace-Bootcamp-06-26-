import re

# ==========================================
# BASE CLASS: Vehicle
# ==========================================
class Vehicle:

    # ------------------------------------------
    # CLASS VARIABLES - Shared by all instances
    college_name    = "ACE Engineering College"
    total_vehicles  = 0

    def __init__(self, vehicle_id, vehicle_type, capacity):
        # ------------------------------------------
        # INSTANCE VARIABLES - Unique to each object
        self.vehicle_id   = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity     = capacity
        # Increment class-level counter
        Vehicle.total_vehicles += 1

    # ------------------------------------------
    # CLASS METHOD
    # Returns total number of vehicles registered
    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    # ------------------------------------------
    # STATIC METHOD
    # Validates vehicle_id format "AP28ZXXXX" (state code + digits + letter + digits)
    @staticmethod
    def validate_vehicle_id(vehicle_id):
        # Pattern: 2 letters, 2 digits, 1 letter, 4 digits  e.g. AP28Z1234
        pattern = r'^[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}$'
        return bool(re.match(pattern, vehicle_id.upper()))

    # ------------------------------------------
    # Display basic vehicle information
    def display_info(self):
        print(f"  Vehicle ID   : {self.vehicle_id}")
        print(f"  Type         : {self.vehicle_type}")
        print(f"  Capacity     : {self.capacity} seats")
        print(f"  College      : {Vehicle.college_name}")


# ==========================================
# SUBCLASS 1: Bus
# ==========================================
class Bus(Vehicle):

    def __init__(self, vehicle_id, capacity, route_number, has_ac=False):
        # Call parent __init__ using super()
        super().__init__(vehicle_id, "Bus", capacity)

        # Bus-specific instance variables
        self.route_number = route_number
        self.has_ac       = has_ac

    # ------------------------------------------
    # __str__: Human-readable info for print()
    def __str__(self):
        ac_status = "Yes" if self.has_ac else "No"
        return (f"Bus [{self.vehicle_id}] | Route: {self.route_number} "
                f"| Capacity: {self.capacity} | AC: {ac_status}")

    # ------------------------------------------
    # __repr__: Developer-readable representation
    def __repr__(self):
        return (f"Bus(vehicle_id='{self.vehicle_id}', "
                f"route={self.route_number}, capacity={self.capacity})")

    # ------------------------------------------
    # Display route-specific information
    def display_route_info(self):
        print(f"  Route Number : {self.route_number}")
        print(f"  AC Available : {'Yes' if self.has_ac else 'No'}")

    # ------------------------------------------
    # Override display_info from Vehicle
    def display_info(self):
        print(f"  Vehicle ID   : {self.vehicle_id}")
        print(f"  Type         : {self.vehicle_type}")
        print(f"  Capacity     : {self.capacity} seats")
        print(f"  Route Number : {self.route_number}")
        print(f"  AC Available : {'Yes' if self.has_ac else 'No'}")
        print(f"  College      : {Vehicle.college_name}")


# ==========================================
# SUBCLASS 2: MiniVan
# ==========================================
class MiniVan(Vehicle):

    def __init__(self, vehicle_id, capacity, trip_purpose):
        # Call parent __init__ using super()
        super().__init__(vehicle_id, "MiniVan", capacity)

        # MiniVan-specific instance variable
        self.trip_purpose = trip_purpose

    # ------------------------------------------
    # __str__: Human-readable info for print()
    def __str__(self):
        return f"MiniVan [{self.vehicle_id}] | Purpose: {self.trip_purpose}"

    # ------------------------------------------
    # __repr__: Developer-readable representation
    def __repr__(self):
        return (f"MiniVan(vehicle_id='{self.vehicle_id}', "
                f"capacity={self.capacity}, purpose='{self.trip_purpose}')")

    # ------------------------------------------
    # Override display_info from Vehicle
    def display_info(self):
        print(f"  Vehicle ID   : {self.vehicle_id}")
        print(f"  Type         : {self.vehicle_type}")
        print(f"  Capacity     : {self.capacity} seats")
        print(f"  Trip Purpose : {self.trip_purpose}")
        print(f"  College      : {Vehicle.college_name}")


# ------------------------------------------
if __name__ == "__main__":
    print("=== Vehicles Module Test ===\n")

    # Test validation
    print(f"  Validate 'AP28Z1234' : {Vehicle.validate_vehicle_id('AP28Z1234')}")
    print(f"  Validate 'INVALID99' : {Vehicle.validate_vehicle_id('INVALID99')}\n")

    bus1 = Bus("AP28Z1234", 50, 3, has_ac=True)
    bus2 = Bus("AP28Z5678", 45, 1, has_ac=False)
    van1 = MiniVan("TN05AB6789", 12, "Industrial Visit")

    print(str(bus1))
    print(repr(bus1))
    print()
    print(str(van1))
    print(repr(van1))
    print()

    print(f"  Total Vehicles: {Vehicle.get_total_vehicles()}\n")

    print("  --- Bus display_info ---")
    bus1.display_info()
    print("\n  --- MiniVan display_info ---")
    van1.display_info()

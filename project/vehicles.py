import re


class Vehicle:

    college_name = "ACE Engineering College"
    total_vehicles = 0

    def __init__(self, vehicle_id, vehicle_type, capacity):

        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.capacity = capacity

        Vehicle.total_vehicles += 1

    @classmethod
    def get_total_vehicles(cls):
        return cls.total_vehicles

    @staticmethod
    def validate_vehicle_id(vehicle_id):

        pattern = r"^(TG|TS|AP)\d{2}[A-Z]{1,2}\d{4}$"
        return bool(re.match(pattern, vehicle_id.upper()))

    def display_info(self):

        print("-" * 50)
        print("Vehicle ID :", self.vehicle_id)
        print("Type       :", self.vehicle_type)
        print("Capacity   :", self.capacity)
        print("College    :", Vehicle.college_name)
        print("-" * 50)


class Bus(Vehicle):

    def __init__(self, vehicle_id, capacity, route_number, has_ac=False):

        super().__init__(vehicle_id, "Bus", capacity)

        self.route_number = route_number
        self.has_ac = has_ac

    def __str__(self):

        ac = "Yes" if self.has_ac else "No"

        return (
            f"Bus [{self.vehicle_id}] | "
            f"Route : {self.route_number} | "
            f"Capacity : {self.capacity} | "
            f"AC : {ac}"
        )

    def __repr__(self):

        return (
            f"Bus(vehicle_id='{self.vehicle_id}', "
            f"route={self.route_number}, "
            f"capacity={self.capacity})"
        )

    def display_route_info(self):

        print("Route Number :", self.route_number)
        print("AC Available :", "Yes" if self.has_ac else "No")

    def display_info(self):

        print("-" * 50)
        print(self)
        self.display_route_info()
        print("-" * 50)


class MiniVan(Vehicle):

    def __init__(self, vehicle_id, capacity, trip_purpose):

        super().__init__(vehicle_id, "MiniVan", capacity)

        self.trip_purpose = trip_purpose

    def __str__(self):

        return (
            f"MiniVan [{self.vehicle_id}] | "
            f"Purpose : {self.trip_purpose}"
        )

    def __repr__(self):

        return (
            f"MiniVan(vehicle_id='{self.vehicle_id}', "
            f"capacity={self.capacity}, "
            f"trip_purpose='{self.trip_purpose}')"
        )

    def display_info(self):

        print("-" * 50)
        print(self)
        print("Capacity :", self.capacity)
        print("-" * 50)
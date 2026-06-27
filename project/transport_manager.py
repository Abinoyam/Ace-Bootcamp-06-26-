from vehicles import Bus, MiniVan, Vehicle
from drivers import Driver
from students import Student


class TransportManager:

    def __init__(self, manager_name):

        self.manager_name = manager_name
        self.buses = []
        self.mini_vans = []
        self.drivers = []
        self.students = []

    def add_bus(self, bus_obj):

        if isinstance(bus_obj, Bus):
            self.buses.append(bus_obj)
            print("Bus Added Successfully.")
        else:
            print("Invalid Bus Object.")

    def add_minivan(self, van_obj):

        if isinstance(van_obj, MiniVan):
            self.mini_vans.append(van_obj)
            print("MiniVan Added Successfully.")
        else:
            print("Invalid MiniVan Object.")

    def add_driver(self, driver_obj):

        if isinstance(driver_obj, Driver):
            self.drivers.append(driver_obj)
            print("Driver Added Successfully.")
        else:
            print("Invalid Driver Object.")

    def add_student(self, student_obj):

        if isinstance(student_obj, Student):
            self.students.append(student_obj)
            print("Student Registered Successfully.")
        else:
            print("Invalid Student Object.")

    def display_all_vehicles(self):

        all_vehicles = self.buses + self.mini_vans

        if not all_vehicles:
            print("\nNo Vehicles Available.")
            return

        print("\n========== VEHICLES ==========")

        for vehicle in all_vehicles:
            vehicle.display_info()

    def display_all_drivers(self):

        if not self.drivers:
            print("\nNo Drivers Available.")
            return

        print("\n========== DRIVERS ==========")

        for driver in self.drivers:
            driver.display_info()

    def display_all_students(self):

        if not self.students:
            print("\nNo Students Registered.")
            return

        print("\n========== STUDENTS ==========")

        for student in self.students:
            student.display_info()

    def search_vehicle(self, vehicle_id):

        all_vehicles = self.buses + self.mini_vans

        for vehicle in all_vehicles:

            if vehicle.vehicle_id.upper() == vehicle_id.upper():

                print("\nVehicle Found")
                vehicle.display_info()
                return

        print("\nVehicle Not Found.")

    def display_dashboard(self):

        print("\n========== DASHBOARD ==========")
        print("Manager Name     :", self.manager_name)
        print("Total Buses      :", len(self.buses))
        print("Total MiniVans   :", len(self.mini_vans))
        print("Total Drivers    :", len(self.drivers))
        print("Total Students   :", len(self.students))
        print("Total Vehicles   :", Vehicle.get_total_vehicles())
from transport_manager import TransportManager
from vehicles import Bus, MiniVan, Vehicle
from drivers import Driver
from students import Student
from fare import RouteFare, SpecialTripFare
from utils import *


def display_main_menu():

    print_divider()
    print("ACE Engineering College Transportation Portal")
    print_divider()

    print("1. Add Bus")
    print("2. Add MiniVan")
    print("3. Add Driver")
    print("4. Register Student")
    print("5. Display Vehicles")
    print("6. Display Drivers")
    print("7. Display Students")
    print("8. Calculate Route Fare")
    print("9. Calculate Special Trip Fare")
    print("10. Search Vehicle")
    print("11. Dashboard")
    print("0. Exit")

    print_divider()


def main():

    print_divider()
    print("Welcome to ACE Engineering College")
    print("Transportation Portal")
    print_divider()

    manager_name = get_non_empty_input("Enter Transport Manager Name: ")

    manager = TransportManager(manager_name)

    while True:

        display_main_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":

            vehicle_id = get_non_empty_input("Enter Bus ID: ").upper()

            if not Vehicle.validate_vehicle_id(vehicle_id):
                print("Invalid Vehicle ID.")
                continue

            capacity = get_integer_input("Enter Capacity: ")
            route = get_integer_input("Enter Route Number: ")
            has_ac = get_yes_no_input("AC Bus (Y/N): ")

            bus = Bus(vehicle_id, capacity, route, has_ac)
            manager.add_bus(bus)

        elif choice == "2":

            vehicle_id = get_non_empty_input("Enter MiniVan ID: ").upper()

            if not Vehicle.validate_vehicle_id(vehicle_id):
                print("Invalid Vehicle ID.")
                continue

            capacity = get_integer_input("Enter Capacity: ")
            purpose = get_non_empty_input("Enter Trip Purpose: ")

            van = MiniVan(vehicle_id, capacity, purpose)
            manager.add_minivan(van)

        elif choice == "3":

            driver_id = get_non_empty_input("Enter Driver ID: ")
            name = get_non_empty_input("Enter Driver Name: ")
            license_number = get_non_empty_input("Enter License Number: ")
            contact = get_non_empty_input("Enter Contact Number: ")

            try:
                driver = Driver(driver_id, name, license_number, contact)
                manager.add_driver(driver)

            except ValueError as error:
                print(error)

        elif choice == "4":

            student_id = get_non_empty_input("Enter Student ID: ")
            name = get_non_empty_input("Enter Student Name: ")
            branch = get_non_empty_input("Enter Branch: ")
            year = get_integer_input("Enter Year: ")

            student = Student(student_id, name, branch, year)
            manager.add_student(student)

        elif choice == "5":

            manager.display_all_vehicles()

        elif choice == "6":

            manager.display_all_drivers()

        elif choice == "7":

            manager.display_all_students()

        elif choice == "8":

            student_id = get_non_empty_input("Enter Student ID: ")
            distance = get_float_input("Enter Distance (KM): ")
            pass_type = get_non_empty_input("Enter Pass Type (Monthly/Semester): ")

            fare = RouteFare(student_id, distance, pass_type)
            fare.display_fare_summary()

        elif choice == "9":

            student_id = get_non_empty_input("Enter Student ID: ")
            distance = get_float_input("Enter Distance (KM): ")
            students = get_integer_input("Enter Number of Students: ")

            fare = SpecialTripFare(student_id, distance, students)
            fare.display_fare_summary()

        elif choice == "10":

            vehicle_id = get_non_empty_input("Enter Vehicle ID: ")
            manager.search_vehicle(vehicle_id)

        elif choice == "11":

            manager.display_dashboard()

        elif choice == "0":

            print("\nThank You for using the Transportation Portal.")
            break

        else:

            print("Invalid Choice. Please Try Again.")


if __name__ == "__main__":
    main()
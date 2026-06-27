from transport_manager import TransportManager
from vehicles import Bus, MiniVan, Vehicle
from drivers import Driver
from fare import RouteFare, SpecialTripFare
from utils import (print_header, print_separator,
                   get_input, get_int_input, get_float_input, yes_no_input)


# ------------------------------------------
def display_main_menu():
    print("\n" + "=" * 55)
    print("   ACE Engineering College Transportation Portal")
    print("=" * 55)
    print("  1. Add New Bus")
    print("  2. Add New MiniVan")
    print("  3. Add New Driver")
    print("  4. Display All Vehicles")
    print("  5. Display All Drivers")
    print("  6. Calculate Route Fare")
    print("  7. Calculate Special Trip Fare")
    print("  8. Search Vehicle by ID")
    print("  9. Display Dashboard Summary")
    print("  0. Exit Portal")
    print("=" * 55)


# ------------------------------------------
def add_bus(manager):
    print_header("ADD NEW BUS")

    vehicle_id = get_input(
        "Enter Bus Vehicle ID (e.g. AP28Z1234): ",
        validator=lambda v: Vehicle.validate_vehicle_id(v),
        error_msg="Invalid vehicle ID format. Use format like AP28Z1234."
    )
    capacity = get_int_input("Enter Seating Capacity: ", min_val=1, max_val=100)
    route_number = get_int_input("Enter Route Number: ", min_val=1)
    has_ac = yes_no_input("Does this bus have AC?")

    bus = Bus(vehicle_id.upper(), capacity, route_number, has_ac)
    manager.add_bus(bus)
    print(f"\n  {str(bus)}")


# ------------------------------------------
def add_minivan(manager):
    print_header("ADD NEW MINIVAN")

    vehicle_id = get_input(
        "Enter MiniVan Vehicle ID (e.g. TN05AB6789): ",
        validator=lambda v: Vehicle.validate_vehicle_id(v),
        error_msg="Invalid vehicle ID format. Use format like TN05AB6789."
    )
    capacity = get_int_input("Enter Seating Capacity: ", min_val=1, max_val=20)
    trip_purpose = get_input("Enter Trip Purpose (e.g. Industrial Visit): ")

    van = MiniVan(vehicle_id.upper(), capacity, trip_purpose)
    manager.add_minivan(van)
    print(f"\n  {str(van)}")


# ------------------------------------------
def add_driver(manager):
    print_header("ADD NEW DRIVER")

    driver_id = get_input("Enter Driver ID (e.g. DRV001): ")
    name      = get_input("Enter Driver Name: ")

    license_number = get_input(
        "Enter License Number (exactly 16 characters): ",
        validator=lambda v: len(v) == 16,
        error_msg="License number must be exactly 16 characters."
    )

    contact = get_input(
        "Enter Contact Number (10 digits): ",
        validator=lambda v: v.isdigit() and len(v) == 10,
        error_msg="Contact must be exactly 10 digits (numbers only)."
    )

    try:
        driver = Driver(driver_id, name, license_number, contact)
        manager.add_driver(driver)
    except ValueError as e:
        print(e)


# ------------------------------------------
def calculate_route_fare():
    print_header("ROUTE FARE CALCULATOR")

    student_id  = get_input("Enter Student ID: ")
    distance_km = get_float_input("Enter Distance (km): ")

    print("  Pass Types: 1. Monthly   2. Semester")
    pt_choice = get_input(
        "Choose Pass Type (1 or 2): ",
        validator=lambda v: v in ("1", "2"),
        error_msg="Enter 1 for Monthly or 2 for Semester."
    )
    pass_type = "Monthly" if pt_choice == "1" else "Semester"

    rf = RouteFare(student_id, distance_km, pass_type)
    print()
    rf.display_fare_summary()


# ------------------------------------------
def calculate_special_trip_fare():
    print_header("SPECIAL TRIP FARE CALCULATOR")

    student_id   = get_input("Enter Student ID: ")
    distance_km  = get_float_input("Enter Distance (km): ")
    num_students = get_int_input("Enter Number of Students: ", min_val=1)

    sf = SpecialTripFare(student_id, distance_km, num_students)
    print()
    sf.display_fare_summary()


# ------------------------------------------
def search_vehicle(manager):
    print_header("SEARCH VEHICLE BY ID")
    vehicle_id = get_input("Enter Vehicle ID to search: ")
    manager.search_vehicle(vehicle_id)


# ------------------------------------------
def main():
    manager = TransportManager("Mr. Ramesh")

    while True:
        display_main_menu()
        choice = input("  Enter your choice: ").strip()

        if choice == "1":
            add_bus(manager)

        elif choice == "2":
            add_minivan(manager)

        elif choice == "3":
            add_driver(manager)

        elif choice == "4":
            # Polymorphism: display_info() differs per class type
            manager.display_all_vehicles()

        elif choice == "5":
            manager.display_all_drivers()

        elif choice == "6":
            calculate_route_fare()

        elif choice == "7":
            calculate_special_trip_fare()

        elif choice == "8":
            search_vehicle(manager)

        elif choice == "9":
            manager.display_dashboard()

        elif choice == "0":
            print("\n  Thank you for using ACE Transportation Portal!")
            print("  Goodbye!\n")
            break

        else:
            print("\n  [ERROR] Invalid choice. Please enter a number from 0 to 9.")


# ------------------------------------------
if __name__ == "__main__":
    main()

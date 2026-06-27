from vehicles import Bus, MiniVan
from drivers import Driver


class TransportManager:

    def __init__(self, manager_name):
        self.manager_name = manager_name

        # ------------------------------------------
        # COMPOSITION: TransportManager "has" lists of other objects
        self.buses     = []   # list of Bus objects
        self.mini_vans = []   # list of MiniVan objects
        self.drivers   = []   # list of Driver objects

    # ------------------------------------------
    # Add a Bus object to self.buses
    def add_bus(self, bus_obj):
        if not isinstance(bus_obj, Bus):
            print("  [ERROR] Only Bus objects can be added to buses list.")
            return
        self.buses.append(bus_obj)
        print(f"  [SUCCESS] Bus '{bus_obj.vehicle_id}' added successfully.")

    # ------------------------------------------
    # Add a MiniVan object to self.mini_vans
    def add_minivan(self, van_obj):
        if not isinstance(van_obj, MiniVan):
            print("  [ERROR] Only MiniVan objects can be added to mini_vans list.")
            return
        self.mini_vans.append(van_obj)
        print(f"  [SUCCESS] MiniVan '{van_obj.vehicle_id}' added successfully.")

    # ------------------------------------------
    # Add a Driver object to self.drivers
    def add_driver(self, driver_obj):
        if not isinstance(driver_obj, Driver):
            print("  [ERROR] Only Driver objects can be added to drivers list.")
            return
        self.drivers.append(driver_obj)
        print(f"  [SUCCESS] Driver '{driver_obj.name}' added successfully.")

    # ------------------------------------------
    # POLYMORPHISM: Call display_info() on all vehicles
    # Bus.display_info() and MiniVan.display_info() behave differently
    def display_all_vehicles(self):
        all_vehicles = self.buses + self.mini_vans
        if not all_vehicles:
            print("  No vehicles registered yet.")
            return
        print(f"\n  {'=' * 50}")
        print(f"  ACE College Vehicle Fleet - Total: {len(all_vehicles)}")
        print(f"  {'=' * 50}")
        for vehicle in all_vehicles:
            vehicle.display_info()        # <-- Polymorphism in action
            print(f"  {'-' * 50}")

    # ------------------------------------------
    # Display all drivers
    def display_all_drivers(self):
        if not self.drivers:
            print("  No drivers registered yet.")
            return
        print(f"\n  {'=' * 50}")
        print(f"  Registered Drivers - Total: {len(self.drivers)}")
        print(f"  {'=' * 50}")
        for driver in self.drivers:
            driver.display_info()
            print(f"  {'-' * 50}")

    # ------------------------------------------
    # Search for a vehicle by vehicle_id (buses + mini_vans)
    def search_vehicle(self, vehicle_id):
        all_vehicles = self.buses + self.mini_vans
        for vehicle in all_vehicles:
            if vehicle.vehicle_id.upper() == vehicle_id.upper():
                print(f"\n  [FOUND] Vehicle '{vehicle_id}':")
                vehicle.display_info()
                return
        print(f"\n  [NOT FOUND] No vehicle with ID '{vehicle_id}' registered.")

    # ------------------------------------------
    # Print dashboard summary
    def display_dashboard(self):
        print(f"\n  {'=' * 50}")
        print(f"  TRANSPORT MANAGER DASHBOARD")
        print(f"  {'=' * 50}")
        print(f"  Manager Name    : {self.manager_name}")
        print(f"  Total Buses     : {len(self.buses)}")
        print(f"  Total MiniVans  : {len(self.mini_vans)}")
        print(f"  Total Drivers   : {len(self.drivers)}")
        print(f"  Total Vehicles  : {len(self.buses) + len(self.mini_vans)}")
        print(f"  {'=' * 50}")


# ------------------------------------------
if __name__ == "__main__":
    print("=== TransportManager Module Test ===\n")

    manager = TransportManager("Mr. Ramesh")

    b1 = Bus("AP28Z1234", 50, 3, has_ac=True)
    b2 = Bus("AP28Z5678", 45, 1, has_ac=False)
    v1 = MiniVan("TN05AB6789", 12, "Industrial Visit")
    d1 = Driver("DRV001", "Ravi Kumar", "MH1234567890ABCD", "9876543210")

    manager.add_bus(b1)
    manager.add_bus(b2)
    manager.add_minivan(v1)
    manager.add_driver(d1)

    manager.display_all_vehicles()
    manager.display_all_drivers()
    manager.search_vehicle("AP28Z1234")
    manager.search_vehicle("XX00Y0000")
    manager.display_dashboard()

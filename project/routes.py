# 1. LIST - Bus stops for Route 1
# (Ordered collection, can be modified)
route_1_stops = ["College Gate", "RTC Cross", "Miyapur", "Kukatpally", "KPHB", "Ameerpet"]

# ------------------------------------------
# 2. TUPLE - GPS Coordinates of each stop
# (Fixed data, immutable)
stop_coordinates = (
    (17.4939, 78.3996),   # College Gate
    (17.4950, 78.3900),   # RTC Cross
    (17.4960, 78.3800),   # Miyapur
    (17.4800, 78.4100),   # Kukatpally
    (17.4700, 78.4200),   # KPHB
    (17.4400, 78.4400),   # Ameerpet
)

# ------------------------------------------
# 3. SET - Registered Student Pass IDs
# (Unique values only, no duplicates)
registered_pass_ids = {"ACE001", "ACE002", "ACE003", "ACE004", "ACE005"}

# ------------------------------------------
# 4. DICTIONARY - Bus Fleet Details
# (Key-Value structured data)
bus_fleet = {
    "AP28Z1234": {"capacity": 50, "driver": "Ravi Kumar",  "route": 1, "ac": True},
    "AP28Z5678": {"capacity": 45, "driver": "Suresh Babu", "route": 2, "ac": False},
    "TN05AB6789": {"capacity": 12, "driver": "Mohan Rao",  "route": 0, "ac": False},
}


# ------------------------------------------
# Display all stops for a given route
def display_route_stops(route_stops):
    if not route_stops:
        print("  No stops defined for this route.")
        return
    print(f"\n  Route Stops ({len(route_stops)} stops):")
    for i, stop in enumerate(route_stops, 1):
        print(f"    {i}. {stop}")


# ------------------------------------------
# Add a new stop to an existing route
def add_stop(route_stops, new_stop):
    if new_stop in route_stops:
        print(f"  Stop '{new_stop}' already exists in the route.")
    else:
        route_stops.append(new_stop)
        print(f"  Stop '{new_stop}' added successfully.")
    return route_stops


# ------------------------------------------
# Register a new student pass ID
def register_student_pass(pass_set, student_id):
    if student_id in pass_set:
        print(f"  Student ID '{student_id}' is already registered.")
    else:
        pass_set.add(student_id)
        print(f"  Student pass '{student_id}' registered successfully.")
    return pass_set


# ------------------------------------------
# Display all bus fleet details
def display_bus_details(bus_dict):
    if not bus_dict:
        print("  No buses in fleet.")
        return
    print(f"\n  {'Bus No':<15} {'Capacity':<10} {'Driver':<20} {'Route':<8} {'AC'}")
    print("  " + "-" * 60)
    for bus_no, details in bus_dict.items():
        ac = "Yes" if details.get("ac") else "No"
        route = details.get("route", "-")
        print(f"  {bus_no:<15} {details['capacity']:<10} {details['driver']:<20} {route:<8} {ac}")


# ------------------------------------------
if __name__ == "__main__":
    print("=== Routes Module Test ===")
    display_route_stops(route_1_stops)
    add_stop(route_1_stops, "Secunderabad")
    add_stop(route_1_stops, "College Gate")  # duplicate test
    print(f"\n  Registered Pass IDs: {registered_pass_ids}")
    register_student_pass(registered_pass_ids, "ACE006")
    register_student_pass(registered_pass_ids, "ACE001")  # duplicate test
    display_bus_details(bus_fleet)

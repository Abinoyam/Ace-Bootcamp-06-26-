from abc import ABC, abstractmethod


# ==========================================
# ABSTRACT BASE CLASS: FareCalculator
# ==========================================
class FareCalculator(ABC):
    # NOTE: This class CANNOT be instantiated directly

    def __init__(self, student_id, distance_km):
        self.student_id  = student_id
        self.distance_km = distance_km

    # ------------------------------------------
    # ABSTRACT METHOD 1 - must be implemented by all subclasses
    @abstractmethod
    def calculate_fare(self):
        pass

    # ------------------------------------------
    # ABSTRACT METHOD 2 - must be implemented by all subclasses
    @abstractmethod
    def display_fare_summary(self):
        pass

    # ------------------------------------------
    # CONCRETE METHOD - shared utility
    # Returns discounted amount
    def apply_discount(self, amount, discount_percent):
        discounted = amount - (amount * discount_percent / 100)
        return round(discounted, 2)


# ==========================================
# CONCRETE CLASS 1: RouteFare
# ==========================================
class RouteFare(FareCalculator):

    def __init__(self, student_id, distance_km, pass_type):
        super().__init__(student_id, distance_km)
        # pass_type: "Monthly" or "Semester"
        self.pass_type = pass_type

    # ------------------------------------------
    # Fare Logic:
    #   Monthly  fare = distance_km * 2.5
    #   Semester fare = distance_km * 12
    def calculate_fare(self):
        if self.pass_type.lower() == "monthly":
            return round(self.distance_km * 2.5, 2)
        elif self.pass_type.lower() == "semester":
            return round(self.distance_km * 12, 2)
        else:
            raise ValueError(f"  [ERROR] Unknown pass type: '{self.pass_type}'. Use 'Monthly' or 'Semester'.")

    # ------------------------------------------
    # Print formatted fare receipt with 10% student discount
    def display_fare_summary(self):
        fare = self.calculate_fare()
        discount_pct = 10
        final = self.apply_discount(fare, discount_pct)
        print(f"  Student ID      : {self.student_id}")
        print(f"  Distance (km)   : {self.distance_km}")
        print(f"  Pass Type       : {self.pass_type}")
        print("  " + "-" * 32)
        print(f"  Fare Calculated : Rs. {fare:.2f}")
        print(f"  Discount Applied: {discount_pct}%")
        print(f"  Final Amount    : Rs. {final:.2f}")


# ==========================================
# CONCRETE CLASS 2: SpecialTripFare
# ==========================================
class SpecialTripFare(FareCalculator):

    def __init__(self, student_id, distance_km, num_students):
        super().__init__(student_id, distance_km)
        self.num_students = num_students

    # ------------------------------------------
    # Fare Logic:
    #   Total fare      = distance_km * 5 * num_students
    #   Per student     = Total fare / num_students
    def calculate_fare(self):
        total = round(self.distance_km * 5 * self.num_students, 2)
        per_student = round(total / self.num_students, 2)
        return total, per_student

    # ------------------------------------------
    # Print formatted fare receipt
    def display_fare_summary(self):
        total, per_student = self.calculate_fare()
        print(f"  Student ID      : {self.student_id}")
        print(f"  Distance (km)   : {self.distance_km}")
        print(f"  No. of Students : {self.num_students}")
        print("  " + "-" * 32)
        print(f"  Total Fare      : Rs. {total:.2f}")
        print(f"  Per Student     : Rs. {per_student:.2f}")


# ------------------------------------------
if __name__ == "__main__":
    print("=== Fare Module Test ===\n")

    print("  [Route Fare - Monthly]")
    rf = RouteFare("ACE2024001", 25, "Monthly")
    rf.display_fare_summary()

    print("\n  [Route Fare - Semester]")
    rf2 = RouteFare("ACE2024002", 30, "Semester")
    rf2.display_fare_summary()

    print("\n  [Special Trip Fare]")
    sf = SpecialTripFare("ACE2024003", 40, 20)
    sf.display_fare_summary()

    print("\n  [Abstract class instantiation test]")
    try:
        fc = FareCalculator("X", 10)
    except TypeError as e:
        print(f"  Correctly blocked: {e}")

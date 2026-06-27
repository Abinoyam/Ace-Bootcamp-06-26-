from abc import ABC, abstractmethod


class FareCalculator(ABC):

    def __init__(self, student_id, distance_km):
        self.student_id = student_id
        self.distance_km = distance_km

    @abstractmethod
    def calculate_fare(self):
        pass

    @abstractmethod
    def display_fare_summary(self):
        pass

    def apply_discount(self, amount, discount_percent):
        discount = amount * discount_percent / 100
        return amount - discount


class RouteFare(FareCalculator):

    def __init__(self, student_id, distance_km, pass_type):
        super().__init__(student_id, distance_km)
        self.pass_type = pass_type

    def calculate_fare(self):

        if self.pass_type.lower() == "monthly":
            return self.distance_km * 2.5

        elif self.pass_type.lower() == "semester":
            return self.distance_km * 12

        else:
            print("Invalid Pass Type.")
            return 0

    def display_fare_summary(self):

        fare = self.calculate_fare()

        print("\n" + "=" * 40)
        print("ROUTE FARE SUMMARY")
        print("=" * 40)
        print("Student ID :", self.student_id)
        print("Distance   :", self.distance_km, "KM")
        print("Pass Type  :", self.pass_type)
        print("Fare       : Rs.", fare)
        print("=" * 40)


class SpecialTripFare(FareCalculator):

    def __init__(self, student_id, distance_km, num_students):
        super().__init__(student_id, distance_km)
        self.num_students = num_students

    def calculate_fare(self):

        total_fare = self.distance_km * 5 * self.num_students
        per_student = total_fare / self.num_students

        return total_fare, per_student

    def display_fare_summary(self):

        total, per_student = self.calculate_fare()

        print("\n" + "=" * 40)
        print("SPECIAL TRIP FARE")
        print("=" * 40)
        print("Student ID      :", self.student_id)
        print("Distance        :", self.distance_km, "KM")
        print("Students        :", self.num_students)
        print("Total Fare      : Rs.", total)
        print("Per Student     : Rs.", per_student)
        print("=" * 40)
class Car:
    #Class attributes 
    all_cars = {}
    total_cars = 0
    _next_id = 1

    def __init__(self, make, model, year, mileage=0):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.services =[]
        self._id = Car._next_id
        Car._next_id += 1
        Car.total_cars += 1
        Car.all_cars[self._id] = self

        #ID
    @property
    def id(self):
        return self._id

    #make
    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        self._make = value

    #model
    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    #year
    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        if not isinstance(value, int) or not 1886 <= value <= 2027:
            raise ValueError("Year must be a whole number between 1886 and 2027.")
        self._year = value


    #mileage
    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        self._mileage =value

    @property
    def services(self):
        return list(self._services)

    @services.setter
    def services(self, value):
        self._services = list(value)

    def add_service(self, description):
        self._services.append({"description": description, "mileage": self._mileage})

    def details(self):
        """Full multi-line description of this car, including its services."""
        lines = [
            f"Car #{self._id}",
            f"  Make:    {self._make}",
            f"  Model:   {self._model}",
            f"  Year:    {self._year}",
            f"  Mileage: {self._mileage:,}",
            "  Services:",
        ]
        if self._services:
            for number, service in enumerate(self._services, start=1):
                lines.append(f"    {number}. {service['description']} (at {service['mileage']:,} miles)")
        else:
            lines.append("    None yet")
        return "\n".join(lines)

    def __str__(self):
        """One-line summary used by print() and the 'View all cars' list."""
        return f"#{self._id} {self._year} {self._make} {self._model} - {self._mileage:,} miles"

    # ---- Class methods: what the CLASS knows about all cars ----
    @classmethod
    def get_all_cars(cls):
        """Return every car, in the order they were created."""
        return list(cls.all_cars.values())

    @classmethod
    def get_total_cars(cls):
        """Return how many cars have been created."""
        return cls.total_cars

    @classmethod
    def find_by_id(cls, car_id):
        """Return the car with this id, or None if it doesn't exist."""
        return cls.all_cars.get(car_id)

# ================= Terminal application =================

MENU = """
----  WELCOME  ----
1. Add a car
2. View all cars
3. View total number of cars
4. See a car's details
5. Service a car
6. Update mileage
7. Quit
"""


def ask_int(prompt):
    """Keep asking until the user types a whole number."""
    while True:
        answer = input(prompt).strip()
        try:
            return int(answer)
        except ValueError:
            print("Please enter a whole number.")


def choose_car():
    """Ask for a car id and return that Car, or None if there isn't one."""
    if Car.get_total_cars() == 0:
        print("No cars yet. Add one first (option 1).")
        return None
    car_id = ask_int("Enter the car's id: ")
    car = Car.find_by_id(car_id)
    if car is None:
        print(f"No car found with id {car_id}.")
    return car

def add_car():
    make = input("Make: ")
    model = input("Model: ")
    year = ask_int("Year: ")
    mileage = ask_int("Current mileage: ")
    try:
        car = Car(make, model, year, mileage)
        print(f"Added: {car}")
    except ValueError as error:
        print(f"Car not added: {error}")


def view_all_cars():
    cars = Car.get_all_cars()
    if not cars:
        print("No cars yet.")
    for car in cars:
        print(car)


def view_total_cars():
    print(f"Total cars: {Car.get_total_cars()}")


def see_car_details():
    car = choose_car()
    if car:
        print(car.details())


def service_car():
    car = choose_car()
    if car:
        description = input("What service was done? ")
        try:
            car.add_service(description)
            print(f"Service recorded for car #{car.id}.")
        except ValueError as error:
            print(f"Service not recorded: {error}")


def update_mileage():
    car = choose_car()
    if car:
        new_mileage = ask_int(f"New mileage (currently {car.mileage:,}): ")
        try:
            car.update_mileage(new_mileage)
            print(f"Mileage updated to {car.mileage:,}.")
        except ValueError as error:
            print(f"Mileage not updated: {error}")

# Menu number -> function to run. Adding an option = one new line here.
ACTIONS = {
    "1": add_car,
    "2": view_all_cars,
    "3": view_total_cars,
    "4": see_car_details,
    "5": service_car,
    "6": update_mileage,
}


def main():
    while True:
        print(MENU)
        choice = input("Choose an option (1-7): ").strip()
        if choice == "7":
            print("Goodbye!")
            break
        action = ACTIONS.get(choice)
        if action:
            action()
        else:
            print("Invalid option. Please choose 1-7.")


# Only start the menu when this file is run directly,
# not when the tests import it.
if __name__ == "__main__":
    main()
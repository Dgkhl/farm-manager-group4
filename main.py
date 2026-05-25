# main.py  —  Farm manager entry point
# Dev 5 : DEMBELE Gaethan Khaleb

from animal        import Animal
from vache_laitiere import VacheLaitiere
from poulet        import Poulet
from input_helpers import (
    get_int, get_float, get_yes_no, get_animal_type, get_string
)


def show_summary(farm_name: str, animals: list,
                 total_revenue: float, days: int) -> None:
    print(f"\n" + "=" * 54)
    print(f"   FARM REPORT : {farm_name.upper()}")
    print(f"   Projection over {days} day(s)")
    print("=" * 54)
    for a in animals:
        print(f"  {a}")
    print("-" * 54)
    print(f"  Animals registered : {len(animals)}")
    print(f"  Estimated revenue  : {total_revenue:,.0f} FCFA")
    print(f"  Projection period  : {days} day(s)")
    print("=" * 54)


def main() -> None:
    print("=" * 54)
    print("   WELCOME — FARM MANAGER")
    print("   Group 4 | BIT | PRG1406")
    print("=" * 54)

    farm_name  = get_string("Farm name : ")
    days       = get_int("Projection duration (days) : ", 1, 365)
    nb_animals = get_int("Number of animals to register : ", 1, 50)

    animals: list        = []
    total_revenue: float = 0.0

    for i in range(nb_animals):
        print(f"\n--- Animal {i + 1} of {nb_animals} ---")

        animal_type = get_animal_type()
        name        = get_string("Animal name : ")
        age         = get_int("Age (years) : ", 0, 30)
        weight      = get_float("Weight (kg) : ", 0.1)
        vaccinated  = get_yes_no("Vaccinated? (yes/no) : ")

        if animal_type == "cow":
            milk   = get_float("Daily milk production (L) : ", 0.0)
            price  = get_float("Price per litre (FCFA) : ", 1.0)
            animal = VacheLaitiere(name, age, weight, vaccinated, milk, price)
            total_revenue += animal.revenue_projection(days)
        else:
            eggs     = get_int("Eggs per day : ", 0, 30)
            is_layer = get_yes_no("Is it a layer? (yes/no) : ")
            animal   = Poulet(name, age, weight, vaccinated, eggs, is_layer)
            total_revenue += animal.egg_revenue(days)

        animals.append(animal)
        print(f"  ► {animal.name} registered.")

    show_summary(farm_name, animals, total_revenue, days)
    print("Thank you for using the farm manager.")


if __name__ == "__main__":
    main()
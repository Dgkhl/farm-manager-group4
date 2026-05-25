# poulet.py  —  Child class (inherits Animal)
# Dev 3 : KABORE Awa

from animal import Animal


class Poulet(Animal):
    """A chicken IS AN Animal — direct inheritance."""

    AVERAGE_EGG_PRICE = 150

    def __init__(self, name: str, age: int, weight: float,
                 is_vaccinated: bool, eggs_per_day: int,
                 is_layer: bool):
        super().__init__(name, age, weight, is_vaccinated)
        self.eggs_per_day = eggs_per_day
        self.is_layer     = is_layer

    def __str__(self) -> str:
        kind = "Layer" if self.is_layer else "Meat"
        return (f"[Chicken - {kind}] {self.name} | "
                f"Eggs/day : {self.eggs_per_day} | "
                f"Weight : {self.weight:.1f} kg")

    @classmethod
    def price_per_egg(cls) -> float:
        """Returns the average price of one egg."""
        return cls.AVERAGE_EGG_PRICE

    @staticmethod
    def category() -> str:
        return "Poultry"

    def egg_revenue(self, days: int) -> float:
        if not self.is_layer:
            return 0.0
        return self.eggs_per_day * Poulet.AVERAGE_EGG_PRICE * days

    @property
    def weekly_production(self) -> int:
        """Returns the number of eggs per week."""
        return self.eggs_per_day * 7
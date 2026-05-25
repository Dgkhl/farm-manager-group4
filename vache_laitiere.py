# vache_laitiere.py  —  Child class (inherits Animal)
# Dev 2 : COMPAORE Adil Fahim Saidou

from animal import Animal


class VacheLaitiere(Animal):
    """A dairy cow IS AN Animal — direct inheritance."""

    def __init__(self, name: str, age: int, weight: float,
                 is_vaccinated: bool, daily_milk_liters: float,
                 price_per_liter: float):
        super().__init__(name, age, weight, is_vaccinated)
        self.daily_milk_liters = daily_milk_liters
        self.price_per_liter   = price_per_liter

    def __str__(self) -> str:
        return (f"[Dairy Cow] {self.name} | "
                f"Milk : {self.daily_milk_liters:.1f} L/day | "
                f"Price : {self.price_per_liter:.0f} FCFA/L")

    def __len__(self) -> int:
        return int(self.daily_milk_liters)

    def revenue_projection(self, days: int) -> float:
        return self.daily_milk_liters * self.price_per_liter * days

    @property
    def is_high_production(self) -> bool:
        """True if the cow produces more than 15 litres per day."""
        return self.daily_milk_liters > 15.0
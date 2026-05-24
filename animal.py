# animal.py — Animal Base Class 
# Dev 1 : ZABRE Twendtoin Filomène Tania
class Animal: 
    valid_species = ['cow', 'chicken', 'sheep', 'rabbit'] 
    def __init__(self, name: str, age: int, weight: float, is_vaccinated: bool):
        self.name = name 
        self.age = age 
        self.weight = weight 
        self.is_vaccinated = is_vaccinated
    def __str__(self) -> str:
        status = "Vaccinated" if self.is_vaccinated else "Not vaccinated"
        return (f"Animal: {self.name} | Age: {self.age} year(s) | Weight: {self.weight} kg | Status: {status}")
    def __eq__(self, other) -> bool: 
        if not isinstance(other, Animal): return False 
        return self.name == other.name and self.age == other.age
    def is_adult(self) -> bool:
        """Returns True if the animal is older than 1 year."""
        return self.age > 1
    def estimated_value(self) -> float: 
        """Arithmetic expression: value based on weight."""
        return self.weight * 1500.0
    @staticmethod
    def animal_type() -> str:
        """Returns a string indicating the type of animal."""
        return "Farm animal"
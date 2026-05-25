from animal import Animal


class VacheLaitiere(Animal):
    """Une vache laitière EST UN Animal — héritage direct."""

    def __init__(self, nom: str, age: int, poids: float,
                 is_vaccinated: bool, production_journaliere: float,
                 prix_litre: float):
        super().__init__(nom, age, poids, is_vaccinated)
        self.production_journaliere = production_journaliere
        self.prix_litre = prix_litre

    # ■■ Magic Method __str__ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def __str__(self) -> str:
        return (f"[Vache Laitière] {self.nom} | "
                f"Production : {self.production_journaliere:.1f} L/jour | "
                f"Prix : {self.prix_litre:.0f} FCFA/L")

    # ■■ Magic Method __len__ ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def __len__(self) -> int:
        """Retourne la production arrondie (en litres entiers)."""
        return int(self.production_journaliere)

    # ■■ Méthode spécifique ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
    def revenu_projection(self, jours: int) -> float:
        """Calcul arithmétique du revenu sur N jours."""
        return self.production_journaliere * self.prix_litre * jours

    @property
    def est_haute_production(self) -> bool:
        """True si production > 15 L/jour."""
        return self.production_journaliere > 15.0
from abc import ABC, abstractmethod


class AbstractAttack(ABC):
    """
    An Attack
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------

    def __init__(self, power=int, name=None, description=None):
        # -----------------------------
        # Attributes
        # -----------------------------
        self._power: int = power
        self._name: str = name
        self._description: str = description

    # -------------------------------------------------------------------------
    # Methods
    # -------------------------------------------------------------------------

    @abstractmethod
    def compute_damage(self, APkm, DPkm) -> int:
        damage = 0
        return damage

        # Basic Getter / Setter

    @property
    def power(self):
        return self._power

    @property
    def description(self):
        return self._description

    @property
    def name(self):
        return self._name

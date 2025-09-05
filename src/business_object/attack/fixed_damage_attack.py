from .abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, APkm, DPkm) -> int:
        return self.power

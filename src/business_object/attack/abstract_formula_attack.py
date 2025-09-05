from .abstract_attack import AbstractAttack

import random
from abc import abstractmethod

class AbstrackFormulaAttack(AbstractAttack):
    def compute_damage(self, APkm, DPkm) -> int:
        damage = ((2*APkm.level/5 + 2)*self.power*self.get_attack_stat(APkm))/self.get_defense_stat(DPkm)*50 +2
        rd = random.uniform(0.85, 1)
        damage = damage*rd
        return damage

@abtractmethod
    def get_attack_stat(self, APkm: AbstractPokemon) -> float:



    

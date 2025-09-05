from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.pokemon.attacker_pokemon import AttackerPokemon
from business_object.pokemon.defender_pokemon import DefenderPokemon


class TestFixedDamageAttack:
    def test_compute_damage(self):
        # GIVEN
        attack = FixedDamageAttack(power = 100)

        # WHEN
        damage = attack.compute_damage(None, None)

        # THEN
        assert damage == 100


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])

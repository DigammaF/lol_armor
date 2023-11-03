
import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass

@dataclass
class Target:
	health: float
	armor: float

def applied_damage(target: Target, damage: float) -> float:
	"""
		Returns the amount of health left after damage application
	"""

	damage_multiplier: float = 100 / (100 + target.armor)
	mitigated_damage: float = damage * damage_multiplier
	return target.health - mitigated_damage

def get_armor_value(target: Target, damage: float) -> float:
	"""
		Returns the added value of target.armor in health points
	"""

	target_no_armor: Target = Target(health=target.health, armor=0)
	health_no_armor: float = applied_damage(target_no_armor, damage)
	health_with_armor: float = applied_damage(target, damage)
	return health_with_armor - health_no_armor

def get_normalized_armor_value(armor: float) -> float:
	return get_armor_value(Target(health=0, armor=armor), damage=1)

def main():
	
	armor_points = np.linspace(0, 500, num=1_000_000)
	armor_values = get_normalized_armor_value(armor_points)

	plt.plot(armor_points, armor_values)
	plt.show()

if __name__ == "__main__":
	main()

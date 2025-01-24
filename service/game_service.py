def attack(player, enemy):
    damage = player.attack(enemy)
    return damage, not enemy.is_alive()

def defend(player, enemy):
    damage_reduced = min(enemy.physical, player.defense)
    player.hp -= max(enemy.physical - player.defense, 0)
    return damage_reduced, not player.is_alive()
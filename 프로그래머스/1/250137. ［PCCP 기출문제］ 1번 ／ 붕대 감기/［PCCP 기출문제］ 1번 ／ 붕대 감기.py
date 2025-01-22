def solution(bandage, health, attacks):
    answer = 0
    suc = 0
    max_hp = health
    for t in range(max(time for time, _ in attacks)+1):
        if attacks and attacks[0][0] == t:
            damage = attacks.pop(0)[1]
            health -= damage
            suc = 0
            if health <= 0:
                return -1
        else:
            suc += 1
            if health == max_hp:
                continue
            elif suc == bandage[0]:
                health += bandage[2] + bandage[1]
                suc = 0
            else:
                health += bandage[1]
                
                
            if health > max_hp:
                health = max_hp
    return health
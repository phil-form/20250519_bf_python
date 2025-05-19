mon_int = 5
mon_second = 6

mon_addition = mon_int + mon_second
print(mon_addition)

print(mon_int == mon_second)
print(mon_int < mon_second)
print(mon_int > mon_second)
print(mon_int >= mon_second)
print(mon_int <= mon_second)

# il faut que soit la première comparaison soit vraie mon_second == mon_int
# soit la seconde mon_int > mon_addition
print(mon_second == mon_int or mon_int > mon_addition)
# ici il faut que les deux comparaisons soient vraies.
print(mon_int != mon_second and mon_int < mon_second)
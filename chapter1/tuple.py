
lax_coordinates=(33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

traveler_ids=[('USA', '31195855', 'a'), ('BRA', 'CE342567', 'b'),]

for passport in sorted(traveler_ids):
    print('%s--%s/%s' % passport)

print(traveler_ids)


for _, passport, _ in traveler_ids:
    print(_)




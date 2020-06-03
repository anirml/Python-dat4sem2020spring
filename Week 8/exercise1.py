import numpy as np
import matplotlib.pyplot as plt



file = './befkbhalderstatkode.csv'

people_stat = np.genfromtxt(file, delimiter=',', dtype=np.uint, skip_header=1)

neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}

pop_per_neighb = {}

for n in neighb.keys():
    mask = (people_stat[:,1] == n) & (people_stat[:,0] == 2015)
    pop_per_neighb[neighb.get(n)] = np.sum(people_stat[mask][:,4])

pop_sorted = {k: v for k, v in sorted(pop_per_neighb.items(), key=lambda item: item[1])}

plt.bar(pop_sorted.keys(), pop_sorted.values(), width=0.6, align='center')
plt.ylabel('NeighB Sum')
plt.xticks(rotation=90)
plt.xlabel('NeighB')
plt.title('Population per neighborhood')

plt.show()


mask_65 = (people_stat[:,2] > 64) & (people_stat[:,0] == 2015)
people_over_65 = np.sum(people_stat[mask_65][:,4])

print(people_over_65)


mask_65_not_from_dk = mask_65 & (people_stat[:,3]!= 5100)
people_over_65_not_from_dk = np.sum(people_stat[mask_65_not_from_dk][:,4])

print(people_over_65_not_from_dk)


vesterbro_pop = dict()
oesterbro_pop = dict()

for i in range(1992, 2016, 1):
    mask = (people_stat[:,1] == 4) & (people_stat[:,0] == i)
    # print(np.sum(people_stat[mask][:,4]))
    vesterbro_pop[i] = np.sum(people_stat[mask][:,4])

for i in range(1992, 2016, 1):
    mask = (people_stat[:,1] == 2) & (people_stat[:,0] == i)
    # print(np.sum(people_stat[mask][:,4]))
    oesterbro_pop[i] = np.sum(people_stat[mask][:,4])

plt.plot(list(oesterbro_pop.keys()), list(oesterbro_pop.values()), color='b', label='Østerbro')
plt.plot(list(vesterbro_pop.keys()), list(vesterbro_pop.values()), color='g', label='Vesterbro')
plt.xlabel('Year')
plt.ylabel('Population')
plt.xticks(list(oesterbro_pop.keys()),rotation=90)
plt.legend()
plt.show()
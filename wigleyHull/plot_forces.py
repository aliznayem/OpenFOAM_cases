import matplotlib.pyplot as plt

f = open('postProcessing/forces/0/forces.dat')
lines = f.readlines()[3:]

tstep_lst = []
pf_lst = []
vf_lst = []
rt_lst = []
for line in lines:
    line_lst = line.split()
    tstep_lst.append(int(line_lst[0]))
    pressure_f = float(line_lst[1].replace('((', ''))
    viscous_f = float(line_lst[4].replace('(', ''))
    pf_lst.append(pressure_f)
    vf_lst.append(viscous_f)
    rt_lst.append(pressure_f + viscous_f)

n = 100
pf_avg = sum(pf_lst[-n:])/n
vf_avg = sum(vf_lst[-n:])/n
rt_avg = sum(rt_lst[-n:])/n
print(f'Pressure force avg: {pf_avg}, Viscous force avg: {vf_avg}, Total avg: {rt_avg}')

plt.plot(tstep_lst, pf_lst, label="Pressure force")
plt.plot(tstep_lst, vf_lst, label="Viscous force")
plt.plot(tstep_lst, rt_lst, label="Total force")
plt.axhline(y=pf_avg, linestyle=':', linewidth='0.5')
plt.axhline(y=vf_avg, linestyle=':', linewidth='0.5')
plt.axhline(y=rt_avg, linestyle=':', linewidth='0.5')
plt.legend(loc="lower right")

plt.ylabel('R')
plt.xlabel('T')

plt.show()
    

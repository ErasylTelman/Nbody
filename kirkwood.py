import sys
import numpy as np
import matplotlib . pyplot as plt
import time
import rebound

solarmass = 1.989e30
au = 1.496e11
gravitationalconstant = 6.67408e-11
yr = 365.25*24*60*60

sim = rebound.Simulation()
sim.integrator = "leapfrog"
sim.G = gravitationalconstant

sim.add(m = solarmass)
sim.add(m = 1e-3*solarmass, a = 5.2038*au, e = 0.04839, hash = "Jupiter")
sim.add(m = 3.213e-7*solarmass, a = 1.523679*au, e = 0.093315, hash = "Mars")

N_testparticles = 10000
a_ini = np.linspace(2*au, 4*au, N_testparticles)
for a in a_ini:
    sim.add(a = a, f = np.random.rand()*2.*np.pi, e = 0.5*np.random.rand())

sim.move_to_com()

orbit = 2*np.pi*np.sqrt(8*au*au*au/(gravitationalconstant*solarmass))
sim.dt = orbit*1e-2

Nsteps = 11
times = np.linspace(0, 1e6*yr, Nsteps)
print(times)

a_vals = np.zeros((N_testparticles, Nsteps))
e_vals = np.zeros((N_testparticles, Nsteps))

sim.N_active = 3

for i, t in enumerate(times):
    sim.integrate(t)
    localtime = time.localtime()
    current_time = time.strftime("%H:%M:%S", localtime)
    print(f"Step {i}/{Nsteps}, Time: {t/yr:.2f} years, Current time: {current_time}")
    
    filename = f"orbits_t{i}.txt"
    with open(filename, "w") as f:
        for j in range(3, sim.N):
            a_vals[j - 3, i] = sim.particles[j].a / au
            e_vals[j - 3, i] = sim.particles[j].e
            f.write(f"{a_vals[j-3, i]:.6f} {e_vals[j-3, i]:.6f}\n")

sim.save_to_file("my_sim.bin")
print("Simulation complete. Data saved.")
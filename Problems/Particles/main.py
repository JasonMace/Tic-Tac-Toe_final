Particle = ["Strange", "Charm", "Electron", "Neutrino", "Photon"]
Class = ["Quark", "Quark", "Lepton", "Lepton", "Boson"]
Spin = ["1/2", "1/2", "1/2", "1/2", "1"]
Electric_charge = ["-1/3", "2/3", "-1", "0", "0"]

inp_spin = input()
inp_ec = input()
length = len(Electric_charge)

for tmp in range(length):
    if Electric_charge[tmp] == inp_ec:
        if Spin[tmp] == inp_spin:
            print(Particle[tmp], Class[tmp])

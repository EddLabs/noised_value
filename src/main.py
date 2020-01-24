from lab_value import LabValue

rho_b = LabValue(val=7.812, err=0.055)
rho_l = LabValue(val=1.26, err=5.7e-4)
g = LabValue(val=981, err=10)
L = LabValue(val=22.22, err=2.8e-3)
a = LabValue(val=0.1964, err=0.0091)

eta = (2 * g * a * (rho_b - rho_l)) / (9 * L)
print(eta)

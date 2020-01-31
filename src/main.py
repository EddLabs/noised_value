from noised_value import NoisedValue

rho_b = NoisedValue(val=7.812, err=0.055)
rho_l = NoisedValue(val=1.26, err=5.7e-4)
g = NoisedValue(val=981, err=10)
L = NoisedValue(val=22.22, err=2.8e-3)
a = NoisedValue(val=0.1964, err=0.0091)

eta = (2 * g * a * (rho_b - rho_l)) / (9 * L)
expected_eta = NoisedValue(val=12.5, err=1.44)
print(f"experiment eta is: {eta}")
print(f"expected eta is: {expected_eta}")
print(f"n sigma is: {expected_eta.n_sigma(eta)}")

print(NoisedValue(val=0, err=1))

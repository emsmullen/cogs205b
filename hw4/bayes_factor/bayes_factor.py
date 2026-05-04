import math
import scipy.integrate as integrate
class BayesFactor:
    def __init__(self, n, k):
        if type(n) is not int or type(k) is not int or n < 0 or k < 0 or k > n:
            raise ValueError("n must be a non-negative integer and k must be an integer between 0 and n.")
        self.n = n
        self.k = k
    def likelihood(self, theta):
        if type(theta) not in [int, float] or theta < 0 or theta > 1:
            raise ValueError("Theta must be a real number between 0 and 1.")
        combination = math.comb(self.n, self.k)
        theta_term = theta ** self.k
        one_minus_theta_term = (1 - theta) ** (self.n - self.k)
        return combination * theta_term * one_minus_theta_term
    def evidence_slab(self):
        return integrate.quad(self.likelihood, 0, 1)[0]
    def evidence_spike(self):
        key_value = 0.5
        delta = 0.0001
        a = key_value - delta
        b = key_value + delta
        return 1/(b-a) * integrate.quad(self.likelihood, a, b)[0]
    def bayes_factor(self):
        evidence_slab = self.evidence_slab()
        evidence_spike = self.evidence_spike()
        if evidence_slab == 0:
            raise ValueError("Evidence for slab is zero, cannot compute Bayes Factor.")
        return evidence_spike / evidence_slab
    
        
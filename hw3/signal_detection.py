import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

class SignalDetection:
    def __init__(self, hits, misses, false_alarms, correct_rejections):
        # Convert to integers in case they are passed as floats or strings
        hits = int(hits)
        misses = int(misses)
        false_alarms = int(false_alarms)
        correct_rejections = int(correct_rejections)
        
        if hits < 0 or misses < 0 or false_alarms < 0 or correct_rejections < 0:
            raise ValueError("All counts (hits, misses, false_alarms, rejections) must be non-negative integers.")

        self.hits = hits
        self.misses = misses
        self.false_alarms = false_alarms
        self.correct_rejections = correct_rejections
        
    def hit_rate(self):
        if self.hits + self.misses == 0:
            return 0
        return self.hits / (self.hits + self.misses)
    def false_alarm_rate(self):
        if self.false_alarms + self.correct_rejections == 0:
            return 0
        return self.false_alarms / (self.false_alarms + self.correct_rejections)
    def d_prime(self):
        hit_rate = self.hit_rate()
        false_alarm_rate = self.false_alarm_rate()
        return stats.norm.ppf(hit_rate) - stats.norm.ppf(false_alarm_rate)
    def criterion(self):
        hit_rate = self.hit_rate()
        false_alarm_rate = self.false_alarm_rate()
        return -0.5 * (stats.norm.ppf(hit_rate) + stats.norm.ppf(false_alarm_rate))
    def __add__(self,other):
        if not isinstance(other, SignalDetection):
            print ("You can only add another SignalDerection object to this one")
            return NotImplemented
        return SignalDetection(self.hits+other.hits, self.misses+other.misses,  self.false_alarms+other.false_alarms, self.correct_rejections+other.correct_rejections)
    def __sub__(self,other):
        if not isinstance(other, SignalDetection):
            print ("You can only subtract another SignalDerection object from this one")
            return NotImplemented
        return SignalDetection(self.hits-other.hits, self.misses-other.misses,  self.false_alarms-other.false_alarms, self.correct_rejections-other.correct_rejections)
    def __mul__(self,factor):
        if not isinstance(factor, (int, float)):
            raise ValueError("Your multiplicative factor must be a real number")
        return SignalDetection(hits = int(self.hits * factor), misses = int(self.misses * factor), false_alarms = int(self.false_alarms * factor), correct_rejections = int(self.correct_rejections * factor))
    def plot_sdt(self):
        #assume noise distribution is N(0,1) and signal distribution is N(d',1)
        d_prime = self.d_prime()
        x = np.linspace(-5,5,2000)
        noise_dist = stats.norm.pdf(x, loc = 0, scale =1)
        signal_distr = stats.norm.pdf(x, loc = d_prime, scale = 1)
        
        fig, ax = plt.subplots()
        ax.plot(x, noise_dist, label = "Noise")
        ax.plot(x, signal_distr, label = "Signal")
        ax.axvline(x = self.criterion(), color = "red", label = "Criterion")
        ax.plot((0, d_prime), (max(signal_distr), max(signal_distr)), 'k-', label = "d'")
        ax.legend()
        ax.set_title("Signal and Noise Distributions")
        ax.set_xlabel("Sensory Continuum")
        ax.set_ylabel("Probability Density")
        plt.show()
        
        return fig, ax
        
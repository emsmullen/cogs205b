import unittest
from bayes_factor import BayesFactor

class TestBayesFactorMethods(unittest.TestCase):
    
    #core Bayes Factor math tests
    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            BayesFactor(n=-1, k=5)
        with self.assertRaises(ValueError):
            BayesFactor(n=10, k=-1)
        with self.assertRaises(ValueError):
            BayesFactor(n=10, k=11)
        with self.assertRaises(ValueError):
            BayesFactor(n=10.5, k=5)
        with self.assertRaises(ValueError):
            BayesFactor(n=10, k="not an integer")
        with self.assertRaises(ValueError):            
            BayesFactor(n="not an integer", k=5)
    
    def test_likelihood(self):
        actual_bf = BayesFactor(n=10, k=5)
        expected_likelihood = 0.2460937500000001
        self.assertAlmostEqual(actual_bf.likelihood(0.5), expected_likelihood, places=5)
        
    def test_evidence_slab(self):
        actual_bf = BayesFactor(n=25, k=15)
        expected_evidence_slab = 0.0385
        self.assertAlmostEqual(actual_bf.evidence_slab(), expected_evidence_slab, places=3)
        
    def test_evidence_spike(self):
        actual_bf = BayesFactor(n=25, k=15)
        expected_evidence_spike = 0.0974
        self.assertAlmostEqual(actual_bf.evidence_spike(), expected_evidence_spike, places=3)
        
    def test_bayes_factor(self):
        actual_bf = BayesFactor(n=25, k=15)
        expected_bayes_factor = 0.0974 / 0.0385
        self.assertAlmostEqual(actual_bf.bayes_factor(), expected_bayes_factor, places=2)
    
    def test_same_prior(self):
        actual_bf = BayesFactor(n=25, k=5)
        actual_bf.evidence_slab = lambda: 0.5
        actual_bf.evidence_spike = lambda: 0.5
        expected_bayes_factor = 1.0
        self.assertAlmostEqual(actual_bf.bayes_factor(), expected_bayes_factor, places=5)
    
    def test_likelihood_invalid_theta(self):
        actual_bf = BayesFactor(n=10, k=5)
        with self.assertRaises(ValueError):
            actual_bf.likelihood(-0.1)
        with self.assertRaises(ValueError):
            actual_bf.likelihood(1.1)
        with self.assertRaises(ValueError):
            actual_bf.likelihood("not a number")
      
    def test_bayes_factor_zero_evidence_slab(self):
        actual_bf = BayesFactor(n=10, k=5)
        actual_bf.evidence_slab = lambda: 0.0
        actual_bf.evidence_spike = lambda: 0.5
        with self.assertRaises(ValueError):
            actual_bf.bayes_factor()
            
    def test_consistent_object_state(self):
        actual_bf = BayesFactor(n=10, k=5)
        self.assertEqual(actual_bf.n, 10)
        self.assertEqual(actual_bf.k, 5)
    
    def test_invalid_initialization(self):
        with self.assertRaises(ValueError):
            BayesFactor(n=-1, k=5)
        with self.assertRaises(ValueError):
            BayesFactor(n=10, k=-1)
        with self.assertRaises(ValueError):
            BayesFactor(n=10, k=11)
        with self.assertRaises(ValueError):
            BayesFactor(n=10.5, k=5)
        with self.assertRaises(ValueError):
            BayesFactor(n=10, k="not an integer")
        with self.assertRaises(ValueError):            
            BayesFactor(n="not an integer", k=5)        
    
    def test_bayes_factor_edge_cases(self):
        actual_bf = BayesFactor(n=0, k=0)
        expected_bayes_factor = 1.0
        self.assertAlmostEqual(actual_bf.bayes_factor(), expected_bayes_factor, places=5)
        
        actual_bf = BayesFactor(n=100, k=100)
        expected_bayes_factor = 0 / 1.0
        self.assertAlmostEqual(actual_bf.bayes_factor(), expected_bayes_factor, places=5) 
        
        actual_bf = BayesFactor(n=100, k=0)
        expected_bayes_factor = 0 / 1.0
        self.assertAlmostEqual(actual_bf.bayes_factor(), expected_bayes_factor, places=5) 
          
    def test_bayes_factor_large_n_k(self):
        #this is the intentionally failing test. we can see that there is issue when the n and k are too large, because the combination term is too large to convert to float. thus we cannot compute the evidence for slab or spike. 
        actual_bf = BayesFactor(n=10000, k=5000) 
        expected_bayes_factor = 0 #don't care about the true expected value, just want to see if it can compute without error
        self.assertAlmostEqual(actual_bf.bayes_factor(), expected_bayes_factor, places=5)
        

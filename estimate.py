import math
import unittest
import random

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    
if __name__ == "__main__":
    unittest.main()
    
    
def wallis(value):
	pi=1
	for i in range (1,value+1):
		pi=pi*4*i*i/((4*i*i)-1)	
	return 2*pi

def is_inside(x,y):
	distance=math.sqrt(math.pow(x,2)+math.pow(y,2))
	if 1>distance:
		return True
	else:
		return False
	
def monte_carlo(value):
	inside1=0
	random.seed()
	for i in range(value):
		x=random.random()
		y=random.random()
		isinside=is_inside(x,y)
		if isinside==True: 
			inside1=inside1+1
	return 4*inside1/value



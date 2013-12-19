import negative
import unittest

class KnownValues(unittest.TestCase):
	KnownValues = ( (1,-1),
			(2,-2),
			(3,-3),
			(4,-4),
			(5,-5),
			(6,-6),
			(7,-7),
			(8,-8),
			(9,-9),
			(10,-10),
			(20.2,-20.2),
			(40.4,-40.2),
			(50,-50),
			(80.3,-80.3),
			(99,-99))

def testToNegativeKnownValues(self):                          
	"""toneagtive should give known result with known input"""
	for integer,numeral in self.knownValues:              
		result = negative.toNegative(integer)                    
		self.assertEqual(numeral, result)


def testFromNegativeKnownValues(self):                          
	"""fromnegative should give known result with known input"""
	for integer, numeral in self.knownValues:                
		result = negative.fromNegative(numeral)                    
		self.assertEqual(integer, result)  


class ToNegativeBadInput(unittest.TestCase):                            
	def testTooLarge(self):                                          
		"""tonegative should fail with large input"""                   
		self.assertRaises(negative.OutOfRangeError, negative.toNegative, 100)

	

class FromNegativeBadInput(unittest.TestCase):                            
	def testTooLarge(self):                                          
		"""fromnegative should fail with large input"""                   
		self.assertRaises(negative.OutOfRangeError, negative.fromNegative, -100)

class SanityCheck(unittest.TestCase):        
	def testSanity(self):                    
		"""fromNegative(toNegative(n))==n for all n"""
		for integer in range(1, 100):       
			numeral = negative.toNegative(integer) 
			result = negative.fromNegative(numeral)
			self.assertEqual(integer, result)




if __name__ == "__main__":
    unittest.main()       

            
			

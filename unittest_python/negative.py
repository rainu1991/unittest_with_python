#Define exceptions
class NegativeError(Exception): pass                
class OutOfRangeError(NegativeError): pass          

 

def toNegative(n):
	"""convert positive to negative numeral"""
	if not (0 < n < 100):                                             
        	raise OutOfRangeError, "number out of range (must be 1..99)" 
	d = n * 2
	result = n - d
	return result
	                                         

def fromNegative(s):
	"""convert negative numeral to positive"""
	if not (0 > s > -100):                                             
        	raise OutOfRangeError, "number out of range (must be -1..-99)" 
	d = -(s) * 2
	result = s + d
	return result
	

#define the main() function
def main():
	i=0					#declare an integer i
	x=119.0				#declare a float x	

	for i in range(120):	#loop i from o to 119, inclusive	
		if((i%2)==0):	#if i is even	
			x += 3.		# add 3 to x
		else:
			x-=5.

		s = "%3.2e" % x

		print(s)

		if _name_ == "_main_":
			main()
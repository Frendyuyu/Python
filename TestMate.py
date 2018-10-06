from Mate import *
if __name__ == "__main__":
	print("=====" * 50)
	print(type(Materials))

	print("=====" * 50)
	for p in Materials.__dict__:
		print(p)

	print("=====" * 50)
	print(Materials.__doc__)

	print("*****" * 20)
	print("Materials test:")
	p0 = Materials("3400200001", "driver", 10000)
	print(p0.__dict__)

	print("*****" * 20)
	print("Driver test:")

	p1 = Driver("3400200001", "driver", 10000, "19320392-123")
	# print(Driver.__dict__)
	print(p1.__dict__)
	# print(p1.__init__)




from Mate import *
if __name__ == "__main__":
	print("=====" * 50)
	print(type(Materials))

	print("=====" * 50)
	for p in Materials.__dict__:
		print(p)

	print("=====" * 50)
	print(Materials.__doc__)

	print("*****" * 50)
	print("Driver test:" )

	p1 = Driver("3400200001", "driver", 1000, "18090889-600")
	print(p1)



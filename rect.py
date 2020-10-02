class rectangle:

	def __init__(self, length, breadth):
		self.length = length
		self.breadth = breadth
		self.area = length*breadth
		self.perimeter = 2*(length+breadth)
		self.diagonal = ((length*length) + (breadth*breadth))**0.5

	def get_area(self):
		return self.area

	def get_perimeter(self):
		return self.perimeter

	def get_diagonal(self):
		return self.diagonal

length = float(input("Enter the length: "))
breadth = float(input("Enter the breadth: "))

r = rectangle(length, breadth)

choice = input("area, perimeter or diagonal? >>> ").lower()

if choice == "area":
	print(r.get_area())
elif choice == "perimeter":
	print(r.get_perimeter())
elif choice == "diagonal":
	print(r.get_diagonal())
else:
	print("Invalid input!")
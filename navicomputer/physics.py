class Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z
		
	def __repr__(self) -> str:
		return "<Vector x=" + str(self.x) + " y=" + str(self.y) + " z=" + str(self.z) + ">"
		
	def __add__(self, other):
		return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
	
	def __sub__(self, other):
		return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
	
	def __mul__(self, other):
		return sum([self.x * other.x, self.y * other.y, self.z * other.z])
	
	def __matmul__(self, other):
		return Vector(
			x = (self.y * other.z) - (self.z * other.y),
			y = (self.x * other.z) - (self.z * other.x),
			z = (self.x * other.y) - (self.y * other.x)
		)

class Simulation:
	def __init__(self, objects: list[object]=[], gravitationalConstant: float) -> None:
		self.gravitationalConstant = self.G = gravitationalConstant
		self.objects = objects
		for object in self:
			object.parent = self
			
	def __iter__(self) -> Iterable:
		return iter(self.objects)
	
	def __contains__(self, object) -> bool:
		return object in self.objects

	def collision(self, object) ->

class Object:
	def __init__(self, parent: Simulation=None, mass: int=0, radius: int=0, velocity: Vector=Vector(0,0,0)):
		self.mass = mass
		self.radius = radius
		self.velocity = velocity
		self.acceleration = Vector(0, 0, 0)
		self.parent = parent
			   

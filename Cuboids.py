class Cuboid(float **kwargs):
	def sqr_cube__init__(self, a, b, c):
		a == b
		c > a and b
		sqr_cube = ((pow(a or b), 2) * c)
	def cubic__init__(self, a, b, c):
		cubic = ((pow(a, b) * c)
	def cuboid__init__(self, **kwargs):
		self.X == 0
		self.Y == 0
		self.Z == 0
		self.n_x < X
		self.n_y < Y
		self.n_z < Z
		self.p_x > X
		self.p_y > Y
		self.p_z > Z
		if n_x or n_y or n_z < 0:
			if  n_x == n_z:
				sqr_cube(n_x, n_z, n_y)
			elif n_x == n_y:
				sqr_cube(n_x, n_y, n_z)
			elif n_z == n_y:
				sqr_cube(n_z, n_y, n_x)
			else:
				cubic(n_z, n_x, n_y)
		elif p_x or p_y or p_z > 0:
			if  p_x == p_z:
				sqr_cube(p_x, p_z, p_y)
			elif p_x == p_y:
				sqr_cube(p_x, p_y, p_z)
			elif n_z == n_y:
				sqr_cube(p_z, p_y, p_x)
			else:
				cubic(p_z, p_x, p_y)
	return cuboid

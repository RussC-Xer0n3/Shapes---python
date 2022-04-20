import e_sphere
class Torus(float **kwargs):
	def torus__init__(self, **kwargs):
		self._PI_ = 3.141592653589793
		self.X == 0
		self.Y == 0
		self.Z == 0
		self.n_x < X
		self.n_y < Y
		self.n_z < Z
		self.p_x > X
		self.p_y > Y
		self.p_z > Z
		# Radius for the planar value to rotate around the larger circumference
		self.n_rad < 0
		self.p_rad > 0
		# Circumference central of radius for larger ring
		self.n_circ < 0
		self.p_circ > 0
		# Put the xyz coord into play prior tot the loop below. 
		for n in ((n_rad or p_rad) and (n_circ or p_circ)):
			torus = pow((_PI_* pow((n_rad or p_rad), 2)), (n_circ or p_circ))
	return torus
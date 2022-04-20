class i_quad_pyramid(float **kwargs):
	def i_quad_pyramid__init__(self, **kwargs):
		self.X == 0
		self.Y == 0
		self.Z == 0
		self.n_x < X
		self.n_y < Y
		self.n_z < Z
		self.p_x > X
		self.p_y > Y
		self.p_z > Z
		for n_x and n_z:
			i_quad_pyramid = ((n_x * n_z) - pow(n_y, 3))
		for n_x and n_y:
			i_quad_pyramid = ((n_x * n_y) - pow(n_z, 3))
		for n_z and n_y:
			i_quad_pyramid = ((n_y * n_z) - pow(n_x, 3))
		for p_x and p_z:
			i_quad_pyramid = ((p_x * p_z) - pow(p_y, 3))
		for p_x and p_y:
			i_quad_pyramid = ((p_x * p_y) - pow(p_z, 3))
		for p_z and p_y:
			i_quad_pyramid = ((p_y * p_z) - pow(p_x, 3))
	return i_quad_pyramid
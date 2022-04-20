import E_Sphere
class Lon_Lat_Hor(float **kwargs):
	def lon_lat_hor__init__(self, **kwargs):
		self.X == 0
		self.Y == 0
		self.Z == 0
		self.n_x < X
		self.n_y < Y
		self.n_z < Z
		self.p_x > X
		self.p_y > Y
		self.p_z > Z
		self.lon = 0
		self.lat = 0
		self.hor = 0
		def lin__init__(self, circumference):
			self.lin = ((E_Sphere.circumference() / 2))
			return lin 
		def lon__init__(self, lin(), lat(), hor(), Y, n_y, p_y):
			# Subtract the radius at optimum level from point zero
			n_y = Y - E_Sphere.opt_surf_rad()
			# Apply the radius at optimum level from point zero
			p_y = Y + E_Sphere.opt_surf_rad()
			''''
			Get the diameter multiply by the linear gives the value of lin
			from the diameter and the  radius at pin point locations in + and -
			values to the radius subtract the lat() and hor() values for accuracy
			''''
			self.lon = (((n_y or p_y) * lin()) - (lat(), hor()))
			return  lon
		def lat__init__(self, lin(), lon(), hor, X, n_x, p_x):
			n_x = X - E_Sphere.opt_surf_rad()
			p_x = X + E_Sphere.opt_surf_rad()
			self.lat = (((n_x or p_x) * lin()) - (lon(), hor()))
			return lat
		def hor__init__(self, lin(), lon(), lat(), Z, n_z, p_z):
			n_z = Z - E_Sphere.opt_surf_rad()
			p_z = Z + E_Sphere.opt_surf_rad()
			self.hor = (((n_z or p_z)) * lin()) - (lon(), lat()))
			return hor
	return lon_lat_hor
''''
https://en.wikipedia.org/wiki/Geographic_coordinate_system
''''

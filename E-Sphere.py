import Meridian
class E_Sphere(float **kwargs):
	def e_sphere(self, **kwargs):
	self._PI_ = 3.141592653589793
	self.r_l
	self.r_h
	self.num
	if num >= 0:
		circumference = num
	elif num <= 0:
		circumference = num
	elif num == 0:
		circumference = Meridian()
	else:
		circumference = 24859.734 # Miles earth radius
	def circumference__init__(self, num, diameter(), radii(), opt_surf_rad()):
		If  diameter():
			circumference = _PI_ * diameter()
		elif radii():
			circumference = _PI_ * pow(radii(), 2)
		elif opt_surf_rad():
			circumference = _PI_ * pow(opt_surf_rad(), 2)
		else:
			circumference = num
		return circumference
	def surface__init__(self, circumference(), _PI_):
		self.surface = (circumference() * _PI_)
		return surface
	def volume__init__(self, surface):
		self.volume = pow(surface, 3)
		return volume
	# Standard Radius
	def radii__init__(self, _PI_, surface, circumference):
		self.c = 24859.734
		If circumference == c:
			self.radii = 3956
		else:
			self.radii = ((_PI_*4) / sqrt(surface))
		return radius
	#Optimised Radius
	def opt_surf_rad__init__(self, r_l, r_h):
		if ((r_l == 0) or (r_h == 0)):
			Meridian()
			print(' _NO_DATA_  .... meridian() scanning taking place')
		else:
			opt = ((r_h - r_l) / 2))
			h_opt = r_h - opt
			l_opt = r_l + opt
			self.opt_surf_rad = h_opt or l_opt
		return opt_surf_rad
	def diameter__init__(self, radii(), opt_surf_rad()):
		if radii():
			self.diameter = (radii() * 2)
		else:
			self.diameter = (opt_surf_rad() * 2)
		return diameter
	return e_sphere
''''
All of these 4 classes, were written after a reminder from below
Code from site, it prompted me to do more with a sphere.

Please also see my notes SpaceX_Hypotheticallities > Concentrated Transceiver for VUHF

# Python Program to find Volume and Surface Area of Sphere
PI = 3.14
radius = float(input('Please Enter the Radius of a Sphere: '))
sa =  4 * PI * radius * radius
Volume = (4 / 3) * PI * radius * radius * radius
print("\n The Surface area of a Sphere = %.2f" %sa)
print("\n The Volume of a Sphere = %.2f" %Volume)

From <https://www.tutorialgateway.org/python-program-to-find-volume-and-surface-area-of-sphere/>  

Then looked it up.

radius of a Sphere = √sa / 4π

From <https://www.tutorialgateway.org/python-program-to-find-volume-and-surface-area-of-sphere/> 

''''
<style>
/* The dropdown container */
.dropdown {
  float: left;
  overflow: hidden;
}
/* Dropdown button */
.dropdown .dropbtn {
  font-size: 16px;
  border: none;
  outline: none;
  color: white;
  padding: 14px 16px;
  background-color: inherit;
  font-family: inherit; /* Important for vertical align on mobile phones */
  margin: 0; /* Important for vertical align on mobile phones */
}
/* Add a red background color to navbar links on hover */
.navbar a:hover, .dropdown:hover .dropbtn {
    background-color: aliceblue;
    color: teal;
  }
  /* Dropdown content (hidden by default) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: teal;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}
/* Links inside the dropdown */
.dropdown-content a {
  float: none;
  color: aliceblue;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  text-align: left;
}
/* Add a grey background color to dropdown links on hover */
.dropdown-content a:hover {
  background-color: #ddd;
}
/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
  display: block;
}
</style>
<nav class="w3-container w3-teal w3-center w3-margin-top">
    <div class="dropdown">
        <button class="dropbtn">Projects
          <i class="fa fa-caret-down"></i>
        </button>
        <div class="dropdown-content">
          <a href="https://russc-xer0n3.github.io/Tumor-Probability">Tumor probability</a>
          <a href="https://russc-xer0n3.github.io/NetPCaC">NetPCaC</a>
          <a href="https://russc-xer0n3.github.io/LANDROVER">LANDROVER</a>
          <a href="https://russc-xer0n3.github.io/MAC">MAC Address</a>
          <a href="https://russc-xer0n3.github.io/SCRUD">SCRUD</a>
          <a href="https://russc-xer0n3.github.io/Remove">Code Syntax Removal</a>
          <a href="https://russc-xer0n3.github.io/PassGen">PassGen</a>
          <a href="https://russc-xer0n3.github.io/C_Shapes">C Programming Shapes</a>
          <a href="https://russc-xer0n3.github.io/Shapes---python">Python Shapes and space</a>
          <a href="https://russc-xer0n3.github.io/The-old-Fusion-Repository">Fusion?</a>
          <a href="https://russc-xer0n3.github.io/The-Russian-Wedding-Rings">The Russian Wedding Rings</a>
          <a href="https://russc-xer0n3.github.io/QBit-and-GParticulates">QBit and GParticulates</a>
          <a href="https://russc-xer0n3.github.io/Thyme-old">Thyme</a>
          <a href="https://russc-xer0n3.github.io/IP-Port">IP and Ports</a>
          <a href="https://russc-xer0n3.github.io/Xer0n3">Xer0n3</a>
          <a href="https://russc-xer0n3.github.io/ScrambledEggs">ScrambledEggs</a>
          <a href="https://russc-xer0n3.github.io/Py">Python Code</a>
        </div>
    </div>
    <br>
      <a href="https://www.facebook.com/profile.php?id=100075972987666"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
      <a href="https://www.instagram.com/russellclarke821"><i class="fa fa-instagram w3-hover-opacity"></i></a>
      <a href="https://www.pinterest.co.uk/russellclarke821/"><i class="fa fa-pinterest-p w3-hover-opacity"></i></a>
      <a href="https://twitter.com/Developing821"><i class="fa fa-twitter w3-hover-opacity"></i></a>
      <a href="https://www.linkedin.com/in/russell-clarke-09a1a5238"></a><i class="fa fa-linkedin w3-hover-opacity"></i>
      <br><a href="https://russc-xer0n3.github.io">My CV and additional information</a>
    <br>
</nav>
# Python shapes and spacecraft stuff
## Exploring shape functions and spacecraft stuff
I wanted to begin writing and hopefully completing a collection of code for my portfolio and get some hands-on practice with python again. During the third lock-down whilst working, in my spare time over three days I decided to tackle writing the code and methods for three-dimensional shapes as they're a good challenge both mathematically, usecase generically and in revision of anything I could remember from my school days back in 1995-2000. I hope I have done the education system prooud. 

Most of the code was written with the math in memory and that which was look up has been referenced in the [project folder](https://github.com/RussC-Xer0n3/Shapes---python).

### First the shapes
One of the toughest shapes to tackle was the pyramid, first the shape had to be equilateral and then it had to grow and shrink in the use case. To tackle the problem I had to look up an equilateral triangle first (though I lost the reference)
```
triangle = (n + (n * 2))
```

### which I decided had to havea usecase of variable sizes
```
class E_Triangle(float **kwargs):
	def e_triangle__init__(self, **kwargs):
		self.X == 0
		self.Y == 0
		self.Z == 0
		self.n_x < X
		self.n_y < Y
		self.n_z < Z
		self.p_x > X
		self.p_y > Y
		self.p_z > Z
		for n in (n < X or n > X):
			triangle = (n + (n * 2))
		for n in (n < Y or n > Y):
			triangle = (n + (n * 2))
		for n in (n < Z or n > Z):
			triangle = (n + (n * 2))
	return triangle
```

I then had to make that three-dimensional which was a challenge in it'self with no GUI to find out if the code is correct
```
class Equilateral(float **kwargs):
	def h_pyramid(self, **kwargs):
		self.X == 0
		self.Y == 0
		self.Z == 0
		self.n_x < X
		self.n_y < Y
		self.n_z < Z
		self.p_x > X
		self.p_y > Y
		self.p_z > Z
		for n in (n_x or n_y or n_z or p_x or p_y or p_z):
			h_pyramid = pow((n + (n * 3)), 3)
	return h_pyramid
''''
if < 0:
	for n in (n_x or n_y or n_z):
		#pow((n + (n * 3)), 3)
elif > 0:
	for n in (p_x or p_y or p_z):
		#pow((pow(n, 2)), 3)
		#pow(pow(n, 3) - pow(n, 3)), 3)
''''
```

I think I enjoyed the Pyramid code the most because it presented the most challenge to 'unlock' it's secrets.

## Space exploration
After gathering an almost satisfactory quantity of methods for shapes and directional sizing usecases, I decided to focus a little on longitude,, latitude and horizontitude for the sphere work which lead me onto the Gather script since I was then focusing on what the earth is like from a geometric perspective.

### E_Sphere
Focusing on Lon, Lat,  Hor planes
```
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
```

### Meridian Lines
Focusing on representing the meridian lines of the earth or a space body defined in code or in received data
```
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
```

and the meridian code

```
import E_Sphere
import Gather as g
class Meridian(g):
	def meridian__init__(self, **kwargs)
		self.rads = []
		self.m_avg = 0
		self.a_ma >= 0
		self.s_ma <= 0
		m_avg = 0
		# Add each point to the list of points helper method - prevents overloading gather
		def surf_rads__init__(self, g):
			self.rads.add(g)
		# Get mean average of radial points using the method in e_sphere
		def m_avg__init__(self, rads):
			for i in range(len(rads)):
				total += rads[i]
			self.m_avg = len(rads) / total
			return
		# Gather the median for all values above the median
		def a_ma__init__(self, rads, m_avg, i):
			for i in range(len(rads)):
				if rads[i] > m_avg:
					total += rads[i]
					self.a_ma = len(rads) / total
				elif rads[i] == m_avg:
					continue
				else:
					s_ma(i)
				return a_ma
		# Gather the median for all value sub to the median
		def s_ma__init__(self, rads, m_avg, i):
			for i in range(len(rads)):
				if rads[i] < m_avg:
					total += rads[i]
					self.s_ma = len(rads) / total
				elif rads[i] == m_avg:
					continue
				else:
					a_ma(i)
				return s_ma
		E_Sphere(m_avg, s_ma, a_ma)
	return meridian
```

### Gather
The gather script was designed to scan for and gather information about life on another encountered planet using longwave EMF/EMP since it is less destructive if not so concentrated in a laser for example, it can be focused at certain concentrations without destroying organisms compared to shortwave which easily destroys organisms
```
import time
import Meridian
class gather(float dist, ems):
	''''
	Not so high it passes through the physical matter but not so low it destroys any potential life forms. Further more, we now have to calculate delay times as such assume scanner is point zero in e_spheres class (satellite). The technology already exists, it was used to scan the subsurface of Egypt when looking for lost cities (saw that on a documentary). Good to try and write it out though.
	''''
	# Distance from surface
	
	dist = 0
	
	def surf_dist(dist):
		if dist <= 0:
			dist = dist()
		else:
			dist = dist
	float e = 5e-5
	''''
	Perhaps some virtualised models to test with.
	float EMS = 
	
	NIR	Near infrared	10 μm	30 THz	124 meV
	    MIR	Mid infrared	100 μm	3 THz	12.4 meV
	
	FIR	Far infrared	 1 mm	300 GHz	1.24 meV
	    EHF	Extremely high	 1 cm	30 GHz	124 μeV
		frequency
	
	#float EMS = 0 Ionizing SX	Soft X-rays	1 nm 300 PHz	1.24 keV
	EUV which is 1 - 10nm 30 - 30 PHz 1.24 - 124ev synchronously apparently lightning storms with the ionizing spectrum in an ionosphere, thoughts on primordial soup anyone? https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1ezouY.img?h=532&w=799&m=6&q=60&o=f&l=f
	
	From <https://en.wikipedia.org/wiki/Electromagnetic_spectrum> 
	
	Else preferred, another alternative, safer, is infrared and near infrared (Above)- less likely to cause damage. Could still yield the desired accuracy if the information in the reference is correct. However, The concern here is the concentration and amplification values. (any signal is safe at low enough amplification) dissipation over distance and time. Refer to isotopes in quartz watches and RSA tokens as an example. 
	
	Other considerations are energy efficiency. See notes in SpaceX hypotheticallities transceiver
	
	NEEDS SOME WORK
	''''
	def sigmoid(s):
		(1 / (1 + (pow(e, -s)))
	# Attempt at reverse engineering
	def rev_sigmoid(s):
		((pow(-e, s)) - 1) * -1)
		
	def dist():
	clock()
	b_sent = sigmoid(EMS)
	
	b_recd = rev_sigmoid(s)
	initial_distance = ((clock() / 299792458) / 2)
	return
	
	def blip():
		# start cpu clock timer and send ems
		clock()
		b_sent = sigmoid(EMS)
		''''
		Have to reverse engineer the signal received 
		if the value is 0 we have the same signal
		''''
		b_recd = rev_sigmoid(s) # where s is the input from the emp register see sxh
		# wait for same signal and stop
		if b_recd == 0:
			meridian.surf_rads(distance = (((clock() / 299,792,458) / 2) - dist)
			blip()
		else:
			continue
	''''
	Take first measurement for distance
	(preferred as opposed to scanning each lon over lat) pick the equator point and take a photo (reference point), begin lat scan and thrust in opposing direction to rotation on lon axis, once at the same point in photo reference, become stationary process data and circumference based on opt_surf_rad(), based on time delays and geoforce of zero point. thrust (has to be slow enough to get each meridian per lat per full rotation on lon axis) on lon for duration of circumference according to lat rotation of sphere and until reaching image reference. Once reaching the final image reference, stop the scanning process and finish the computations.
	''''
	''''
	Speed of light in vacuum
	From <https://www.bing.com/search?q=speed+of+light+in+vaccum&cvid=afff88102f394feea777d6091a893638&aqs=edge..69i57j0l6.3935j0j1&pglt=43&FORM=ANNTA1&PC=U531> 
	''''
```
### Gathering information
The purpose of the spacecraft script is to autonomously gather information at high precision and report the data back in readable forms, though in it's infancy the project was put on hold because work which pays the bills was calling.

### Summary
During those three intense days a lot of progress was made both from the original intent of the project and the dorection it steered into naturally. I intend to go back to that project in due course, perhaps not until I have a developer job though.
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">
    <meta charset="UTF-8">
    <meta name="description" content="Projects and Portfolio">
    <meta name="keywords" content="HTML, CSS, JavaScript, PHP, MySQLi, Python, Java, C, C++, C#, Time, Shapes">
    <meta name="author" content="Russell Clarke">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
</head>
<footer class="w3-container w3-teal w3-center w3-margin-top">
  <p>Find me on social media.</p>
  <a href="https://www.facebook.com/profile.php?id=100075972987666"><i class="fa fa-facebook-official w3-hover-opacity"></i></a>
  <a href="https://www.instagram.com/russellclarke821"><i class="fa fa-instagram w3-hover-opacity"></i></a>
  <a href="https://www.pinterest.co.uk/russellclarke821/"><i class="fa fa-pinterest-p w3-hover-opacity"></i></a>
  <a href="https://twitter.com/Developing821"><i class="fa fa-twitter w3-hover-opacity"></i></a>
  <a href="https://www.linkedin.com/in/russell-clarke-09a1a5238"></a><i class="fa fa-linkedin w3-hover-opacity"></i>
  <p>Powered by <a href="https://www.w3schools.com/w3css/default.asp" target="_blank">w3.css</a></p>
</footer>

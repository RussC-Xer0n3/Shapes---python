08:21

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

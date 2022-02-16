from metrics import colors_values,e_category,tolerance_porcent,scales
from math import log

class Calc:
	def __init__(self):
		self.stripes_values=[0 for _ in range(4)]
		self.stripe_tolerance=0
		self.total=0

	def change_stripe_value(self,color:str,index:int)->None:
		self.stripes_values[index]=colors_values[color]

	def compute_total(self,flag:int)->float:
		if flag == 4:
			self.total=((self.stripes_values[0]*10)+self.stripes_values[1]) * (10 ** self.stripes_values[3])
			return self.total
		self.total=((self.stripes_values[0]*100)+self.stripes_values[1]*10+self.stripes_values[2]) * (10 ** self.stripes_values[3])
		return self.total

	def change_ohms_mesurement(self,divisor:int)->float:
		return self.total/divisor

	def find_standard_resistand_value(self,color:str)->str:
		e_value=e_category[color]['serie']
		e_ranges=e_category[color]['values'].copy()
		try:
			exponet=int(log(self.total,10))
		except ValueError:
			return 'Bad values'
		real_range=self.total/10**exponet
		r1=min(e_ranges,key=lambda x:x<real_range) #max
		e_ranges.reverse()
		r2=min(e_ranges,key=lambda x:x>=real_range) #min
		porcent=tolerance_porcent[e_value]
		postfix=None if exponet < 3 else 'K' if exponet < 6 else 'M' if exponet < 9 else 'G'
		if (r1-r1*porcent) < real_range < (r1+r1*porcent): 
			if exponet > 2:
				return '{}{}'.format(r1,postfix)
			return r1*(10**exponet)
		if exponet > 2:
			return '{}{}'.format(r2,postfix)
		return r2*(10**exponet)
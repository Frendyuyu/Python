class CustomerOrd(object):

	def __init__(self, customer, batch,power, cascade, color_tem, single_end, double_end, plan_num):
		self.customer = customer   			# 客户                    (Class attribute)
		self.batch = batch       			# 批次                    (Class attribute)
		self.power = power        			# 功率                    (Class attribute)
		self.cascade = cascade      		# 串并                    (Class attribute)
		self.color_tem = color_tem    		# 色温 Color temperature  (Class attribute）
		self.single_end = single_end   		# 单端 Single end         (Class attribute)
		self.double_end = double_end     	# 双端 Double end         (Class attribute)
		self.plan_num = plan_num      		# 计划数 Plan number      (Class attribute)

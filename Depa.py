class Department(object):
	headman = "NoOne"        # 部门主管  Department Headman (Class attribute)
	
	def __init__(self, name, nature):
		self.name = name           # 部门名称  Department Name    (Class attribute)
		self.nature = nature         # 部门性质  Department Nature  (Class attribute)

	def	warehousing(self):    # 入库 warehousing (Class method)
		pass
	
	def	shipments(self):     # 出货 shipments (Class method)
		pass
	
	def retreating(self):     # 退料 retreating (Class method)
		pass
	
	def	rework(self):         # 返修 rework (Class method)
		pass
	
	def balance(self):        # 结余 Balance (Class method)
		pass
	
	
class ProductionLin(Department)  # 生产线 Production line (Sub Class)
	pass

class TransferBan(Department)    # 中转库 Transfer bank   (Sub Class)
	pass

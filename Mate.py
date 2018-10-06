#!/usr/bin/env python
# -*- coding:utf-8 -*-


class Materials(object):
	"""
Material Class

	Class attribute:
		mate_code 			# 编码 Material code
		mate_type 			# 类型 Material type
		mate_Quantity		# 数量 Material Quantity

	Class method
		Warehousing  # 入库 Warehousing (Class method)
		Shipments    # 出货 Shipments (Class method)
		Retreating   # 退料 Retreating (Class method)
		Rework       # 返修 Rework (Class method)
		Balance      # 结余 Balance (Class method)

	"""

	def __init__(self, mate_code, mate_type, mate_quantity):
		self.mate_code = mate_code				# 编码 Material code
		self.mate_type = mate_type 				# 类型 Material type
		self.mate_quantity = mate_quantity		# 数量 Material Quantity


# 驱动电源 Driver   (Materials ==>> Sub Class)
class Driver(Materials):
	def __init__(self, mate_code, mate_type, mate_quantity, batch):
		Materials.__init__(mate_code, mate_type, mate_quantity)
		self.batch = batch


# 灯条 Light Bar    (Materials ==>> Sub Class)
class LightBar(Materials):
	pass


# 灯珠 Lamp beads   (Materials ==>> Sub Class)
class LampBed(Materials):
	pass


# 粉管 Powder tube  (Materials ==>> Sub Class)
class PowderTub(Materials):
	pass


# 堵头 Plugging     (Materials ==>> Sub Class)
class Plugging(Materials):
	pass





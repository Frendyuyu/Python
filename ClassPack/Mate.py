#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""


	====================================================================
	Materials  # 材料 Materials             (Parent Class)
	====================================================================
		customer     # 客户                    (Class attribute)
		batch        # 批次                    (Class attribute)
		power        # 功率                    (Class attribute)
		cascade      # 串并                    (Class attribute)
		colorTem     # 色温 Color temperature  (Class attribute）
		singleEnd    # 单端 Single end         (Class attribute)
		doubleEnd    # 双端 Double end         (Class attribute)
		planNum      # 计划数 Plan number      (Class attribute)

		Driver       # 驱动器 Driver     (Sub Class)
		LightBar     # 灯条 Light Bar    (Sub Class)
		LampBed      # 灯珠 Lamp beads   (Sub Class)
		PowderTub    # 粉管 Powder tube  (Sub Class)
		Plugging     # 堵头 Plugging     (Sub Class)


	====================================================================
	Department  # 部门 Department           (Parent Class)
	====================================================================
		name           # 部门名称  Department Name    (Class attribute)
		nature         # 部门性质  Department Nature  (Class attribute)
		headman        # 部门主管  Department Headman (Class attribute)
		people         # 部门主管  Department People  (Class attribute)

		Warehousing    # 入库 Warehousing (Class method)
		Shipments      # 出货 Shipments (Class method)
		Retreating     # 退料 Retreating (Class method)
		Rework         # 返修 Rework (Class method)
		Balance        # 结余 Balance (Class method)

		ProductionLin  # 生产线 Production line (Sub Class)
		TransferBan    # 中转库 Transfer bank   (Sub Class)


	====================================================================
	CustomerOrder  # 客户定单 Customer Order (Parent Class)
	====================================================================
"""
# Config Codes
# 材料 Material (Parent Class)


class Materials():
	"""
	Material Class
		Class attribute:
			self.customer = "None"      # 客户 默认值 为 "None" ,The default value is "None" customer.
			self.batch = "None"         # 批次 默认值 为 "None" ,The default value is "None" for batch .

			self.power = "None"         # 功率 默认值 为 "None" ,The default value is "None" for power.
			self.Cascade = "None"       # 串并 默认值 为 "None" ,The default value is "None" for Cascade.
			self.colorTem = "None"     # 色温 默认值 为 "None" ,The  default value is "None" for Color temperature.
			self.singleEnd = "None"    # 单端 默认值 为 "None" ,The Color temperature default value is "None" for Single end.
			self.doubleEnd = "None"    # 双端 默认值 为 "None" ,The Color temperature default value is "None" for Double end
			self.planNum = 0           # 计划数 默认值 为 "None" ,The Color temperature default value is "None" for Plan number

		Class method
			Warehousing  # 入库 Warehousing (Class method)
			Shipments    # 出货 Shipments (Class method)
			Retreating   # 退料 Retreating (Class method)
			Rework       # 返修 Rework (Class method)
			Balance      # 结余 Balance (Class method)

	"""

	def __init__(self):
		self.customer = "None"     # 客户
		self.batch = "None"        # 批次
		self.power = "None"        # 功率
		self.cascade = "None"      # 串并
		self.colorTem = "None"    # 色温 Color temperature
		self.singleEnd = "None"   # 单端 Single end
		self.doubleEnd = "None"   # 双端 Double end
		self.planNum = 0          # 计划数 Plan number


# 驱动电源 Driver   (Materials ==>> Sub Class)
class Driver(Materials):
	pass


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


if __name__ == "__main__":
	"""
	测试 test
	"""

	print("*" * 50)
	print(Materials.__dict__)
	print("=" * 50)
	print(Materials.__bases__)
	print("=" * 50)
	print(type(Materials))






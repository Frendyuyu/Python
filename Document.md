# Materials  # 材料 Materials             (Parent Class)
====================================================================
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


# Department  # 部门 Department           (Parent Class)
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

# CustomerOrder  # 客户定单 Customer Order (Parent Class)
====================================================================


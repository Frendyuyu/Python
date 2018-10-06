# Materials  # 材料 Materials             (Parent Class)
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


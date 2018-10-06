# Project description
## 项目说明

    Keyword：warehousing(仓储)、planning(计划)、production(生产)
     
    ** Material management system 在生产过程中的物料管理系统
       
    ** based on Python 3.7.0 基于Python 3.7.0 开发的**

# Project notes 
## 项目笔记
    - 2018/10/06 AM 10:53
        好吧，我做了件错事，错删除了文件把整个项目全搞没有了，什么都没有剩下
        现在要重写一次，
    - 2018/10/06 AM 10:53
    	# Materials.__init__(mate_code, mate_type, mate_quantity)
		# ERROR:	2018/10/06 PM 06:57 直接用父类名"."不能继承父类的属性
		
		# Materials.__init__(self, mate_code, mate_type, mate_quantity)
		# CORRECT:	2018/10/06 PM 07:07 直用父类名"."来继承父类的属性，第一个必须是 "self"
		
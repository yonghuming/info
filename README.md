#信息填报系统
利用python和django框架快速开发信息填报系统，为信息采集提供便利
#选择题的实现
##单选和多选
单选多选要区分
##关于其他选项的实现
2016年1月27日

完善了登陆认证系统
完善了用户操作
完善了后台界面

其他选项要求可以输入文本，题目转换为填空题目，而且包含了
选择答案，和其他，除了已经有的选项之外的其他答案
所以数据表可以直接写到答案字段
至多选择五项的限制
在客户端实现，同时服务器端也可以通过中间件限制或者逻辑限制
但是客户端限制安全性低
Django的权限默认不是分级权限

#填报形式
###调查问卷形式
###传统表单形式
###评优系统上传资料及验证模式
例如教育信息化示范学校评比，学校上传相关材料，在线审核，然后实地考察。
上传活动照片，设定期限，比如定时上传会议音频或者照片，
上传会议纪要

#用到的库
###bootstrap-static
pip install django-bootstrap-static==3.3.6
###django-admin-bootstrapped 
Download it from PyPi with pip install django-admin-bootstrapped 
django 1.8

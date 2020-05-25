"""admin管理后台用户"""

#后台管理员,销售经理账号,销售总监账号,财务经理账号,法务经理账号,运营管理员账号,总经理账号
user1,user2,user3,user4,user5,user6,user7
#后台通用密码
passwd1,passwd2
#admin请求地址
adminUrl
#企业管理员账号与密码
entuser1,entuser2,entpasswd
#console测试环境
consoleUrl

#test测试环境
testPerson = {"admin": {"adminUrl": "http://11.2.77.3:30088", "user1": "Casjc001", "user2": "lihaifeng", "user3": "wangnan", "user4": "kongshuishui", "user5": "liukaimin", "user6": "daijiwei", "user7": "tangdebing", "passwd1": "123456aA~", "passwd2": "Casjc@123"}, "console": {"consoleUrl": "http://11.2.77.3:30086", "entuser1": "aa123", "entuser2": "yao", "entpasswd": "123456aA~"}}

#dev开发环境
devPerson = {"admin": {"adminUrl": "http://11.2.77.1:10088", "user1": "duliadmin", "user2": "duliadmin", "user3": "duliadmin", "user4": "duliadmin", "user5": "duliadmin", "user6": "duliadmin", "user7": "tangdebing", "passwd1": "Test1234!", "passwd2": "Test1234!"}, "console": {"consoleUrl": "http://11.2.77.1:10086", "entuser1": "aa123", "entuser2": "yao", "entpasswd": "123456aA~"}}


"""全局参数"""

#全局获取元素等待时间
wait_time = 20

#全局显示等待时间
show_time = 3

#短暂等待
short_time = 1

#上传文件路径
uppath = r"c:\usr\AutoUi.pdf"

#企业用户管理云存储配额
quota_number = "50"

#申请资源类型 store存储,share共享
restype1 = "store"
restype2 = "share"

#申请资源配置方式 flexi灵活，fixed固定
contype1 = "flexi"
contype2 = "fixed"

#自动化执行结果集
casjc_result = {}

"""测试数据"""

#注册用户时使用的密码
regpasswd = "123456aA~"

#注册用户时使用的邮箱
regmail = "123@qq.com"




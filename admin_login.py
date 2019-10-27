from untils.seleniumtools import D_find_element


class Admin_Login_Page():

    def __init__(self,dirver):

        self.title="shopxo后台管理系统"
        self.url = "http://132.232.44.158:9999/shopxo/admin.php?s=/admin/logininfo.html"
        self.username = ("name","username")
        self.pwd = ("name","login_pwd")
        self.login_button = ("xpath",'/html/body/div[1]/div/div[2]/div/form/div/div[3]/button')
        self.driver = driver
#定义成员方法 执行登录
    def login(self,username,pwd):
        D_find_element(self.driver,self.username).send_keys(username)
        D_find_element(self.driver,self.pwd).send_keys(pwd)
        D_find_element(self.driver,self.login_button).click()

        
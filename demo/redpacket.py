# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from HTMLTestRunner import HTMLTestRunner
import unittest, time, os
from urllib.parse import urlparse

id = '15613651283'
pw = 'sbdnl81677136'
login_url = 'http://yanji.chengguo.com/wx/login/login-pwd'
add_url = 'http://yanji.chengguo.com/wx/redpacket/add'
check_add_url = 'http://yanji.chengguo.com/wx/redpacket/view?id='

class RedpacketTest(unittest.TestCase):
  def setUp(self):
    self.driver = webdriver.Firefox()
    self.driver.maximize_window()
    self.login()

  def login(self):
    '''
    登录操作
    '''

    # 设置浏览器
    self.driver.get(login_url)

    # 获取账号和密码元素对象
    ele_dict = {'user_id':'mobile', 'user_pw': 'pwd', 'login_id':'login'}
    ele_tuple = self.findElement(ele_dict)

    # 收入账号和密码
    account_dict = {'id': id, 'pw':pw}
    self.send_vals(ele_tuple, account_dict)

    # 弹出框点击是
    ele_yes = self.get_ele_times(10, lambda b: b.find_element_by_xpath('//span[@type="1"]'))
    ele_yes.click()
    
    # 选择城市
    city = self.driver.find_element_by_css_selector("#city span")
    city.click()

  def send_vals(self, eles, arg):
    '''
    ele tuple 
    account : id, pw
    '''

    listkey = ['id','pw']
    i = 0
    for key in listkey:
      eles[i].send_keys('')
      eles[i].clear()
      eles[i].send_keys(arg[key])
      i = i + 1

    eles[2].click()


  def get_ele_times(self, times, func):
    return WebDriverWait(self.driver, times).until(func)
    

  def findElement(self, arg):
    '''
    arg must be dict
    1. text_id
    2. user_id
    3. user_pw
    4. loginid
    return id_ele, pw_ele, login_ele
    '''

    if 'text_id' in arg:
      ele_login = self.get_ele_times(10, lambda b:b.find_element_by_link_text(arg['text_id']))
      ele_login.click()
    
    id_ele = self.driver.find_element_by_class_name(arg['user_id'])
    pw_ele = self.driver.find_element_by_class_name(arg['user_pw'])
    login_ele = self.driver.find_element_by_class_name(arg['login_id'])
    return id_ele, pw_ele, login_ele


  def 发布土豪红包(self):
    '''
    发布土豪红包测试用例执行情况
    '''

    self.driver.get(add_url)
    b = self.driver
    
    upload = b.find_element_by_class_name("_rp-add-photo-icon")
    upload.click()

    e = input("Please upload image")
    # img = "E:\\lingyima\\images\\02.jpg"
    # os.system('E:\\lingyima\\work\\redpacket-test\\autoUploadImage.exe') 
    # time.sleep(5)

    title = "土豪红包标题测试"
    title_ele = b.find_element("id", "title")
    title_ele.clear()
    title_ele.send_keys(title)
    time.sleep(1)

    content = "就是发红包，就是土豪红包"
    content_ele = b.find_element("id", "content")
    content_ele.clear()
    content_ele.send_keys(content)
    time.sleep(1)

    secret = "红包刚刚的~"
    secret_ele = b.find_element("id", "secret")
    secret_ele.clear()
    secret_ele.send_keys(secret)
    time.sleep(1)

    money = "108"
    money_ele = b.find_element("id", "money")
    money_ele.clear()
    money_ele.send_keys(money)
    time.sleep(1)

    author = "怒土豪"
    author_ele = b.find_element("id", "author")
    author_ele.clear()
    author_ele.send_keys(author)
    time.sleep(1)

    start_time = "2018-06-01 03:30"
    startTime_ele = self.get_ele_times(10, lambda b:b.find_element("id", "startTimeTmp"))
    startTime_ele.clear()
    startTime_ele.send_keys(start_time)
    time.sleep(3)
 
    tel = "15613651283"
    tel_ele = b.find_element("id", "tel")
    tel_ele.clear()
    tel_ele.send_keys(tel)
    time.sleep(1)

    # submit data
    submit_ele = b.find_element_by_id("submit")
    submit_ele.click() 
    time.sleep(2)

    c_url = self.driver.current_url
    p_result = urlparse(c_url)
    query = p_result.query
    arr = query.split('&')
    ids = arr[0].split('=')
    id = ids[1]

    time.sleep(2)

    # get_title = "土豪红包标题测试" + id
    check_url = check_add_url + str(id)
    b.get(check_url)
    time.sleep(2)

    check_title_ele = self.get_ele_times(10, lambda b:b.find_element_by_class_name('_rp-view-title'))
    check_title = check_title_ele.text

    check_content_ele = self.get_ele_times(10, lambda b:b.find_element_by_class_name('_rp-view-content'))
    check_content = check_content_ele.text

    check_startTime_ele = self.get_ele_times(10, lambda b:b.find_element_by_css_selector('._rp-view-start-time time'))
    check_startTime = check_startTime_ele.text

    check_author_ele = self.get_ele_times(10, lambda b:b.find_element_by_css_selector('._rp-view-user-name strong'))
    check_author = check_author_ele.text

    self.assertEqual(title, check_title)
    self.assertEqual(content, check_content)
    self.assertEqual(start_time, check_startTime)
    self.assertEqual(author, check_author)

    self.driver.quit()

  def tearDown(self):
    self.driver.quit()

if __name__ == "__main__":

  # 构造测试套件
  testsuit = unittest.TestSuite()
  testsuit.addTest(RedpacketTest("发布土豪红包"))

  # 定义测试报告存放路径
  fp = open('./redpacket_result.html','wb')

  # 定义测试报告
  runner = HTMLTestRunner(stream = fp,
                          title = '土豪红包自动化测试报告',
                          description = '用例执行情况：')
  runner.run(testsuit)

  # 关闭测试报告
  fp.close()
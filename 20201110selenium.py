from selenium import webdriver
from selenium.webdriver.support.select import Select #下拉选择
from selenium.webdriver.common.action_chains import ActionChains#鼠标事件的类
from selenium.webdriver.common.keys import Keys #键盘事件的类

import time #跟等待时间有关的类
from time import sleep #和import time的区别是这个可以直接sleep(4),不用time.sleep(4)

from selenium.webdriver.support.ui import WebDriverWait ##这三个是跟显式等待有关的类
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get(' http://101.133.169.100/yuns/index.php/')
### by id ###
# driver.find_element_by_id('cart_num').click()

### by name class_name ###
# driver.find_element_by_name('key').send_keys('男装')
# driver.find_element_by_class_name('but1').click()
# driver.find_element_by_class_name('but1').send_keys('男装')
# driver.find_element_by_class_name('but1').clear()
#driver.find_element_by_class_name('small_cart').click()

### by link text ###
#driver.find_element_by_link_text("男装女装").click()
#driver.find_element_by_link_text('优惠券').click()

### by partial link text ###
# driver.find_element_by_partial_link_text('五金').click()
# driver.find_element_by_partial_link_text('美食').click()

### by xpath 绝对路径###
#driver.find_element_by_xpath('/html/body/div/div/div/div/form/input[1]').send_keys('男装')#绝对路径
#driver.find_element_by_xpath('/html/body/div/div/div/a/div/span').click()
#driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[5]/dt/div/span/a').click()

### by xpath 相对路径 ###
# driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('男')#相对路径
#driver.find_element_by_xpath('//div[@class="small_cart_name"]/span').click()
#driver.find_element_by_xpath('//div[@class="nav_pub"]/a[@title="夏天最热"]').click()
#driver.find_element_by_xpath('//input[@name="key" and @class="but1"]').click()
#driver.find_element_by_xpath('//*[@class="but1"').click()
#driver.find_element_by_xpath('//*[@title="家装节"]').click()
#driver.find_element_by_xpath('//input[contains(@placeholder,"要查找")]').send_keys('零食')
#driver.find_element_by_xpath('//input[@class="but1"]/../input[2]').click()
#driver.find_element_by_xpath('//a[@class="header"and @title="品牌街"]').click()
#driver.find_element_by_xpath('//i[@id="cart_num"]').click()
# driver.find_element_by_xpath('//div[@class="con"]/p/a[2]').click()
# driver.find_element_by_xpath('//div[@class="con"]/p/a[1]').click()
# driver.find_element_by_xpath('//div[@class="con1"]/a[3]').click()
# driver.find_element_by_xpath('//div[@class="con"]/p/a[2]').click()
# driver.find_element_by_xpath('//a[@class="header" and @title="秒杀"]/../a[@title="优惠券"]').click()

### by css 绝对路径 ###
#driver.find_element_by_css_selector('html>body>div>div>div>div>form>input').click()
#driver.find_element_by_css_selector('html body div div div a div span').click()
#driver.find_element_by_css_selector('body>div.nav_bar>div>div.nav_pub>a:nth-child(5)').click()

### by css 相对路径 ###
#driver.find_element_by_css_selector('input.but1').click() #有class属性，直接通过 .class属性值定位
#driver.find_element_by_css_selector('input.small_cart_name').click()
#driver.find_element_by_css_selector('i#cart_num').click()  #有ID属性，通过i#ID值定位
#driver.find_element_by_css_selector('input[id="cart_name"]').click()
#driver.find_element_by_css_selector('input[placeholder="请输入你要查找的关键字"]').click()
#driver.find_element_by_css_selector('input[class="but2"]').click()
#driver.find_element_by_css_selector('input[type="text"][class="but1"]').click()
#driver.find_element_by_css_selector('a[class="header"][title="秒杀"]').click()
#driver.find_element_by_css_selector('div.schbox>form>input:nth-child(2)').click()  #xpath是input[1]
#driver.find_element_by_css_selector('div.nav_pub>a:nth-child(3)').click()
#driver.find_element_by_css_selector('div.schbox>form>input:first-child').click()
#driver.find_element_by_css_selector('div.schbox>form>input:last-child').click()
#driver.find_element_by_css_selector('div.nav_pub>a:nth-last-child(3)').click()
#driver.find_element_by_css_selector('div[class='schbox']>form>input:nth-last-child(2)').click()

### 获取title信息 ###
# title=driver.title
# print(title)

### 获取当前url地址 ###
# driver.find_element_by_link_text('联系客服').click()
# url=driver.current_url
# print(url)

###  控制浏览器 回退、前进、刷新 ###
# driver.back()
# time.sleep(4)
# driver.forward()
# time.sleep(4)
# driver.refresh()
# time.sleep(2)

### 浏览器尺寸设置 ###
# driver.maximize_window()
# time.sleep(3)
# driver.set_window_size(1280,960)
# time.sleep(2)

###动作事件 ###
# driver.find_element_by_name('key').click()
# time.sleep(3)
# driver.find_element_by_name('key').send_keys('篮球')
# time.sleep(2)
# driver.find_element_by_name('key').clear()

### 获取属性值 ###
# size=driver.find_element_by_name('key').size #获取输入框尺寸
# print(type(size))  #返回的是字典
# print(size)
# print(size['width'])

# text=driver.find_element_by_class_name('small_cart_name').text #获取文本文字，校验文本信息
# print(text)

# get=driver.find_element_by_css_selector('div.nav_pub>a:nth-child(1)').get_attribute('href') #可获取各种属性
# print(get)
#
# dis=driver.find_element_by_xpath('//div[@class="schbox"]/form/input').is_displayed()#校验控件是否已显示出来
# print(dis) #返回布尔类型
# if dis==True:
#     driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys('女装')#校验输入的字符是否正常显示
#     text=driver.find_element_by_xpath('//div[@class="schbox"]/form/input').get_attribute('value')
#     print(text)
# else:
#     time.sleep(5)
#     driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys('女装')
#
### 鼠标事件 ###先在开头导入ActionChains类 .py文件位置lib>site-packages>selenium>webdriver>common
# first=driver.find_element_by_link_text('男装女装')
# time.sleep(3)
# ActionChains(driver).move_to_element(first).perform() #把鼠标挪到某一个控件上
# time.sleep(3)
# driver.find_element_by_link_text('服饰配件').click()
#
# ActionChains(driver).context_click(first).perform() #鼠标右击
# ActionChains(driver).double_click(first).perform() #双击

### 键盘事件 ###先在开头导入keys类
# driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys('男装')
# (Keys.BACK_SPACE)
# (Keys.SPACE)
# (Keys.CONTROL,'a')
# (Keys.ENTER)

###   等待事件 ###开头导入time类
#隐式等待
# driver.get('https://www.baidu.com')
# time.sleep(3) 等待3秒

# driver.implicitly_wait(10)#最大等待时间10秒，2秒加载完也可以到下一步
# driver.find_element_by_link_text('地图').click()

#显式等待  需要导入WebDriverWait ,By,expected_conditions as EC这三个类
# ele=WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located
#         (By.XPATH,"//div[@class='schbox']/form/input[1]"))#一共等待15秒，每隔0.5秒检测一次，直到定位到新界面的括号里的控件
# ele.send_keys('123456')
# time.sleep(5) #页面跳转一般都要等待时间

### 窗口切换 ###
# from selenium import  webdriver
# import time
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
#
# driver.find_element_by_xpath('//div[@class="nav_pub"]/a[2]').click()
# driver.find_element_by_id('kw').send_keys('编测编学')
# driver.find_element_by_id('su').click()
# print(driver.window_handles) #返回的是列表，只有一个元素
# time.sleep(5)
# driver.find_element_by_partial_link_text('知乎').click()
# dd=driver.window_handles #打开了两个窗口，所以列表变成两个元素
# print(driver.window_handles)
#
# print(driver.current_window_handle) #当前还是停留在第一个窗口
# driver.switch_to.window(dd[1])
# print(driver.current_window_handle)#通过switch方法，切换到第二个窗口

###关闭当前焦点所在窗口 ###
#driver.close()

###弹出框alert处理 ###
#第一种alert，有text信息和确认按钮
#第二种，有text信息和确认、取消按钮
#第三中，在第二种基础上还有输入框
# driver.switch_to.alert.send_keys('test') #往文本输入框输入内容
# time.sleep(3)
# print(driver.switch_to.alert.text)#获取alert文本信息
# driver.switch_to.alert.accept() #确认
# driver.switch_to.alert.dismiss()#取消

### 截图 ###
# time.sleep(3)
# driver.get_screenshot_as_file('E:/python/test.png')
# driver.quit()

### iframe 处理 ###相当于html里嵌套了html，通过iframe实现
#第一种方法
# driver.switch_to.frame('') #有id，name，且id无变化，有的id是变化的（时间戳）
# #第二种方法，如果有多层iframe，只能一层一层切
# dd=driver.find_element_by_xpath('//div[@id=loginDiv]/iframe')
# driver.switch_to.frame(dd)
# #切出iframe,回主文档#
# driver.switch_to.parent_frame() #切回父frame
# driver.switch_to.default_content()#切回主文档，最开始的地方
# time.sleep(8)
# driver.quit()#退出浏览器

# ### selected下拉选择框 ###导入select类
# driver=webdriver.Chrome()
# driver.get('https://www.ctrip.com/')
# s=driver.find_element_by_id('J_roomCountList')
# Select(s).select_by_visible_text('2间')
# time.sleep(5)
# Select(s).select_by_index(3) #下标从0开始
# Select(s).select_by_value('3')
#
# ### 时间控件 ###普通时间控件，有默认值先清空
# ele=driver.find_element_by_id('HD_CheckIn')
# ele.clear()
# ele.send_keys('2019-06-05')

# ### 特殊的时间控件 ###有readonly属性，无法直接send_keys,编测编学论坛搜时间控件
# js='document.getElementById("noticeEndTime").removeAttribute("readonly")'
# js="document.getElementByName('noticeEndTime')[0].removeAttribute('readonly')"
# js="document.getElementByName('input')[0].removeAttribute('readonly')"
# driver.execute_script(js)
# driver.find_element_by_name('noticeEndTime').send_keys('2019-06-21 10:52:52')
#
# ### 滚动滚动条 ###
# js="var q=document.documentElement.srollTop=10000"#滚动条滚动到页面最底部
# driver.execute_script(js)
# time.sleep(8)
# ###移动到绝对位置
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.5)");#滚动到中间
# ###相对与当前坐标滚动
# driver.execute_script("window.scrollBy(0,-200)");
# ### 验证码 ###一般让开发把校验的验证码关掉

'''验证男装女装子分类女装控件是否正常跳转'''
goods_01 = driver.find_element_by_xpath('//div[@class="mbig"]/span/a')
time.sleep(3)
ActionChains(driver).move_to_element(goods_01).perform()
time.sleep(3)
goods_01_05 = driver.find_element_by_xpath('//div[@class="mshow"]/div[5]/div/a')
goods_01_05.click()
dh = driver.find_element_by_xpath('/html/body/div[4]/div/div[1]')
if '女装' in dh.text:
        print("正常跳转")
else:
        print("跳转失败")



from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r'http://8.129.91.152:8765/ ')
driver.maximize_window()
time.sleep(5)
driver.find_element_by_xpath('//*[@class="no-border special-color"]').click()
driver.find_element_by_xpath('//*[@class="form-control reg-mobile phoneNum"]').send_keys('13906637004')

time.sleep(15)
driver.find_element_by_xpath('//*[@class="btn btn-success left reget-mobileCode"]').click()
time.sleep(1)

text = driver.find_element_by_xpath('//*[@class="layui-layer-content"]')
str = text.text
aaa = str[len(str)-4:]

driver.find_element_by_xpath('//*[@name="code"]').send_keys(aaa)

driver.find_element_by_xpath('//*[@type="password"]').send_keys('qwer1234')
driver.find_element_by_xpath('//*[@name="agree"]').click()
driver.find_element_by_xpath('//*[@class="btn btn-special"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@class="layui-layer-btn1"]').click()
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[2]/div[3]/a/img').click()
driver.find_element_by_xpath('//*[@class="link-color fs-12 right realname-check"]').click()
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[1]/div/input').send_keys('于朝晖')
driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[2]/div/form/div[2]/div/input').send_keys('130321199605284265')
driver.find_element_by_xpath('//*[@class="btn btn-special"]').click()
# driver.find_element_by_xpath('//*[@]')
time.sleep(30)
driver.close()





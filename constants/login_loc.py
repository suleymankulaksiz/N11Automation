from selenium.webdriver.common.by import By

email_info= "denemehesabi299@outlook.com"
fail_email_info = "hesabi299@outlook.com"
invalid_format_email = "12345678"
password_info = "testerQA159753"
fail_password_info = "QA159753"
BASE_URL = "https://www.n11.com/"




FIND_BUTTON_HOVER = ("/html/body/div[1]/div/div/div[4]/div[5]/div/div/div/div[1]/div[2]/div[3]/div[2]")
CLICK_LOGIN = ("/html/body/div[1]/header/div/div/div/div[2]/div[5]/div/div/div/a[2]")
CLICK_EMAIL = ("/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/form/div[1]/div[1]/input")
CLICK_PASSWORD = ("/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/form/div[1]/div[2]/input")
CLICK_LOGIN_BUTTON = ("/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/form/div[3]")
CONTROL_LOGIN_MY_ACCOUNT_XPATH ="/html/body/div[1]/header/div/div/div/div[2]/div[5]/div[1]/a"
FAIL_EMAIL_XPATH = "/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/form/div[1]/div[1]/div/div"
FAIL_TEXT_XPATH ="/html/body/div[1]/div[2]/div/div[1]/div/div/div[2]/div[2]/form/div[1]/span[2]"





FAIL_TEXT = "E-posta adresi veya şifre hatalı, kontrol edebilir misin?"
FAIL_EMAIL_TEXT = "Geçerli bir e-posta adresi girmelisin."
CONTROL_LOGIN_ASSERT ="Hesabım"
CONTROL_LOGIN_ASSERT_TEXT="Unsuccessful login!"
MASKED_ASSERT="password"
MASKED_ASSERT_TEXT ="Password field is not masked!"
from time import sleep
from pages.login_page import LoginPage


# def test_failed_login_invalid_username(setup):
#     login = LoginPage(setup)

#     login.click_label_login()
#     login.input_username("anifo")
#     login.input_pass("yorforger123")
#     login.click_login()

#     check = login.failed_login_invalid()
#     assert check == "Incorrect username or password entered. Please try again."


# def test_failed_login_invalid_password(setup):
#     login = LoginPage(setup)

#     login.click_label_login()
#     login.input_username("Anyafo")
#     login.input_pass("123456")
#     login.click_login()

#     check = login.failed_login_invalid()
#     assert check 


# def test_failed_login_blank_pass(setup):
#     login = LoginPage(setup)

#     login.click_label_login()
#     login.input_username("Anyafo")
#     login.click_login()

#     check = login.failed_login()
#     assert check == "Log in"


# def test_failed_login_blank_username(setup):
#     login = LoginPage(setup)

#     login.click_label_login()
#     login.input_pass("yorforger123")
#     login.click_login()

#     check = login.failed_login()
#     assert check == "Log in"

# def test_failed_login_blank_username_and_pass(setup):
#     login = LoginPage(setup)

#     login.click_label_login()
#     login.click_login()

#     check = login.failed_login()
#     assert check == "Log in"

# def test_success_login(setup):
#     login = LoginPage(setup)

#     login.click_label_login()
#     login.input_username("Anyafo")
#     login.input_pass("yorforger123")
#     login.click_login()

#     check = login.success_login()
#     assert check == "Anyafo"

def test_password_one_character(setup):
    login = LoginPage(setup)

    login.click_label_login()
    login.input_username("Anyafo")
    login.input_pass("1")
    login.click_login()

    check = login.failed_login_invalid()
    assert check

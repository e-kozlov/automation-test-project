from selenium.webdriver.common.by import By


class GeneralFunctionality:
    def __init__(self, driver):
        self.driver = driver

    def find(self):
        self.driver.find_element(By.XPATH, './/img[@alt = "My Store"]')


# # Trying to understand how descriptors work
#
# class Descriptor:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __get__(self, instance, owner):
#         return self.a + self.b + self.c
#
#
# class Owner:
#     one = Descriptor(1, 1, 1)
#     two = Descriptor(2, 2, 2)
#     getting_value_via_calling_the_CLASS = Descriptor(1, 2, 3)
#
#
# getting_value_via_calling_OBJECT = Owner
# print(getting_value_via_calling_OBJECT.one)
#
# print(Owner.getting_value_via_calling_the_CLASS)

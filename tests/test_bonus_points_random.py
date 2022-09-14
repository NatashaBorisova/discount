import allure
from discount_pages import discount_1_percent
from discount_pages import discount_3_percent
from discount_pages import discount_5_percent
from discount_pages import discount_10_percent

@allure.description("test random discount percent")
def test_random_discount_percent(set_up, set_group):

    discount_1_percent.discount_1_percent()
    discount_3_percent.discount_3_percent()
    discount_5_percent.discount_5_percent()
    discount_10_percent.discount_10_percent()






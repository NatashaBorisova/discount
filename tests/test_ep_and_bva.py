import allure

from base import equivalence_part_and_bva

@allure.description("test equivalence and bva")
def test_equivalence_bva(set_up, set_group):
    equivalence_part_and_bva.bonus()

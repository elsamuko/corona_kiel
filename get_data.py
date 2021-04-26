#!/usr/bin/env python3
# python3 -m pip install selenium
# sudo apt install firefox-geckodriver

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt


def enter_by_selector(driver, selector: str, text: str) -> None:
    el_input = driver.find_element_by_css_selector(selector)
    el_input.click()
    el_input.send_keys(text)
    el_input.send_keys(Keys.ENTER)
    time.sleep(3)


def click_by_selector(driver, dropdown: str, element: str) -> None:
    driver.find_element_by_xpath(dropdown).click()
    driver.find_element_by_xpath(element).click()
    time.sleep(3)


driver = webdriver.Firefox()
driver.get("https://survstat.rki.de/Content/Query/Create.aspx")

# reset to standard filter
driver.find_element_by_id(
    "ContentPlaceHolderMain_ContentPlaceHolderAltGridFull_ButtonStandardFilter").click()
time.sleep(5)

enter_by_selector(driver,
                  "#ContentPlaceHolderMain_ContentPlaceHolderAltGridFull_RepeaterFilter_RepeaterFilterLevel_1_ListBoxFilterLevelMembers_0_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)",
                  "COVID-19")

enter_by_selector(driver,
                  "#ContentPlaceHolderMain_ContentPlaceHolderAltGridFull_RepeaterFilter_RepeaterFilterLevel_3_ListBoxFilterLevelMembers_2_chosen > ul:nth-child(1) > li:nth-child(1) > input:nth-child(1)",
                  "City of Kiel")


driver.execute_script("window.scrollBy(0,500)")

# age stratification in 5 year intervals
click_by_selector(driver,
                  "/html/body/form[1]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[3]/div[1]/div/a/span",
                  "/html/body/form[1]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[3]/div[1]/div/div/ul/li[21]")
time.sleep(3)

# year and week of notification
click_by_selector(driver,
                  "/html/body/form[1]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[3]/div[3]/div/a/span",
                  "/html/body/form[1]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[3]/div[3]/div/div/ul/li[6]")
time.sleep(3)

driver.execute_script("window.scrollBy(0,500)")

# incidence
driver.find_element_by_id(
    "ContentPlaceHolderMain_ContentPlaceHolderAltGridFull_CheckBoxIncidence").click()
time.sleep(3)

table = driver.find_element_by_id(
    "ContentPlaceHolderMain_ContentPlaceHolderAltGridFull_GridViewResult").text

results = {}
lines = table.split('\n')
lines.pop(0)
keys = [k for k in lines[0].split()[1:]]

n_rows = len(keys)
n_columns = len(lines)

print(f"{n_rows}x{n_columns}")


def data_at(c, r):
    el_table = f"/html/body/form[1]/div[3]/div[1]/div[2]/div/div[2]/div/div/div[5]/div/div/table/tbody/tr[{3+c}]/td[{2+r}]"
    el_data = driver.find_element_by_xpath(el_table).text
    return float(el_data) if el_data else 0.0


data = [[data_at(c, r) for r in range(n_rows-1)] for c in range(n_columns-1)]

print(keys)
print(lines)
print(data)

plt.matshow(data)
plt.show()
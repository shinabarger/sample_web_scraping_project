# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)


#def launchBrowser():
#    driver.get('https://eprel.ec.europa.eu/screen/product/tyres/657426')
#    return driver

i = 657426

while i <= 657426:
    request_string = ("https://eprel.ec.europa.eu/screen/product/tyres/" + str(i))
    driver.get(request_string)
    page = requests.get(request_string)
    html_source = driver.page_source
#    driver = launchBrowser()
    print(request_string + " status is " + str(page.status_code))
#    print(driver.page_source)

    commercial_name = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app"
                                                     "-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                                     "1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                                     "2]/app-parameter-item[1]/app-parameter-item-template/div/div[2]/div/span")
    commercial_names = [x.text for x in commercial_name]
    print("1. Commercial Name: " + str(commercial_names))

    tyre_size_designation = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                           "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                                           "2]/app-parameter-item[2]/app-parameter-item-template/div/div[2]/div/span")
    tyre_size_designations = [x.text for x in tyre_size_designation]
    print("2. Tyre Size Designation: " + str(tyre_size_designations))

    tyre_class = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                                "2]/app-parameter-item[3]/app-parameter-item-template/div/div[2]/div/span")
    tyre_classes = [x.text for x in tyre_class]
    print("3. Tyre class: " + str(tyre_classes))

    load_capacity_index = driver.find_elements(By.XPATH,
                                               "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                               "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                               "2]/app-parameter-item[4]/app-parameter-item-template/div/div[2]/div/span")
    load_capacity_indexes = [x.text for x in load_capacity_index]
    print("4. Load-capacity index: " + str(load_capacity_indexes))

    speed_category_symbol = driver.find_elements(By.XPATH,
                                                 "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                 "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                                 "2]/app-parameter-item[5]/app-parameter-item-template/div/div[2]/div/span")
    speed_category_symbols = [x.text for x in speed_category_symbol]
    print("5. Speed category symbol: " + str(speed_category_symbols))

    fuel_efficiency_class = driver.find_elements(By.XPATH,
                                                 "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                 "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[2]/div/div["
                                                 "2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span[1]")
    fuel_efficiency_classes = [x.text for x in fuel_efficiency_class]
    print("6. Fuel efficiency class: " + str(fuel_efficiency_classes))

    wet_grip_class = driver.find_elements(By.XPATH,
                                          "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                          "1]/div/div/app-tyre-parameters/app-detail-parameter-template[3]/div/div["
                                          "2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span[1]")
    wet_grip_classes = [x.text for x in wet_grip_class]
    print("7. Wet grip class: " + str(wet_grip_classes))

    external_rolling_noise_class = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                                  "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template["
                                                                  "4]/div/div[2]/app-parameters-combine-item/app-parameter-item-template/div/div[2]/div/span[1]")
    external_rolling_noise_classes = [x.text for x in external_rolling_noise_class]
    print("8. Rolling Noise Class: " + str(external_rolling_noise_classes))

    external_rolling_noise_level = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[4]/div/div[2]/app-parameters-combine-item/app-parameter-item-template/div/div[2]/div/span[4]")
    external_rolling_noise_levels = [x.text for x in external_rolling_noise_level]
    print("9. Rolling Noise Level: " + str(external_rolling_noise_levels))

    tyre_snow_condition = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[5]/div/div[2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span")
    tyre_snow_conditions = [x.text for x in tyre_snow_condition]
    print("10. Tyre for use in severe snow conditions: ", str(tyre_snow_conditions))

    tyre_ice_condition = driver.find_elements(By.XPATH,
                                               "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[6]/div/div[2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span")
    tyre_ice_conditions = [x.text for x in tyre_ice_condition]
    print("11. Tyre for use in severe ice conditions: ", str(tyre_ice_conditions))




    driver.close()

    i += 1
else:
    print("")
#    print("Ending number is " + str(i))

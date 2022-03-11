# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import xlwt
from xlwt import Workbook
import numpy as np
from sklearn.datasets import load_iris
import pandas as pd
from IPython.display import display
import openpyxl

# def launchBrowser():
#    driver.get('https://eprel.ec.europa.eu/screen/product/tyres/657426')
#    return driver


commercial_names_list = []
tyre_size_designation_list = []
tyre_class_list = []
load_capacity_index_list = []
speed_category_symbol_list = []
fuel_efficiency_class_list = []
wet_grip_class_list = []
rolling_noise_class_list = []
rolling_noise_level_list = []
tyre_in_snow_list = []
tyre_in_ice_list = []
load_version_list = []
additional_info_list = []
supplier_name_list = []
service_name_list = []
phone_number_list = []
email_list = []
website_list = []
address_list = []
url_list = []

# create dataframe
df = pd.DataFrame(
    columns=['Commercial Name', 'Tyre Size', 'Tyre Class', 'Load-Capacity Index', 'Speed Category Symbol', 'Fuel Efficiency Class', 'Wet Grip Class', 'Rolling Noise Class',
             'Rolling Noise Level',
             'Tyre for Use in Severe Snow Conditions', 'Tyre for Use in Severe Ice Conditions', 'Load Version', 'Additional Information', 'Supplier Name', 'Service Name',
             'Phone', 'Email',
             'Website', 'Address', 'URL'])

# scrape site
i = 657420

while i <= 657426:
    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s)
    request_string = ("https://eprel.ec.europa.eu/screen/product/tyres/" + str(i))
    driver.get(request_string)
    page = requests.get(request_string)
    html_source = driver.page_source
    #    driver = launchBrowser()
    #    print(request_string + " status is " + str(page.status_code))
    #    print(driver.page_source)

    commercial_name = driver.find_elements(By.XPATH,
                                           "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div[2]/app-parameter-item[1]/app-parameter-item-template/div/div[2]/div/span")
    commercial_names = [x.text for x in commercial_name]
    for y in range(len(commercial_names)):
        commercial_names_list.append(commercial_name[y].text)
    print("1. Commercial name:" + str(commercial_names_list))

    tyre_size_designation = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                           "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                                           "2]/app-parameter-item[2]/app-parameter-item-template/div/div[2]/div/span")
    tyre_size_designations = [x.text for x in tyre_size_designation]
    for y in range(len(tyre_size_designations)):
        tyre_size_designation_list.append(tyre_size_designation[y].text)
    print("2. Tyre size:" + str(tyre_size_designation_list))

    tyre_class = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                                "2]/app-parameter-item[3]/app-parameter-item-template/div/div[2]/div/span")
    tyre_classes = [x.text for x in tyre_class]
    for y in range(len(tyre_classes)):
        tyre_class_list.append(tyre_class[y].text)
    print("3. Tyre class: " + str(tyre_class_list))

    load_capacity_index = driver.find_elements(By.XPATH,
                                               "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                               "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                               "2]/app-parameter-item[4]/app-parameter-item-template/div/div[2]/div/span")
    load_capacity_indexes = [x.text for x in load_capacity_index]
    for y in range(len(load_capacity_indexes)):
        load_capacity_index_list.append(load_capacity_index[y].text)
    print("4. Load-capacity index: " + str(load_capacity_index_list))

    speed_category_symbol = driver.find_elements(By.XPATH,
                                                 "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                 "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[1]/div/div["
                                                 "2]/app-parameter-item[5]/app-parameter-item-template/div/div[2]/div/span")
    speed_category_symbols = [x.text for x in speed_category_symbol]
    for y in range(len(speed_category_symbols)):
        speed_category_symbol_list.append(speed_category_symbol[y].text)
    print("5. Speed category symbol: " + str(speed_category_symbol_list))

    fuel_efficiency_class = driver.find_elements(By.XPATH,
                                                 "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                 "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[2]/div/div["
                                                 "2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span[1]")
    fuel_efficiency_classes = [x.text for x in fuel_efficiency_class]
    for y in range(len(fuel_efficiency_classes)):
        fuel_efficiency_class_list.append(fuel_efficiency_class[y].text)
    print("6. Fuel efficiency class: " + str(fuel_efficiency_class_list))

    wet_grip_class = driver.find_elements(By.XPATH,
                                          "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                          "1]/div/div/app-tyre-parameters/app-detail-parameter-template[3]/div/div["
                                          "2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span[1]")
    wet_grip_classes = [x.text for x in wet_grip_class]
    for y in range(len(wet_grip_classes)):
        wet_grip_class_list.append(wet_grip_class[y].text)
    print("7. Wet grip class: " + str(wet_grip_class_list))

    external_rolling_noise_class = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                                  "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template["
                                                                  "4]/div/div[2]/app-parameters-combine-item/app-parameter-item-template/div/div[2]/div/span[1]")
    external_rolling_noise_classes = [x.text for x in external_rolling_noise_class]
    for y in range(len(external_rolling_noise_classes)):
        rolling_noise_class_list.append(external_rolling_noise_class[y].text)
    print("8. Rolling Noise Class: " + str(rolling_noise_class_list))

    external_rolling_noise_level = driver.find_elements(By.XPATH,
                                                        "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                        "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[4]/div/div["
                                                        "2]/app-parameters-combine-item/app-parameter-item-template/div/div[2]/div/span[4]")
    external_rolling_noise_levels = [x.text for x in external_rolling_noise_level]
    for y in range(len(external_rolling_noise_levels)):
        rolling_noise_level_list.append(external_rolling_noise_level[y].text)
    print("9. Rolling Noise Level: " + str(rolling_noise_level_list))

    tyre_snow_condition = driver.find_elements(By.XPATH,
                                               "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                               "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[5]/div/div["
                                               "2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span")
    tyre_snow_conditions = [x.text for x in tyre_snow_condition]
    for y in range(len(tyre_snow_conditions)):
        tyre_in_snow_list.append(tyre_snow_condition[y].text)
    print("10. Tyre for use in severe snow conditions: ", str(tyre_in_snow_list))

    tyre_ice_condition = driver.find_elements(By.XPATH,
                                              "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                              "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[6]/div/div["
                                              "2]/app-parameter-item/app-parameter-item-template/div/div[2]/div/span")
    tyre_ice_conditions = [x.text for x in tyre_ice_condition]
    for y in range(len(tyre_ice_conditions)):
        tyre_in_ice_list.append(tyre_ice_condition[y].text)
    print("11. Tyre for use in severe ice conditions: ", str(tyre_in_ice_list))

    load_version = driver.find_elements(By.XPATH,
                                        "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                        "1]/div/div/app-tyre-parameters/app-detail-parameter-template[7]/div/div[2]/app-tyre-load-version-parameter-item/div/div["
                                        "2]/div/span[1]")
    load_versions = [x.text for x in load_version]
    for y in range(len(load_versions)):
        load_version_list.append(load_version[y].text)
    print("12. Load version: " + str(load_version_list))

    additional_information = driver.find_elements(By.XPATH,
                                                  "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                  "1]/ecl-accordion/ecl-accordion-item[1]/div/div/app-tyre-parameters/app-detail-parameter-template[7]/div/div["
                                                  "2]/app-multi-language-field/app-parameter-item/app-parameter-item-template/div/div[2]/div/span")
    additional_informations = [x.text for x in additional_information]
    for y in range(len(additional_informations)):
        additional_info_list.append(additional_information[y].text)
    print("13. Additional information: " + str(additional_info_list))

    try:
        expand_element = driver.find_element(By.XPATH,
                                             "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                             "3]/h3/button/span/span")
        expand_element.click()

    # NoSuchElementException thrown if not present
    except NoSuchElementException:
        print("Element does not exist")

    try:
        supplier_name = driver.find_elements(By.XPATH,
                                             "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                             "3]/div/div/app-supplier-contact/div[1]/div[2]/span")
        supplier_names = [x.text for x in supplier_name]
        for y in range(len(supplier_names)):
            supplier_name_list.append(supplier_name[y].text)
        print("14. Supplier Name: " + str(supplier_name_list))

    except NoSuchElementException:
        print("Element does not exist")
        driver.close()

    service_name = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                  "1]/ecl-accordion/ecl-accordion-item[3]/div/div/app-supplier-contact/div[2]/div[2]/span")
    service_names = [x.text for x in service_name]
    for y in range(len(service_names)):
        service_name_list.append(service_name[y].text)
    print("15: Service name: " + str(service_name_list))

    phone_number = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                                  "1]/ecl-accordion/ecl-accordion-item[3]/div/div/app-supplier-contact/div[3]/div[2]/span")
    phone_numbers = [x.text for x in phone_number]
    for y in range(len(phone_numbers)):
        phone_number_list.append(phone_number[y].text)
    print("16: Phone: " + str(phone_number_list))

    email = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                           "3]/div/div/app-supplier-contact/div[4]/div[2]/a")
    emails = [x.text for x in email]
    for y in range(len(emails)):
        email_list.append(email[y].text)
    print("17: Email: " + str(email_list))

    website = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                             "1]/ecl-accordion/ecl-accordion-item[3]/div/div/app-supplier-contact/div[5]/div[2]/a")
    websites = [x.text for x in website]
    for y in range(len(websites)):
        website_list.append(website[y].text)
    print("18: Website: " + str(website_list))

    address = driver.find_elements(By.XPATH, "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div["
                                             "1]/ecl-accordion/ecl-accordion-item[3]/div/div/app-supplier-contact/div[6]/div[2]/span")
    addresses = [x.text for x in address]
    for y in range(len(addresses)):
        address_list.append(address[y].text)
    print("19: Address: " + str(address_list))

    try:
        expand_element = driver.find_element(By.XPATH,
                                             "//*[@id='ecl-main-content']/div/app-detail-page/ux-block-content/div/app-detail/div/div/div[1]/ecl-accordion/ecl-accordion-item["
                                             "3]/h3/button/span/span")
        expand_element.click()
        current_url = driver.current_url
        url_list.append(str(current_url))
        print("20: URL: " + str(url_list))

    # NoSuchElementException thrown if not present
    except NoSuchElementException:
        print("Element does not exist")

    driver.close()

    i += 1
else:
    print("")


#    print("Ending number is " + str(i))

def save_titles_to_excel():
    wb = Workbook()
    bold = xlwt.easyxf('font: bold 1')
    sheet1 = wb.add_sheet('Tyre Information')
    sheet1.write(0, 0, 'Commercial Name', bold)
    sheet1.write(0, 1, 'Tyre Size', bold)
    sheet1.write(0, 2, 'Tyre Class', bold)
    sheet1.write(0, 3, 'Load-Capacity Index', bold)
    sheet1.write(0, 4, 'Speed Category Symbol', bold)
    sheet1.write(0, 5, 'Fuel Efficiency Class', bold)
    sheet1.write(0, 6, 'Wet Grip Class', bold)
    sheet1.write(0, 7, 'Rolling Noise Class', bold)
    sheet1.write(0, 8, 'Rolling Noise Level', bold)
    sheet1.write(0, 9, 'Tyre for use in severe snow conditions', bold)
    sheet1.write(0, 10, 'Tyre for use in severe ice conditions', bold)
    sheet1.write(0, 11, 'Load Version', bold)
    sheet1.write(0, 12, 'Additional Information', bold)
    sheet1.write(0, 13, 'Supplier Name', bold)
    sheet1.write(0, 14, 'Service Name', bold)
    sheet1.write(0, 15, 'Phone', bold)
    sheet1.write(0, 16, 'Email', bold)
    sheet1.write(0, 17, 'Website', bold)
    sheet1.write(0, 18, 'Address', bold)
    sheet1.write(0, 19, 'URL', bold)
    wb.save('xlwt example.xls')

save_titles_to_excel()

data_tuples = list(zip(commercial_names_list[0:], tyre_size_designation_list[0:], tyre_class_list[0:], load_capacity_index_list[0:], speed_category_symbol_list[0:],
                       fuel_efficiency_class_list[0:], wet_grip_class_list[0:], rolling_noise_class_list[0:], rolling_noise_level_list[0:], tyre_in_snow_list[0:],
                       tyre_in_ice_list[0:], load_version_list[0:], additional_info_list[0:], supplier_name_list[0:], service_name_list[0:], phone_number_list[0:],
                       email_list[0:], website_list[0:], address_list[0:], url_list[0:]))
temp_df = pd.DataFrame(data_tuples,
                       columns=['Commercial Name', 'Tyre Size', 'Tyre Class', 'Load-Capacity Index', 'Speed Category Symbol', 'Fuel Efficiency Class', 'Wet Grip Class',
                                'Rolling Noise Class', 'Rolling Noise Level', 'Tyre for Use in Severe Snow Conditions', 'Tyre for Use in Severe Ice Conditions',
                                'Load Version', 'Additional Information', 'Supplier Name','Service Name', 'Phone', 'Email', 'Website', 'Address', 'URL'])
df = df.append(temp_df)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(df)

def save_dataframe_to_excel():
    # create excel writer object
    writer = pd.ExcelWriter('EU Tyre Information.xlsx')
    df.to_excel(writer)
    # save the excel
    writer.save()
    print('DataFrame is written successfully to Excel File.')

save_dataframe_to_excel()


import pandas as pd
import chrome_driver as cd
import get_data_attributes as gt

#Define the parameters:
receipt_prefix = 'YSC'
receipt_series = '1990274'
#receipt_number = 'YSC1990274536'
receipt_counter = 536
button_name = 'initCaseSearch'
element_id = 'receipt_number'
url = 'https://egov.uscis.gov/casestatus/landing.do'
path = '/anaconda3/pkgs/chromedriver-binary-2.38-0/bin/chromedriver-binary'
div_class_to_capture = "rows text-center"

#Initiate Variables
df = []

for indx in range(1, 2):
    receipt_counter = receipt_counter + 1
    receipt_number = receipt_prefix + receipt_series + str(receipt_counter)
    print('looking for ' + receipt_number)


    #Search for the receipt and reterive the html result
    r1 = cd.ChromeDriver(path, url, element_id, receipt_number, button_name)
    html = r1.execute_chrome_driver()

    #get relevant data from the html
    r2 = gt.GetData(html, div_class_to_capture)
    status, status_text, date = r2.extract_data()

    #Store the data in a list
    df.append([receipt_number,status,date,status_text])

print(*df, sep="\n")

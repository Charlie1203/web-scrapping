import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Create a new Chrome webdriver instance
driver = webdriver.Chrome()

# Navigate to the login page
driver.get('http://gruposm.dyndns.org:3306/SST/Account/Login.aspx')

# Find the input element with the name "txtUsuario" and set its value to "Usuario"
usuario_input = driver.find_element(By.NAME, 'txtUsuario')
usuario_input.send_keys('gsmadmin')

# Send TAB key to shift focus to the password field
usuario_input.send_keys(Keys.TAB)

# Find the active element (which should be the password field) and enter the text "Contraseña"
password_input = driver.switch_to.active_element
password_input.send_keys('202120')

# Send Enter key to submit the login form
password_input.send_keys(Keys.ENTER)

# Wait for 2 seconds for the page to load
time.sleep(2)

# Navigate to the target page
driver.get('http://gruposm.dyndns.org:3306/SST/Custodia/CustodiaCargaFinal.aspx')

# Wait for 10 seconds for the page to load
time.sleep(2)

# Find the table element with ID 'ctl00_MainPane_Content_gPendientes_DXMainTable'
table = driver.find_element(By.ID, 'ctl00_MainPane_Content_gPendientes_DXMainTable')

# Get the table HTML and create a new Excel workbook
table_html = table.get_attribute('outerHTML')
workbook = openpyxl.Workbook()

# Create a new worksheet and populate it with the table data
worksheet = workbook.active
worksheet.title = 'Table Data'

# Initialize row counter
row_count = 0

for row_idx, row in enumerate(table.find_elements(By.XPATH, './/tr[@class="dxgvDataRow_MetropolisBlueSST"]')):
    for col_idx, cell in enumerate(row.find_elements(By.XPATH, './/td')):
        value = cell.text.strip()
        worksheet.cell(row=row_idx+1, column=col_idx+1, value=value)
    # Increment row counter and print progress to terminal
    row_count += 1
    print(f'Cargando {row_count} fila en el excel')

# Save the workbook to an Excel file
workbook.save('table_data.xlsx')

# Close the browser window
driver.quit()

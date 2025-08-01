from selenium import webdriver
import os
import sys
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
from selenium.webdriver.common.action_chains import ActionChains
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QMessageBox

class uat_auto():
    def pass_inputs(self):
        array=0
        # Create the application
        app = QApplication(sys.argv)
        # Create a temporary widget (needed for dialogs)
        widget = QWidget()
        widget.setWindowTitle("Input Example")
        # Show input dialog
        login_id, ok = QInputDialog.getText(widget, 'Input Dialog', "Enter Login_ID: ")
        # Show message box based on input
        if ok and login_id:
            pass
        else:
            QMessageBox.warning(widget, 'No Input', 'You didn\'t enter Login_ID.')

        input_count, ok = QInputDialog.getText(widget, 'Input Dialog', "Enter Test count: ")
        # Show message box based on input
        if ok and input_count:
            pass
        else:
            QMessageBox.warning(widget, 'No Input', 'You didn\'t enter Test count.')

        offer_num, ok = QInputDialog.getText(widget, 'Input Dialog', "Enter Offer Number: ")
        # Show message box based on input
        if ok and offer_num:
            pass
        else:
            QMessageBox.warning(widget, 'No Input', 'You didn\'t enter Offer Number.')
        
        kv_index, ok = QInputDialog.getText(widget, 'Input Dialog', "Enter KV index: ")
        # Show message box based on input
        if ok and kv_index:
            array=int(kv_index)-1
        else:
            QMessageBox.warning(widget, 'No Input', 'You didn\'t enter Offer Number.')
        
        
        char=''.join([charr for charr in offer_num if charr.isalpha()])
        id=int(''.join([idd for idd in offer_num if idd.isnumeric()]))
        count=int(input_count)
        # msv_iterate=int(count/5)
        # run_count=0
        #array=0
       
        def resource_path(relative_path):
            try:
                base_path = sys._MEIPASS  # PyInstaller stores temp files here
            except AttributeError:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        # Path to the EdgeDriver executable
        driver_path = resource_path("msedgedriver.exe")

        # Set up the Edge WebDriver
        service = Service(executable_path=driver_path)
        options = webdriver.EdgeOptions()
        options.add_argument("--start-maximized")
        driver = webdriver.Edge(service=service,options=options)
        wait = WebDriverWait(driver, 60)
        driver.get('https://cplm-qa-hitachienergy.cloud.thingworx.com/Thingworx/Runtime/index.html?mashup=HE.SPACE.BDS.EConfigListCTO_MU#master=HE.SPACE.BDS.Master_MU&mashup=HE.SPACE.BDS.EConfigListCTO_MU&__applyThemeName=PTC%20Convergence%20Theme')
        login = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierInput"]')))
        login.send_keys(login_id)
        #submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="signOnButton"]')))
        #submit_button.click()
        time.sleep(10)



        run=1
        while run<=count:

            top_level_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'root_pagemashupcontainer-2_ptcsbutton-24-bounding-box')))
            time.sleep(3)
            new_btn = top_level_container.find_element(By.CSS_SELECTOR, 'ptcs-button')
            new_btn.click()
            time.sleep(1.25)
            toplvl_containers =['root_pagemashupcontainer-2_ptcstextfield-37-bounding-box','root_pagemashupcontainer-2_ptcstextfield-38-bounding-box','root_pagemashupcontainer-2_ptcstextfield-279-bounding-box']
            for i in range (0,len(toplvl_containers)):
                # Wait for the top-level container element to be present
                top_level_container = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, toplvl_containers[i])))
                # Locate the shadow host element within the top-level container
                shadow_host = top_level_container.find_element(By.CSS_SELECTOR, 'ptcs-textfield')
                # Execute JavaScript to access the shadow DOM
                shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
                # Locate the input element inside the shadow DOM
                input_element = shadow_root.find_element(By.CSS_SELECTOR, 'input#input')
                # Scroll the element into view
                driver.execute_script('arguments[0].scrollIntoView(true);', input_element)
                # Use JavaScript to set the value directly
                driver.execute_script(f'arguments[0].value = "Job_ID{char}{id}";', input_element)
                # Manually trigger the input event
                driver.execute_script('arguments[0].dispatchEvent(new Event("input", { bubbles: true }));', input_element)
            id+=1
            toplvl_ddcontainers =['root_pagemashupcontainer-2_ptcsdropdown-68-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-69-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-70-bounding-box',
                                'root_pagemashupcontainer-2_ptcsdropdown-71-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-72-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-73-bounding-box',
                                'root_pagemashupcontainer-2_ptcsdropdown-112-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-113-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-114-bounding-box',
                                'root_pagemashupcontainer-2_ptcsdropdown-115-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-150-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-151-bounding-box','root_pagemashupcontainer-2_ptcsdropdown-152-bounding-box']
            for i in range (0,len(toplvl_ddcontainers)):
                toplvl_ddcontainer = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, toplvl_ddcontainers[i])))
                params = toplvl_ddcontainer.find_element(By.CSS_SELECTOR, 'ptcs-dropdown')
                #time.sleep(1)
                if i==0:
                    time.sleep(4)
                    params.click()
                elif i==9:
                    time.sleep(3)
                    params.click()
                else:
                    time.sleep(0.8)
                    params.click()
                
                time.sleep(1.5)
                iframe = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
                
                ext_id=toplvl_ddcontainers[i].replace('bounding-box','external-wc')

                shadow_host= WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, ext_id)))
                shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)

                # Locate all list items within the shadow root and select random
                list_items = shadow_root.find_elements(By.CSS_SELECTOR, "ptcs-list-item")

                
                if toplvl_ddcontainers[i]=='root_pagemashupcontainer-2_ptcsdropdown-68-bounding-box':
                    item=list_items[array]
                    actions = ActionChains(driver)
                    actions.move_to_element(item).click().perform()

                    # if run_count<msv_iterate:
                    #     item=list_items[array]
                    #     actions = ActionChains(driver)
                    #     actions.move_to_element(item).click().perform()
                    #     run_count+=1
                    
                    # else:
                    #     run_count=0
                    #     array+=1
                    #     item=list_items[array]
                    #     actions = ActionChains(driver)
                    #     actions.move_to_element(item).click().perform()
                    #     run_count+=1
                else:
                    random_item = random.choice(list_items)
                    actions = ActionChains(driver)
                    actions.move_to_element(random_item).click().perform()



            # Submit button for each while loop
            top_level_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'root_pagemashupcontainer-2_ptcsbutton-18-bounding-box')))
            time.sleep(0.5)
            submit_btn = top_level_container.find_element(By.CSS_SELECTOR, 'ptcs-button')
            submit_btn.click()
            time.sleep(6)
            #while condition iterate
            run+=1

        time.sleep(5)
        driver.quit()
        sys.exit()
    # Exit the application
        

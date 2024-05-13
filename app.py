from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def automate_process():
    
    #CHANGE THIS DATA before starting application
    msg = 'Esta é uma mensagem automatizada com Selenium.'
    contacts = ["Meu Numero", "Grupo 01", "Grupo 02 ", "Grupo 03", "Grupo 04", "Grupo 05"]
    
    #Configuring Browser 
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    driver.get("https://web.whatsapp.com/")
    
    sleep(30)
    
    inc = 0
    for name in contacts:  
        #clicking in search button
        driver.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
        sleep(1)        
        #writing name contact or group
        driver.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(name)
        sleep(1)
        #Pressing ENTER to chosen name
        driver.find_element('xpath','//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        sleep(1)
        #writing message
        driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(msg)
        sleep(1)
        #Pressing Enter to send message
        driver.find_element('xpath','//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p').send_keys(Keys.ENTER)
        sleep(1)
        
        inc+=1
        
        #If number of messages is greater than 5, wait 10 seconds to next interation
        if inc == 5:
            inc = 0
            sleep(10)
    
        
if __name__ == "__main__": 
    try:  
        automate_process()            
    except Exception as error:
        print(f"[ERROR] -> {error=}")
    
    print("Done!")

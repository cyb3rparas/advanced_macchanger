#! /usr/bin/python
import subprocess
import time
from termcolor import colored
new_mac=[]
t=[]
def change_mac(interface,new_mac):
	subprocess.call(["ifconfig",interface,"down"])
	subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
	subprocess.call(["ifconfig",interface,"up"])

def main():
	print(colored("                        WELCOME TO ADVANCED MAC CHANGER!",'cyan',attrs=['bold']))
	print(colored("This script helps you to change your MAC address multiple times automatically with your chosen time limits and at last it also restores back your original MAC address!!",'cyan',attrs=['bold']))
	print(colored("                         *****COd3d by 0daymaroon*****",'cyan',attrs=['bold']))
	print()
	print()
	interface=str(input("Enter the Target Interface:"))
	aa=subprocess.run(["cat /sys/class/net/"+interface+"/address"], shell=True, stdout=subprocess.PIPE).stdout
	n=int(input("Enter no. of times you want to change MAC address="))
	for k in range(n):
		while(1==1):
			print()
			checkmac=input(colored("Enter MAC Address number "+str(k+1)+" =",'yellow'))
			before=subprocess.run(["ifconfig "+interface+" | grep ether"], shell=True, stdout=subprocess.PIPE).stdout
			change_mac(interface,checkmac)
			after=subprocess.run(["ifconfig "+interface+" | grep ether"], shell=True, stdout=subprocess.PIPE).stdout
			if before==after :
				print(colored("Error!!This address can't be used! Try another.. ",'red'))
			else:
				print(colored("Address accepted!",'green'))
				break;
		new_mac.append(checkmac)
		ti=int(input(colored("Enter number of seconds you want to keep this address for=",'yellow')))
		t.append(ti)
	print()
	print("All done! Script is running....")
	for k in range(n):
		change_mac(interface,new_mac[k])
		time.sleep(t[k])
	change_mac(interface,aa)
	print()
	print(colored("Script has been ended successfully and your original MAC Address has been restored!!",'green'))
	print(colored("                          Thanks for using :)",'green',attrs=['bold']))
main()

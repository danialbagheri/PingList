#!/usr/bin/python3
import os
import sys
import platform    # For getting the operating system name
import subprocess  # For executing a shell command
args = sys.argv

def ping(host):
    """
    Returns True if host (str) responds to a ping request.
    Remember that a host may not respond to a ping (ICMP) request even if the host name is valid.
    """

    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    # command = ['ping', param, '1', host]
    # FNULL = open(os.devnull, 'w')
    pinging = os.system(f"ping -c 3 {host}")
    if pinging == 0:
        return True
    else:
        return False


	# os.system("""
	# 	osascript -e 'display notification "{}" with title "{}"'
	# 	""".format(message, title))
def notify(message):
	title = "IP is Down"
	plt = platform.system()
	if plt=='Darwin':
		os.system("""
			osascript -e 'display notification "{}" with title "{}"'
			""".format(message, title))
	if plt=='Linux':
		os.system("""
			notify-send "{}" "{}"'
			""".format(message, title))	
	else:
		return False


if len(args) == 2:

	if os.path.exists(args[1]):
		switch_ips = open(args[1]).read().splitlines()
		for each in switch_ips:
			testip = ping(each)
			if testip == False:
				sys.stdout.write(f"{each}, is dead.")
				try:
					notify(f"{each} IP is dead. Please check!\n")
				except:
					pass
			else:
				sys.stdout.write(f"{each}, IS ALIVE!!!\n")
						

	else:
		sys.stdout.write('File, ', os.path.realpath(args[1]), 'does not exist.  Please try again.')

else:
	sys.stdout.write('ERROR: Invalid syntax\n'\
	'Example: \"sudo python pinglist.py file.txt\"')
	sys.exit(1)






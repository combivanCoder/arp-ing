#!/usr/bin/env python3
# pylint: disable=I0011
# pylint: disable=C0103
# pylint: disable=C0325
# pylint: disable=C0413
"""Documentation goes here ;)"""

import subprocess
from subprocess import PIPE
import os

def os_type():
    '''
    This function works, checking what OS you are running in order to use if or ipconfig later.
    :return: boolean - is_Windows
    '''
    try:
        if os.name == "Windows":
            is_Windows = True
        else:
            is_Windows = False
    except Exception as err:
        print("Error in tracking os type: ", err)
    return is_Windows

def whoami():
    '''
    Okay, this works and gets the return screen output. But why this and not others?
    :return:
    '''
    print("whoami: ")
    try:
        windows_type = os_type()
        if windows_type:
            config = subprocess.call("ifconfig")
        else:
            config = subprocess.call("ipconfig")
    except Exception as err:
        print("There is a problem still: ", err)
    print("Config: ", config)
    return


def ping2():
    '''
    This failed due to priv requirement for -c switch, so its removed.
    :return: str, however the process doesn't wait for the execution to complete.
    '''
    print("Ping2 - os.system: ")
    os.system("ping 192.168.0.1 > tmp")
    print(open('tmp', 'r').read())
    os.remove('tmp')
    return


def ping(address):
    print("subprocess.call simple: ")
    subprocess.call("ping", "-c 4 " + address)
    print("something ")
    return


def run_command(cmd):
    """given shell command, returns communication tuple of stdout and stderr"""
    print("Popen command: ")
    return subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE).communicate()


def nmap_return(address):
    print("This has been passed for nmap: ", address)
    switches = "-Pn " + str(address)
    s = subprocess.call(switches, stdout=PIPE, shell=True, timeout=None) # stdin=None, stdout=None, stderr=None,
    for line in s.stdout:
        print("finally: ", line)
    output = subprocess.run('nmap -Pn 192.168.0.1', capture_output=True, text=True)
    print("Found: ", output.stdout.readline)
    return

def another():
    new_command = "{}{}".format("ping -c 2 192.168.0.1", self.tld)
    self.logDebug("Trying intitial who is with command " + new_command)
    self.process = subprocess.Popen(newCommand.split(), stdout=subprocess.PIPE)
    self.rawResponse, self.error = self.process.communicate()
    return


def another():
    print("process.communicate: ")
    new_command = "{}{}".format("ping -c 2 192.168.0.1", self.tld)
    self.logDebug("Trying initial who is with command " + new_command)
    self.process = subprocess.Popen(newCommand.split(), stdout=subprocess.PIPE)
    self.rawResponse, self.error = self.process.communicate()
    return


def main_function():
    print("Staring with")
    whoami()
    ping2()
    another()
    run_command("ping -c 2 192.168.0.1")
    addresses = ["192.168.0.1/24", "192.168.1.0/24"]
    for a in addresses:
        print("A :", a)
        nmap_return(a)
        ping(a)
    print("Here in main.")
    return

# Changed: evaluate the content of variable __name__, instead of the string "__name__"
if __name__ == "__main__":
    print("Finding stuff...")
    main_function()

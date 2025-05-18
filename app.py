import os

def get_password():
    password = "123456"  # hardcoded password
    return password

def run_command(cmd):
    os.system(cmd)  # command injection riski

run_command("echo Hello World")

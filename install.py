#! /usr/bin/env python3
import subprocess

def install():
    command = ['sudo', 'cp', './he', '/usr/local/bin/he']
    subprocess.call(command)
    command = ['he', 'settings']
    subprocess.call(command)


if __name__ == "__main__":
    install()

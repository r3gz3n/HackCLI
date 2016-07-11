#! /usr/bin/env python3
from os.path import expanduser
from subprocess import call

HOME = expanduser("~")

def install():
    command = ['sudo', 'cp', './he', '/usr/local/bin/he']
    call(command)
    command = ['touch', HOME + '/.he_conf']
    call(command)
    setting = 'EDITOR:None\nBROWSER:None\nFILEPATH:None\nTEMPLATE:None\nLANG:None\nCLIENT_ID:None\nCLIENT_SECRET:None\n'
    with open(HOME + '/.he_conf', 'w') as conf:
        conf.write(setting)
    command = ['he', 'settings']
    call(command)


if __name__ == "__main__":
    install()

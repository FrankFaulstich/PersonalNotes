import sys

def installPyQt6():
    try:
        from PyQt6 import QtWidgets
    except:
        print('PyQt6 library is not installed in your Python env.')
        instPyQt6 = input('Do you want to install it (y/n)? ')
        instPyQt6 = instPyQt6.lower()
        if instPyQt6 == 'y':
            import subprocess
            try:
                subprocess.call('python -m pip install PyQt6 --user')
            except:
                try:
                    subprocess.call('python3 -m pip3 install PyQt6 --user')
                except:
                    print('WARNING: Installation of PyQt6 library failed!')
                    print('Please use command "pip install PyQt6 --user" in your Command Prompt.')
                    input('Press Enter to exit...')
                    sys.exit()
        else:
            input('Press Enter to exit...')
            sys.exit()
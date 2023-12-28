import sys

# TODO: #4 Umstellung der Installation auf PyQt6
def installPyQt5():
    try:
        from PyQt5 import QtWidgets
    except:
        print('PyQt5 library is not installed in your Python env.')
        instPyQt5 = input('Do you want to install it (y/n)? ')
        instPyQt5 = instPyQt5.lower()
        if instPyQt5 == 'y':
            import subprocess
            try:
                subprocess.call('python -m pip install PyQt5 --user')
            except:
                try:
                    subprocess.call('python3 -m pip3 install PyQt5 --user')
                except:
                    print('WARNING: Installation of PyQt5 library failed!')
                    print('Please use command "pip install PyQt5 --user" in your Command Prompt.')
                    input('Press Enter to exit...')
                    sys.exit()
        else:
            input('Press Enter to exit...')
            sys.exit()
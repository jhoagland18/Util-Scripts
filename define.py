# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import webbrowser, sys, pyperclip

def main():
    if len(sys.argv) > 1:
        # Get address from command line.
        query = '+'.join(sys.argv[1:])
    else:
        # Get address from clipboard.
        query = pyperclip.paste()

    webbrowser.open('https://www.merriam-webster.com/dictionary/' + query)

if __name__ == '__main__':
    main()

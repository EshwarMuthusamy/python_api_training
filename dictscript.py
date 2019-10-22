#!/usr/bin/python3

def main():
    hostipdict = { 'h1': '10.2.2.1', 'h2': '21.23.1.1', 'h3': '192.168.21.1' }
    print(hostipdict)
    print(hostipdict['h2'])
    print(hostipdict.get('122'))
if __name__ == '__main__':
    main()

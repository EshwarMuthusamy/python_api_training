#!/usr/bin/python3
def main():
    mylist = []
    mylist.append('192.168.23.3')
    print(mylist)
    mylist.append('10.0.0.1')
    print(mylist)
    mylist2 = ['127.16.23.1', "10.32.21.1"]
    print(mylist2)
    mylist.extend(mylist2)
    print(mylist)
    print(mylist[-3])
    ml3 = [1,2,3]
    print(ml3)
if __name__ == '__main__':
    main()

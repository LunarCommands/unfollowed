#! /usr/bin/python3

import json
import update_main as upd


def main():
    followers = []
    with open('phil_elementz_followers.json', 'r') as f:
        data = json.load(f)
        f.close()
        
    for person in list(data['followers']):
        followers.append(person['username'])

    with open('followers_main.json', 'r') as g:
        followers_main_list = json.load(g)
        
    for nick in followers_main_list:
        if nick not in followers:
            print(nick)
            
    answer = input('Czy stara lista ma byc zastapiona nowa? (y/n)\n')
    if answer == 'y':
        upd.main()
        print()
        print('Lista zostala pomyslnie nadpisana.')
        print('Do widzenia.')

    else:
        print()
        print('Lista nie zostala nadpisana.')
        print('Do widzenia.')


if __name__ == '__main__':
    main()

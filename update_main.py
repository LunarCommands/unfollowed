#! /usr/bin/python3
import json


def main():
    followers = []
    with open('phil_elementz_followers.json', 'r') as f:
        data = json.load(f)
        
    for person in data['followers']:
        followers.append(person['username'])
        
    with open('followers_main.json', 'w') as g:
        g.write(json.dumps(followers))
    
if __name__ == '__main__':
    main()

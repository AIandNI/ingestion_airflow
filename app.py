import sys
from config import DB_DETAILS
def main():
    #'''Program takes at least one argument'''
    env = sys.argv[1]
    print(env)
    dbdetails = DB_DETAILS[env]
    print(dbdetails)


if __name__ == '__main__':
    main()

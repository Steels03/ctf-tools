import os
import sys
import time


def search(directory):
    wordlist = ['api', 'key', 'username', 'user', 'uname', 'pw', 'password', 'pass', 'email', 'mail', 'credentials', 'credential', 'login', 'token', 'secret', 'cookie']
    wordlist2 = [':"', '="', ' :"', ' ="', ': "', '= "', ' : "', ' = "', " :'", "='", " :'", " ='", " : '", "= '", " : '", " = '"]
    exclude = ['.git'] # Add extensions you don't want to crawl
    CRED = '\033[91m' # Color red
    CGREEN = '\033[32m' # Color green
    CBLUE = '\033[34m' # Color green
    CEND = '\033[0m' # Color reset
    try:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in exclude]
            for filename in files:
                fn = (os.path.join(root, filename))
                f = open(fn, 'r', errors='ignore')
                index = 0
                for l in f:
                    index += 1
                    for s in wordlist:
                        for s2 in wordlist2:
                            if s+s2 in l:
                                if (l.split(s+s2, 1)[1]).split(' ', 1)[0] != '':
                                    res = CRED +(l.split(s+s2, 1)[1]).split(' ', 1)[0] + CEND
                                else:
                                    res = CRED + (l.split(s+s2, 1)[1]).split(' ', 2)[1] + CEND
                                if 4<= len(res) <= 40 and s not in res:
                                    t = CRED + (s+s2) + CEND
                                    li = CGREEN + str(index) + CEND
                                    fn = CBLUE + fn + CEND
                                    print('=> {0}:{1} : {2}{3}'.format(fn.replace('../', ''), li, t, res.replace('\n', '')))
                f.close()
    except OSError as e:
        print('An error has occured\n{}'.format(e))


def main():
    global_time = time.time()
    if len(sys.argv)<2:
        print("Basic usage :\npython3 secret-crawler.py <directory>")
    else:
        directory = sys.argv[1]
        search(directory)
        print('\n>>> Total time : {} sec.\n'.format(time.time() - global_time))


if __name__ == '__main__':
    main()
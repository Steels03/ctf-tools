import requests


def recon(url):
    files = ["robots.txt", "feed", "readme.html", "xmlrpc.php", ".htaccess", "wpeprivate/config.json", "license.txt", "readme.html"]
    directories = ["wp-content/uploads/", "wp-content/plugins/", "wp-includes/"]
    results_f = []
    results_d = []

    print("")
    print("")
    print("Starting file testing.")
    print("")
    for i in files:
        r_files = requests.get(url + "/" + i)
        if r_files.status_code == 200:
            print(url + "/" + i + " : found.")
            results_f.append(i)
        elif r_files.status_code == 503:
            print(url + "/" + i + " : forbidden.")
        elif r_files.status_code == 404:
            print(url + "/" + i + " : not found.")
    print("")
    print("")
    print("All files checked, starting directory checking.")
    print("")

    for i in directories:
        r_directories = requests.get(url + "/" + i)
        if r_directories.status_code == 200:
            print(url + "/" + i + " : found.")
            results_d.append(i)
        elif r_directories.status_code == 503:
            print(url + "/" + i + " : forbidden.")
        elif r_directories.status_code == 404:
            print(url + "/" + i + " : not found.")
    print("")
    print("")
    print("All files and directories checked.")
    print("")

    print("These files were found : ")
    for i in results_f :
        print(i)

    print("")
    print("These directories were found : ")
    for i in results_d :
        print(i)


def check_url(url):
    while "http" not in url:
        print("You need to add either http or https to the URL.")
        url = input("Enter the Wordpress URL to scan : ")
    recon(url)


def main():
    url = input("Enter the Wordpress URL to scan : ")
    check_url(url)


if __name__ == "__main__":
    main()

import requests
from colorama import Fore, Back, Style

wp_pages = ["/wp-login.php", "/xmlrpc.php", "/robots.txt"]


def process_urls():
    with open('urls.txt', 'r', encoding="utf-8") as urls:
        return [line.strip() for line in urls if line.strip()]



def check_wp_defalt_login():
    urls = process_urls()
    login_page = wp_pages[0]

    for base_url in urls:
        full_url = base_url + login_page
        web_request = requests.get(full_url)
        web_request.status_code

    if web_request.status_code == 200:
        print (Fore.RED + 'Default admin login exists! ' + full_url)
        print(Style.RESET_ALL)
    else:
        return False

def check_for_xmlrpc():
    urls = process_urls()
    login_page = wp_pages[1]

    for base_url in urls:
        full_url = base_url + login_page
        web_request = requests.get(full_url)
        response = web_request.text

    if web_request.text == "XML-RPC server accepts POST requests only.":
        print (Fore.RED + 'XMLRPC is enabled! ' + full_url + '\n')
        print(Style.RESET_ALL)
    else:
        print (Fore.GREEN + 'XMLRPC not enabled!' + '\n')

def check_and_render_robots():
    urls = process_urls()
    login_page = wp_pages[2]

    for base_url in urls:
        full_url = base_url + login_page
        web_request = requests.get(full_url)
        response = web_request.text
        print ("Printing contents of robots.txt... \n" + '\n' + response)



check_wp_defalt_login()
check_for_xmlrpc()
check_and_render_robots()

import requests, sys, getopt
from colorama import Fore, Back, Style

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "u:p"
long_options = ["url=", "proxy"]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except:
    sys.exit(2)

if len(sys.argv) <= 1:
    print('Usage: python3 get_request.py (-u|--url) [URL] (-p|--proxy)')
    exit(1)

use_proxy = False

for current_argument, current_value in arguments:
    if current_argument in ("-u", "--url"):
        url = current_value
    if current_argument in ("-p", "--proxy"):
        use_proxy = True

requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}

def format_text(title, item):
    cr = '\r\n'
    section_break = cr + "*" * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
    return text

if use_proxy == True:
    r = requests.get(url, verify=False, proxies=proxies)
else:
    r = requests.get(url, verify=False)

print(format_text('Status Code: ', r.status_code))
print(format_text('Headers: ', r.headers))
print(format_text('Cookies: ', r.cookies))
print(format_text('Response Text: ', r.text))
import requests, sys, getopt
from colorama import Fore, Back, Style

full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = "u:"
long_options = ["url="]

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except:
    print("Please enter a URL with the -u or --url flag.  Exiting...")
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-u", "--url"):
        url = current_value

requests.packages.urllib3.\
disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def format_text(title, item):
    cr = '\r\n'
    section_break = cr + "*" * 20 + cr
    item = str(item)
    text = Style.BRIGHT + Fore.RED + title + Fore.RESET + section_break + item + section_break
    return text

r = requests.get(url, verify=False)
print(format_text('Status Code: ', r.status_code))
print(format_text('Headers: ', r.headers))
print(format_text('Cookies: ', r.cookies))
print(format_text('Response Text: ', r.text))
from __future__ import print_function
import argparse
import mechanicalsoup
import getpass

print("Login to DiggerNet")
username = input("Please enter your DiggerNet username (AKA your QWID): ")

passwd = getpass.getpass("Please enter your DiggerNet password: ")

browser = mechanicalsoup.StatefulBrowser(
    soup_config={'features': 'lxml'},
    raise_on_404=True,
    user_agent='MyBot/0.1: mysite.example.com/bot_info',
)
# Uncomment for a more verbose output:
# browser.set_verbose(2)

browser.open("https://mines-csm.symplicity.com/students/")
browser.select_form('form[name="loginform"]')
browser.get_current_form().print_summary()
browser["username"] = username
browser["password"] = passwd
resp = browser.submit_selected()

# Uncomment to launch a web browser on the current page:
browser.launch_browser()

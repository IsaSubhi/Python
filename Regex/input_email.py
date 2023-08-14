# read email from user

import re

'''
EMAIL REGEX EXPLANATION:

^ - beginning

the part before the @ (email's name):
(?:\w+\.)*  - aaa.bbb.ccc. etc
\w+         - ddd
                    --> aaa.bbb.ccc.ddd

@

the part after the @ (email's domain):
(?:\w+\.)+(?:com|co\.il|org.il)

$ - end
'''

# EMAIL_REGEX = r"(?:\w+\.)*\w+@(?:\w+\.)+\w+"

# better than the above since it won't accept a trailing text.
# EMAIL_REGEX = r"^(?:\w+\.)*\w+@(?:\w+\.)+\w+$"

# limited to certain domains
EMAIL_REGEX = r"^(?:\w+\.)*\w+@(?:\w+\.)+(?:com|co\.il|org.il)$"



while True:
    email = input("enter an email (com, co.il, org.il only):")
    match = re.match(EMAIL_REGEX, email)

    if match is None:
    # if match:
        print("that's not a valid email!")
    else:
        break

print("email {} registered.".format(email))

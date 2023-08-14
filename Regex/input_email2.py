# read email from user

import re

# better than the above since it won't accept a trailing text.
EMAIL_REGEX = r"^(?:[a-z0-9_]+\.)*[a-z0-9_]+@(?:[a-z0-9_]+\.)+[a-z0-9_]+$"




while True:
    email = input("enter an email:")
    match = re.match(EMAIL_REGEX, email, re.I)

    if match is None:
    # if match:
        print("that's not a valid email!")
    else:
        break

print("email {} registered.".format(email))

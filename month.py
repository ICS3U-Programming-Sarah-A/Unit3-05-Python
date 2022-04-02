#!/usr/bin/env python3

# Created by: Sarah
# Created on: Apr, 1st, 2022S
# This program asks the user to enter a number. It then tell them
# what month the number corresponds with.

# format number entered into a string
def find_month(month):
    months = {
      1: "{} represents January.".format(month),
      2: "{} represents February.".format(month),
      3: "{} represents March.".format(month),
      4: "{} represents April.".format(month),
      5: "{} represents May.".format(month),
      6: "{} represents June.".format(month),
      7: "{} represents July.".format(month),
      8: "{} represents August.".format(month),
      9: "{} represents September.".format(month),
      10: "{} represents October.".format(month),
      11: "{} represents November.".format(month),
      12: "{} represents December.".format(month),

    }
    # checks to see if user number entered is valid, handling an error case
    return months.get(month, "Error, {} does not represent a month".
                      format(month))


# calls the function
if __name__ == "__main__":
    user_month = int(input("Enter the number for a month"
                           " (i.e 2 is for February): "))
    print(find_month(user_month))

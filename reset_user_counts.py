#!/usr/bin/python3.6
# Description:
    # This script resets the text count for each user

import fileinput, sys

class ResetUserCounts:
    def reset_counts(self):
        for line in fileinput.input("user_phone_numbers.txt", inplace=1):
            count = int(line[-3:].strip())
            line = line.replace("| "+str(count),"| 0")
            sys.stdout.write(line)

    def execute(self):
        self.reset_counts()

if __name__ == "__main__":
    reset = ResetUserCounts()
    reset.execute()
import os
import sys
import re

## environment
testdir="./testcase"
total=0
success=0
fail=0

print("Start!")

# TEST_DIR exists
if os.path.isdir(testdir):
    pass
elif os.access(testdir, R_OK):
    pass
else:
    print("There is not %s directory" % (testdir))
    sys.exit(1)

# run each scripts
#test_cases = [f for f in os.listdir(testdir) if re.match(r'*.py', f)]
test_list = [f for f in os.listdir(testdir)]
print("test-cases", test_list)

if re.match(r'*.py', "a.py"): # BUGBUG: Why does this not work?
    print("match")


# terminate
print("Finish!: total-test:%d pass:%d fail:%d" % (total, success, fail))

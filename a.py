import os
import sys
import re

## environment
testdir="./testcase"
total_cases=0
success_cases=0
fail_cases=0

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
test_cases = [f for f in os.listdir(testdir) if re.match(r'(.*).py', f)]
#test_list = [f for f in os.listdir(testdir)]
print("test-cases", test_cases)
total_cases=len(test_cases)

# terminate
print("Result: total:%d pass:%d fail:%d" % (total_cases, success_cases, fail_cases))

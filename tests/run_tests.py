import os
import sys

DIRNAME, FILENAME = os.path.split(os.path.abspath(__file__))
UNIT_TEST_PATH = os.path.join(DIRNAME, "unit_tests")
sys.path.append(os.path.join(DIRNAME, "..", "..", "site-packages"))
import qi

def main():
	print "Running unit tests"
	print UNIT_TEST_PATH
	tests = [f for f in os.listdir(UNIT_TEST_PATH) if os.path.isfile(os.path.join(UNIT_TEST_PATH, f))]
	for test in tests:
		test = os.path.join(UNIT_TEST_PATH, test)
		print "Runnin test", test
		sys.path.append(os.path.join(DIRNAME, "..", "..", "site-package"))
		os.system(os.path.join(DIRNAME, "..", "middleware.py --ip localhost --port 65533 --script " + test))
	
if __name__ == "__main__":
	main()
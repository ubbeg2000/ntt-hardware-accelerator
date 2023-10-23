#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(
            prog='compare.py',
            description='Tests <testbench>.v using testcases in testcase.txt by comparing \
                expected results in expected.txt and actual results in actual.txt')

parser.add_argument('-t', '--testcase', required=True, default="testcase.txt")
parser.add_argument('-e', '--expected', required=True, default="expected.txt")
parser.add_argument('-a', '--actual', required=True, default="actual.txt")

args = parser.parse_args()

testcase_file = open(args.testcase, "r")
expected_file = open(args.expected, "r")
actual_file = open(args.actual, "r")

expected_results = list(expected_file.readlines())
actual_results = list(actual_file.readlines())

if len(expected_results) != len(actual_results):
    print("Number of expected results doesn't match number of actual results, aborting...")
    exit()

for (i, testcase) in enumerate(testcase_file.readlines()):
    t = testcase.strip()
    e = expected_results[i].strip()
    a = actual_results[i].strip()

    print(f"Testcase #{i+1}")
    print(f"Case     : {t}")
    print(f"Expected : {e}")
    print(f"Actual   : {a}")
    
    if e != a:
        print("NOK\n")
    else:
        print("OK\n")

testcase_file.close()
expected_file.close()
actual_file.close()


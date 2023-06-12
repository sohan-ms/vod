#!/bin/bash
pytest -s -v -m "sanity" --alluredir='Reports' --html=./Reports/report.html testCases --browser chrome
#pytest -s -v -m "sanity" --alluredir='../Reports/allureReports' --html=./Reports/report.html test_login.py --browser chrome
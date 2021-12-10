# IS218 Calculator Project

This branch sees the calculator go from a standalone Python program to a Flask web app.<br>
I also added an error message for zero division attempts using Flask's integrated message flashing.

[![Build Status](https://app.travis-ci.com/tmazyrko/IS218_calculator.svg?branch=calc-v5)](https://app.travis-ci.com/tmazyrko/IS218_calculator)

## Project Setup

To run tests, Lint, and Coverage report use this command:

pytest  --pylint --cov

_.pylintrc is the config for pylint_<br>
_.coveragerc is the config for coverage_<br>
_setup.py is a config file for pytest_

## Flash Message Demo

![flash-error-demo](img/flash_error_demo.gif)
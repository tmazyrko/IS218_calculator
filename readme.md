# IS218 Calculator Project

[![Build Status](https://app.travis-ci.com/tmazyrko/IS218_calculator.svg?branch=calc-v6)](https://app.travis-ci.com/tmazyrko/IS218_calculator)

This branch implements the DataTables plugin and adds a page to demo an interactive table filled with sample data.

## Project Setup

To run tests, Lint, and Coverage report use this command:

pytest  --pylint --cov

_.pylintrc is the config for pylint_<br>
_.coveragerc is the config for coverage_<br>
_setup.py is a config file for pytest_

## Flash Message Demo

![flash-error-demo](img/flash_error_demo.gif)<br>
_Demo of Flask flash message when attempting to divide by zero._

## DataTables Demo

![datatables-demo](img/datatables_demo.gif)<br>
Demo of interactive table filled with sample data.<br>
[https://datatables.net](https://datatables.net/)
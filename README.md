
# Toolshop website automation - UI and API tests - Atlantbh Quality Assurance Python Internship

## Project description

This is a repository in which I have placed both UI and API tests and necessary dependencies for running tests. Tests include smoke tests, both for UI and API workflow, and E2E tests for UI. which was made for [Toolshop website](https://practicesoftwaretesting.com/) as a part of Atlantbh Quality Assurance Python Internship. Tests are written in Playwright Python testing framework using Pytest.

## Prerequisites

Test and environment are set up and written on macOS operating system. To run the test you need to have installed following:

[Python3](https://www.python.org/downloads/) - choose the version according to your macOS

[Homebrew](https://brew.sh/) - package manager for macOS

[PyCharm](https://www.jetbrains.com/pycharm/download/?section=mac) - best IDE for running and writing tests in Python

[Postman](https://www.postman.com/downloads/) - recommended, download desktop app to run API requests effectively

## Installation

All the dependencies are placed in **requirements.txt** file. Simply copy in the terminal command below:

```bash
  pip install -r requirements.txt
```
For using Allure Reporter with Pytest in your test, you will need to install Allure Report command-line tool. Simply copy in the main terminal command below:

```bash
  brew install allure
```
## Project structure

Below is the project structure tree schema

```bash

├── pages
│   ├── cart_page.py
│   ├── home_page.py
│   ├── login_page.py
│   ├── page_manager.py
│   ├── payment_page.py
│   ├── product_page.py
│   └── register_page.py
├── tasks
│   ├── api_tasks.py
│   └── ui_tasks.py
├── test_data
│   └── common_data.py
├── tests
│   ├── conftest.py
│   ├── test_dummy.py
│   ├── test_e2e_different_payment_options.py
│   ├── test_e2e_filtering.py
│   ├── test_e2e_sorting.py
│   ├── test_smoke.py
│   └── test_smoke_api.py
└── utilities
    └── user_data.py
├── .gitignore
├── pytest.ini
├── README.md 
├── requirements.txt
```
## Running Tests

To run tests, use the following command

```bash
  python -m pytest tests/select_desired_test_file.py
```
If you want to run test with Allure Reporter, run the following command

```bash
  python -m pytest tests/select_desired_test_file.py --alluredir allure-results
```
To use test markers, created in **pytest.ini** file, simply run the command in terminal

```bash
  python -m pytest -m desired_test_marker  
```
To run tests in headless mode, and print test output to the console use the following command in terminal

```bash
  python -m pytest -o "addopts=" tests/select_desired_test_file.py  -s  
```
## Generating Reports

To generate reports, run the following command

```bash
  allure serve allure-results
```
## Author

[@mnizicqa](https://github.com/mnizicqa)

## License

[MIT](https://choosealicense.com/licenses/mit/)

# Week 3 Environment setup and test automation

This is a repository in which I have placed dummy test and necessary dependencies for running test, which was made for Week 3 Atlantbh Quality Assurance Python Internship. Test is written in Playwright Python testing framework using Pytest.


## Prerequisites

Test and environment are setup and written on macOS operating system. To run the test you need to have installed following:

[Python](https://www.python.org/downloads/) - choose the version according to your macOS

[Homebrew](https://brew.sh/) - package manager for macOS

## Installation

All of the dependencies are placed in **requirements.txt** file. Simply copy in the terminal command below:

```bash
  pip install -r requirements.txt
```

For using Allure Reporter with Pytest in your test, you will need to install Allure Report command-line tool. Simply copy in the main terminal command below:

```bash
  brew install allure
```
## Running Tests

To run test, run the following command

```bash
  pytest
```

If you want to run test with Allure Reporter, run the following command

```bash
  pytest --alluredir allure-results
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


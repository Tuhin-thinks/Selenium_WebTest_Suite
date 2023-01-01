## Webscraping Test Suite

Basic test suite for webscraping. This is a work in progress.

# Installation

1. Install [Python 3](https://www.python.org/downloads/).
2. Install [pip](https://pip.pypa.io/en/stable/installing/).
3. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/).
4. Clone this repository.
5. Create a virtual environment: `virtualenv venv`
6. Activate the virtual environment: `source venv/bin/activate`
7. Install the requirements: `pip install -r requirements.txt`
8. Run the main script: `python main.py`

## Usage

The main script can be used to design complex webscraping pipelines.  The script is designed to be run from console.

## Brief

This script is created to simplify the work of writing webscraping scripts, 
and to remove the repeated work of testing and writing steps for the successful/working tests.
Here, we can write a pipeline of steps, and the script will run the pipeline and test the steps.
Thus you have a test suite for your webscraping pipeline.

### Currently supported modules:

- [x] [selenium](https://selenium-python.readthedocs.io/)

### Future Plans:

- [ ] [scrapy](https://scrapy.org/)
- [ ] [requests](https://requests.readthedocs.io/en/master/)
- [ ] [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [ ] [lxml](https://lxml.de/)

## Contributing

Contributions are welcome.  Please see the [contributing guidelines](CONTRIBUTING.md).


## Features to be added

- [ ] Add support for more modules.
- [ ] Add complete documentation.
- [ ] Add support for complete testing to test suite algo file generation process.
- [ ] Add support for more complex pipelines.
- [ ] Write tests for the test suite.
- [ ] Add examples for the test suite. (**Important**)

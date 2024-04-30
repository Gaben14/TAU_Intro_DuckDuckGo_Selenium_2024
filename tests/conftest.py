"""
This module contains shared fixtures.
"""
import json
import pytest
import selenium.webdriver


@pytest.fixture
def config(scope='session'):
    # Read the config file:
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert that values inside the config.json are acceptable:
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    return config

@pytest.fixture
def browser(config):
    # Initialize the WebDriver instance - setUp
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        options = selenium.webdriver.ChromeOptions()
        options.add_argument('headless')
        b = selenium.webdriver.Chrome(options=options)
    else:
        raise Exception(f'Browser {config["browser"]} is not supported!')

    # Make its calls wait up to 10 seconds for elements to appear
    b.implicitly_wait(config["implicit_wait"])

    # Return the WebDriver instance for setup
    yield b

    # Quit the WebDrive instance for the cleanup - tearDown
    b.quit()

@pytest.fixture
def get_url():
    URL = "https://www.duckduckgo.com"
    return URL

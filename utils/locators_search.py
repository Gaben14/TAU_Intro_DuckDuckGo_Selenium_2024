# Locators for search
from selenium.webdriver.common.by import By
import random

class SearchPageLocators:
    # Class variables:
    SEARCH_INPUT = (By.ID, 'searchbox_input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Search"]')
    RESULT_TITLE = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')

    rnd_num = random.randint(0, 9)
    RANDOM_ARTICLE = (By.CSS_SELECTOR, f"#r1-{rnd_num} a[data-testid='result-title-a']")
    AUTOCOMPLETE_CONTAINER = (By.ID, 'listbox--11')
    AUTOCOMPLETE_SUGGESTIONS_LI = (By.CLASS_NAME, 'searchbox_suggestion__csrUQ')
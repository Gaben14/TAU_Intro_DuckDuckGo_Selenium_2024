# Locators for search
from selenium.webdriver.common.by import By
import random

class SearchPageLocators:
    # Class variables - UpperCase syntax:
    SEARCH_INPUT = (By.ID, 'searchbox_input')
    SEARCH_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Search"]')
    RESULT_TITLE = (By.CSS_SELECTOR, 'a[data-testid="result-title-a"]')

    rnd_num = random.randint(0, 9)
    RANDOM_ARTICLE = (By.CSS_SELECTOR, f"#r1-{rnd_num} a[data-testid='result-title-a']")
    AUTOCOMPLETE_CONTAINER = (By.ID, 'listbox--11')
    AUTOCOMPLETE_SUGGESTIONS_LI = (By.CLASS_NAME, 'searchbox_suggestion__csrUQ')

    # Settings Locators
    SETTINGS_LINK = (By.CLASS_NAME, 'dropdown--settings')

    DARK_MODE = (By.CSS_SELECTOR, 'div[data-theme-id="d"]')
    # The label will have the 'is checked' class, which will be needed for assertion
    DARK_MODE_LABEL = (By.CSS_SELECTOR, 'label[for="setting_kae_d"]')
    LIGHT_MODE_LABEL = (By.CSS_SELECTOR, 'label[for="setting_kav"]')

    FONT_SIZE_DROPDOWN = (By.ID, 'setting_ks')
    FONT_SIZE_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, '#setting_ks option')
    FONT_FAMILY_DROPDOWN = (By.ID, 'setting_kt')
    FONT_FAMILY_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, '#setting_kt option')

    APPEARANCE_RESET_LINK = (By.CLASS_NAME, 'js-settings-dropdown-reset-appearance')

    LANGUAGE_DROPDOWN = (By.ID, "setting_kad")
    LANGUAGE_HUNGARIAN = (By.CSS_SELECTOR, '#setting_kad > option[value="hu_HU"]')

    INFINITY_SCROLL_TOGGLE = (By.ID, "setting_kav")
    # The grandparent will have the 'is checked' class, which
    INFINITY_SCROLL_GPARENT = (By.CSS_SELECTOR, 'div.frm__field.fix:has(#setting_kav)')

    OPEN_LINKS_TOGGLE = (By.ID, "setting_kn")
    # Same logic as with Infinity_Scroll
    OPEN_LINKS_GPARENT = (By.CSS_SELECTOR, 'div.frm__field.fix:has(#setting_kn)')

    GENERAL_RESET_LINK = (By.CLASS_NAME, 'js-settings-dropdown-reset-general')



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

    # Regions Locators
    REGIONS_DROPDOWN_LINK = (By.CSS_SELECTOR, 'a[data-testid="region-filter-label"]')
    REGIONS_DROPDOWN_DIV_INACTIVE = (By.CLASS_NAME, 'has-inactive-region')
    REGIONS_DROPDOWN_DIV = (By.CSS_SELECTOR, 'div:has(+a[data-testid="region-filter-label"]')
    # REGIONS_FILTER_CLEAR_ALL_LINK = (By.CLASS_NAME, 'js-region-filter-clear')
    REGIONS_SPANS = (By.CSS_SELECTOR, 'span.fdosLIuRgrWo7SyeqSUb')
    REGIONS_FILTER_INPUT = (By.CSS_SELECTOR, 'input[placeholder="Search"]')
    REGIONS_FILTER_INPUT_RESULT = (By.CSS_SELECTOR, 'div.eRQYVfFPOfM6ezz54H_V  div.BDI1KtNF8HUPBZ4Cw_nK')

    # Settings Locators
    SETTINGS_LINK = (By.CLASS_NAME, 'dropdown--settings')

    DARK_MODE = (By.CSS_SELECTOR, 'div[data-theme-id="d"]')
    # The label will have the 'is checked' class, which will be needed for assertion
    DARK_MODE_LABEL = (By.CSS_SELECTOR, 'label[for="setting_kae_d"]')
    LIGHT_MODE_LABEL = (By.CSS_SELECTOR, 'label[for="setting_kae_-1"]')

    FONT_SIZE_DROPDOWN = (By.ID, 'setting_ks')
    FONT_SIZE_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, 'select#setting_ks option')
    FONT_FAMILY_DROPDOWN = (By.ID, 'setting_kt')
    FONT_FAMILY_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, 'select#setting_kt option')

    APPEARANCE_RESET_LINK = (By.CLASS_NAME, 'js-settings-dropdown-reset-appearance')

    LANGUAGE_DROPDOWN = (By.ID, "setting_kad")
    LANGUAGE_HUNGARIAN = (By.CSS_SELECTOR, '#setting_kad > option[value="hu_HU"]')

    # FYI: Using the labels for the toggle click, as the input was resulting in errors.
    INFINITY_SCROLL_TOGGLE = (By.CSS_SELECTOR, 'label[for="setting_kav"]')
    # The grandparent will have the 'is checked' class, which
    INFINITY_SCROLL_GPARENT_DIV = (By.CSS_SELECTOR, 'div.frm__field.fix:has(#setting_kav)')

    OPEN_LINKS_TOGGLE = (By.CSS_SELECTOR, 'label[for="setting_kn"]')
    # Same logic as with Infinity_Scroll
    OPEN_LINKS_GPARENT_DIV = (By.CSS_SELECTOR, 'div.frm__field.fix:has(#setting_kn)')

    GENERAL_RESET_LINK = (By.CLASS_NAME, 'js-settings-dropdown-reset-general')



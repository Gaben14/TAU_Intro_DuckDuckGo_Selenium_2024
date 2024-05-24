from selenium.webdriver.common.by import By
# <a> tags should have the LINK at the beginning?
# Locators:  all letters as uppercase
IMAGES_TAB = (By.CSS_SELECTOR, 'a[data-testid="tab-label-images"]')
IMAGE_SIZE_DROPDOWN = (By.CLASS_NAME, 'dropdown--size')
IMAGE_SIZE_MEDIUM = (By.CSS_SELECTOR, 'a[data-value="Medium"]')

DROPDOWN_LIST = (By.CSS_SELECTOR, 'div.modal--dropdown--color a.modal__list__link')

ALL_COLORS_DROPDOWN = (By.CLASS_NAME, 'dropdown--color')
BLACK_AND_WHITE = (By.CSS_SELECTOR, 'a[data-value="Monochrome"]')
ALL_TYPES = (By.CLASS_NAME, 'dropdown--type')
ANIMATED_GIF = (By.CSS_SELECTOR, 'a[data-value="gif"]')

ALL_LICENSES_DROPDOWN = (By.CLASS_NAME, 'dropdown--license')
FREE_TO_SHARE_AND_USE_LINK = (By.LINK_TEXT, 'Free to Share and Use')
IMG_RESULTS = (By.CSS_SELECTOR, 'div.tile.tile--img.has-detail')
IMG_RESULTS_2 = (By.CSS_SELECTOR, 'div[class="tile tile--img has-detail"]')

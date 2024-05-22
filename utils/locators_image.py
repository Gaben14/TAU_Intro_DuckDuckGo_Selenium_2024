from selenium.webdriver.common.by import By

# Temporarily moving the locators here
IMAGES_TAB = (By.CSS_SELECTOR, 'a[data-testid="tab-label-images"]')
IMAGE_SIZE_DROPDOWN = (By.CLASS_NAME, 'dropdown--size')
IMAGE_SIZE_MEDIUM = (By.CSS_SELECTOR, 'a[data-value="Medium"]')
ALL_COLORS_DROPDOWN = (By.CLASS_NAME, 'dropdown--color')
BLACK_AND_WHITE = (By.CSS_SELECTOR, 'a[data-value="Monochrome"]')
ALL_TYPES = (By.CLASS_NAME, 'dropdown--type')
ANIMATED_GIF = (By.CSS_SELECTOR, 'a[data-value="gif"]')

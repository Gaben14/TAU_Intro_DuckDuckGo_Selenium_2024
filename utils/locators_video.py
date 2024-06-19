from selenium.webdriver.common.by import By

class VideoPageLocators:
    VIDEO_TAB = (By.CSS_SELECTOR, 'a[data-testid="tab-label-videos"]')

    VIDEO_UPLOAD_DATE_DROPDOWN = (By.CLASS_NAME, 'dropdown--publishedAfter')
    VIDEO_UPLOAD_DATE_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, 'div.modal--dropdown--publishedAfter a')
    VIDEO_PAST_WEEK = (By.CSS_SELECTOR, 'a[data-value="w"]')
    VIDEO_UPLOAD_DATE_DROPDOWN_CHILD_LINK = (By.CSS_SELECTOR, 'div.dropdown--publishedAfter > a')

    VIDEO_RESOLUTION_DROPDOWN = (By.CLASS_NAME, 'dropdown--videoDefinition')
    VIDEO_RESOLUTION_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, 'div.modal--dropdown--videoDefinition a')
    VIDEO_STAND_DEF = (By.CSS_SELECTOR, 'a[data-value="standard"]')

    VIDEO_DURATION_DROPDOWN = (By.CLASS_NAME, 'dropdown--videoDuration ')
    VIDEO_DURATION_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, 'div.modal--dropdown--videoDuration a')
    VIDEO_DURATION_DROPDOWN_CHILD_LINK = (By.CSS_SELECTOR, 'div.dropdown--videoDuration > a')

    VIDEO_LICENSE_DROPDOWN = (By.CLASS_NAME, 'dropdown--videoLicense')
    VIDEO_LICENSE_DROPDOWN_OPTIONS = (By.CSS_SELECTOR, 'div.modal--dropdown--videoLicense a')
    YOUTUBE_STANDARD_LINK = (By.CSS_SELECTOR, 'a[data-value="youtube"]')
    VIDEO_LICENSE_DROPDOWN_CHILD_LINK = (By.CSS_SELECTOR, 'div.dropdown--videoLicense > a')

    VIDEO_SEARCH_RESULTS = (By.CLASS_NAME, 'tile--vid')
    VIDEO_SEARCH_RESULTS_LINK = (By.CSS_SELECTOR, 'div.tile--vid h6 a')

    YOUTUBE_ACCEPT_ALL_BTN = (By.XPATH, '//span[text() = "Accept all"]/ancestor::button')

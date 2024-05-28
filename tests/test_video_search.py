"""
These tests (test cases) cover DuckDuckGo video searches.
"""

from pages.video_search import DuckDuckGoVideoSearch
from utils.locators_video import VideoPageLocators


class TestVideoSearch:
    """
        Test Case:

        1. Open the browser and the https://duckduckgo.com page - Assert if the page has been opened successfully -
        HTTP 200
        2. Find the search-bar. Enter the phrase.
        3. Click on the 'Videos' tab - Assert if Videos tab is active
        4. Change the value inside "Any times" to "Past Week"
            - Assert if value has been changed to "Past Week"
        5. Change the value inside "Any resolution" to "Standard definition"
            - Assert if value has been changed to "Standard definition"
        6. Create a list which contains all the options from the "Any Duration" dropdown
            - Randomly change the value of the dropdown.
            - Assert if the value has changed.
        7. Change the license under the "Any License" dropdown to "YouTube standard"
            - Assert if the change has been successful
        8. Check if there is any search results after the change.
        9. Open one of the Results in a new tab, change to that tab.
            - Assert the title of the new tab contains the Phrase
            - Close the tab and navigate back to Video Page.
    """
    pass

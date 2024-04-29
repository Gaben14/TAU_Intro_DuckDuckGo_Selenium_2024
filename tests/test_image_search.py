"""
These tests (test cases) cover DuckDuckGo image searches.
"""

from pages.result import DuckDuckGoSearchResult
from pages.search import DuckDuckGoSearchPage

class TestImageSearch():
    """
    Test Case:

    1. Open the browser and the https://duckduckgo.com page - Assert if the page has been opened successfully - HTTP 200
    2. Find the search-bar, clear the input field. Enter the phrase.
    3. Click on the 'Images' tab - Assert if Images tab is active
    4. Change the value inside "All sizes" to "Medium" - Assert if value has been changed to Medium
    5. Create a list which contains all the color options from the "All colors" dropdown
        5.1 Change the value inside "All Colors" to a random value from the previously created list
        5.2 Assert if the color has been changed.
    6. Change the type under the "All types" dropdown to "Animated GIF"
        6.1 Assert if the change has been successful
    7. Change the "All Licenses" to "Free to Share and Use" - Assert if there are any images after this change.
    """

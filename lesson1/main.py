# Lesson 1: Setting up Python Playwright and Navigating to TikTok
# Objective: Create a script that launches a browser, navigates to TikTok, and prints the page title


import time
from playwright.sync_api import sync_playwright

def main():
    # Setup
    with sync_playwright() as p:
        # Launch the browser in non-headless mode
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigation
        page.goto("https://www.tiktok.com")
        time.sleep(4)

        # Output results
        print(f"Page title: {page.title()}")

        # Cleanup
        browser.close()

# Error handling
try:
    main()
except Exception as e:
    print(f"An error occurred: {e}")

# Ethical reminder
print("Remember to respect TikTok's terms of service and scraping guidelines.")

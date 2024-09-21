import requests
from bs4 import BeautifulSoup
import csv
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

# Function to scrape Wikipedia for a specific surname
def scrape_wikipedia(surname):
    base_url = f"https://en.wikipedia.org/wiki/{surname.replace(' ', '_')}"
    try:
        response = requests.get(base_url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the title and the first few paragraphs
        title = soup.find('h1', id="firstHeading").text
        paragraphs = soup.find_all('p', limit=5)
        if not paragraphs:
            raise Exception("No content found")
        content = ' '.join([p.text for p in paragraphs])

        return {"Title": title, "Source": "Wikipedia", "URL": base_url, "Content": content[:500]}  # Returning first 500 chars
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred while scraping Wikipedia: {http_err}")
    except Exception as e:
        print(f"Error scraping Wikipedia: {e}")
    return None

# Function to scrape FamilySearch for a specific surname and take a screenshot
def scrape_familysearch(surname):
    base_url = f"https://www.familysearch.org/en/surname?surname={surname}"
    try:
        # Start the Selenium WebDriver (Make sure ChromeDriver is installed)
        driver_path = "path_to_chromedriver"  # Update this path
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)

        driver.get(base_url)
        time.sleep(3)  # Give time for page to load

        # Take screenshot
        screenshot_path = f"screenshot_{surname}.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved as {screenshot_path}")

        # Extract page content
        content_div = driver.find_element(By.CSS_SELECTOR, 'div.surname-info-section')
        content = content_div.text if content_div else "No content available"

        driver.quit()

        return {"Title": f"FamilySearch results for {surname}", "Source": "FamilySearch", "URL": base_url, "Content": content[:500]}  # Returning first 500 chars
    except Exception as e:
        print(f"Error scraping FamilySearch: {e}")
    return None

# Function to save data to CSV
def save_to_csv(data, filename="surname_lineage_data.csv"):
    if data:
        keys = data[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as output_file:  # Use 'utf-8' encoding
            dict_writer = csv.DictWriter(output_file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
        print(f"Data saved to {filename}")
    else:
        print("No data to save.")

# Main function that scrapes Wikipedia and FamilySearch for a specific surname
def scrape_all_sources(surname):
    scraped_data = []

    # Scrape Wikipedia
    wiki_data = scrape_wikipedia(surname)
    if wiki_data:
        scraped_data.append(wiki_data)

    # Scrape FamilySearch
    fs_data = scrape_familysearch(surname)
    if fs_data:
        scraped_data.append(fs_data)

    return scraped_data

# Main execution
if __name__ == "__main__":
    surname = input("Enter a surname to trace lineage: ")  # Let user input surname
    results = scrape_all_sources(surname)
    
    if results:
        # Save the combined results to CSV
        save_to_csv(results)
    else:
        print("No results found.")

    # Wait before making the next request to avoid overloading servers
    time.sleep(1)

#Competitor Product Price Tracking and Reporting Automation using Playwright (Python) and saved output to CSV

from playwright.sync_api import sync_playwright
import pandas as pd

# Products
products = ["Shakespeare's Sonnets", 
            "Tipping the Velvet", 
            "Soumission", 
            "Sharp Objects",
            "Libertarianism for Beginners", 
            "The Requiem Red", 
            "Set Me Free",
            "Olio", 
            "It's Only the Himalayas", 
            "The Black Maria"]

# Store scraped data
product_data = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")

    for product in products:
        search_results = page.locator(f"text='{product}'")
        if search_results.count() > 0:
            search_results.nth(0).click()
            price_text = page.locator("div.product_main p.price_color").inner_text()
            price = float(price_text.replace("£", ""))
            product_data.append({"Product Name": product, "Price": price})
            page.goto("https://books.toscrape.com/")
        else:
            product_data.append({"Product Name": product, "Price": None})

    browser.close()

df = pd.DataFrame(product_data)
df = df.sort_values(by="Price", na_position='last')
df.to_csv(r"C:\Users\Neha\OneDrive\Desktop\ppyautogui\Retail_Price_Report.csv", index=False)
print("Report saved successfully!")
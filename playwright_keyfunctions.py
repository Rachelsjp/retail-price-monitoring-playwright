from playwright.async_api import async_playwright
import asyncio

async def playwright_functions():
    async with async_playwright() as p:  
        browser = await p.chromium.launch(headless=False)  
        page = await browser.new_page()  

        # Navigation
        await page.goto("https://www.google.com/")

        # Just to see the page before closing
        await asyncio.sleep(5)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(playwright_functions())
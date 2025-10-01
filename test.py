import asyncio
from playwright.async_api import async_playwright

async def test():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto("https://www.basketball-reference.com/leagues/NBA_2016_games.html")
        await page.wait_for_selector("#content.filter", state="attached", timeout=15000)
        html = await page.inner_html("#content.filter")
        print(html[:500])  # print first 500 characters
        await browser.close()

asyncio.run(test())

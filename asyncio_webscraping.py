import asyncio
import aiohttp # pip install aiohttp
import time

async def fetch(url, session):
    async with session.get(url) as response:
        print(f'Fetching {url}')
        return await response.text()

async def main():
    urls = [
        'https://www.zeit.de',
        'https://www.spiegel.de',
        'https://www.welt.de',
        'https://www.sz.de'
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(url, session) for url in urls]
        html_pages = await asyncio.gather(*tasks)
        for page in html_pages:
            print(f'Page length: {len(page)}')

# Zeit messen
start_time = time.time()
asyncio.run(main())
print(f"Execution time: {time.time() - start_time} seconds")

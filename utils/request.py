import aiohttp


async def get_img_url():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://random.dog/woof.json') as resp:
            if resp.status != 200:
                return
            dict_url = await resp.json()
            img_url = dict_url.get('url')
            return img_url

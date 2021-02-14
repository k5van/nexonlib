
MAPLEID=10100
import requests 
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import aiohttp
import asyncio

async def fetch(session, url):
    async with session.get(url) as response:
        if response.status != 200:
            return
            response.raise_for_status()
        content_type=response.headers["Content-Type"]
        if "image" in content_type:
            return url

async def fetch2(text,session, url):
    async with session.get(url) as response:
        if response.status != 200:
            return
            response.raise_for_status()
        if text in await response.text():
            return url

async def fetch_all(session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch(session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def fetch_all2(text,session, urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch2(text,session, url))
        tasks.append(task)
    results = await asyncio.gather(*tasks)
    return results

async def NXCheckpng(url, start, amount ):
    baseurl="https://nxcache.nexon.net/cms/2021/q1/"
    urls=[]
    for i in range(start, start+amount+1):
        urls.append(str(baseurl+str(i)+"/"+url+".png"))
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
    return htmls

async def updatecheck():
    baseurl="https://nxcache.nexon.net/cms/2021/q1/"
    urls=[]
    url="-update-preview-v220-designed-post_01"
    for k in range(210118,210123):
        for j in range(5305,5400):
            for i in range(1200, 1270):
                urls.append(str(baseurl+str(i)+"/"+"msw-"+str(j)+"-"+str(k)+url+".png"))
    print(urls[0])
    print(len(urls))
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
    return htmls


async def NXCheckjpg(url, start, amount ):
    baseurl="https://nxcache.nexon.net/cms/2021/q1/"
    urls=[]
    for i in range(start, start+amount+1):
        urls.append(str(baseurl+str(i)+"/"+url+".jpg"))
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all(session, urls)
    return htmls

async def NXCheckpng2(text, start, amount ):
    baseurl2="https://maplestory.nexon.net/news/"
    urls=[]
    for i in range(start, start+amount+1):
        urls.append(str(baseurl2+str(i)+"/"))
    async with aiohttp.ClientSession() as session:
        htmls = await fetch_all2(text,session, urls)
    return htmls





def underMaintenance(gameid=MAPLEID):
    
    headers = {
    '$Host': 'api.nexon.io',
    '$Connection': 'close',
    '$User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) NexonLauncher/3.3.4 Chrome/69.0.3497.128 Electron/4.2.5 Safari/537.36',
    '$X-Amzn-Trace-Id': 'NxL=6ea85ba6c8df48628d08a957e4fe3566.26',
    '$Authorization': 'Bearer MST_SFe4S0cpmcQspgASaQD0jm6IWkCWKP0yz_ZLO6MMv1geyoEZvsQjyuyh4Ag9orKlkoA1li-EmpWsD-70dSH0lMfc-PwaADrNIQjtFDwOpKQuyWeSOWq0xT_CnvJOL0FgE8htTdBCQH4.',
    '$Accept': '*/*',
    '$Referer': 'https://nxl.nxfs.nexon.com/nxl/main/games/10100',
    '$Accept-Encoding': 'gzip, deflate',
    '$Accept-Language': 'en-US',
}
    params = (
    ('product_id', '10100'),
    )
    r = requests.get('https://api.nexon.io/maintenance', headers=headers, params=params, verify=False)



    data=""
    try:
        data=r.json()
    except ValueError:
        return [False,"The game is up."]

    if len(data)==0:
        return [False,"The game is up."]
    else:
        return [True, data['message']+"\nMaintenance type: "+data['maintenanceMode']]

def latestNews(gameid=MAPLEID):
    r = requests.get('https://nxl.nxfs.nexon.com/news/regions/1/10100/en-US/list.json', verify=False)
    try:
        data=r.json()
        data[0]["url"]="https://maplestory.nexon.net/news/"+str(int(data[0]["Id"]*-1))
        return data[0]
    except ValueError:
        return {"Id" : -1, "url" : ""}

def latestSale(gameid=MAPLEID):
    r = requests.get('https://gapi.nexon.net/cms/news/1180/sale', verify=False)
    try:
        data=r.json()
        data[0]["url"]="https://maplestory.nexon.net/news/"+str(data[0]["Id"])
        return data[0]
    except ValueError:
        return {"Id" : -1, "url" : ""}


# test=underMaintenance(10100)
# print(test[0])




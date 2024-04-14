import json
from playwright.sync_api import sync_playwright, Page, Route, BrowserContext
from tqdm.auto import tqdm
from utils.models import PerformanceAudit

def _block_by_type(resource_type: str):
    def block_requests(route: Route):
        if route.request.resource_type == resource_type:
            return route.abort()
        return route.continue_()
    return block_requests

def _block_by_name(resource_name: str):
    def block_requests(route: Route):
        if resource_name in route.request.url:
            return route.abort()
        return route.continue_()
    return block_requests

def _add_cookies(context: BrowserContext, cookies_file: str):
    with open(cookies_file, 'r') as f:
        cookies = json.loads(f.read())
    context.add_cookies(cookies)

def get_performance_data(
        page: Page,
        url: str,
        block: bool = False
    ) -> PerformanceAudit:
    try:
        # print(f'[+] Fetching {url}')
        page.goto(url)
        performance_obj = page.evaluate("()=> JSON.stringify(window.performance.getEntriesByType('navigation'))")
        data = json.loads(performance_obj)[0]
        return PerformanceAudit(**data, block=block)
    except Exception as e:
        print(f'[!] Fail on fetching {url}')
        return None
    
def run_audits(
        urls: list[str],
        resource_type: str = None,
        resource_name: str = None,
        cookies_file: str = None,
        headless: bool = True
    ) -> list[PerformanceAudit]:

    with sync_playwright() as p:
        print('[+] Audit started')
        block = False
        browser = p.chromium.launch(headless=headless)
        context = browser.new_context()

        if cookies_file:
           _add_cookies(context, cookies_file)

        if resource_name:
            block = True
            block_requests_by_name = _block_by_name(resource_name)
            context.route('**/*', block_requests_by_name)
        
        if resource_type:
            block = True
            block_requests_by_type = _block_by_type(resource_type)
            context.route('**/*', block_requests_by_type)
        
        page = context.new_page()
        audits = [get_performance_data(page, url, block) for url in tqdm(urls)]
        print('[+] Audit finished')
        print(f'[+] Audited {len(audits)} pages')
        return list(filter(lambda x: x is not None, audits))
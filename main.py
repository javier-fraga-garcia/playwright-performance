import typer
import pandas as pd
from utils.performance import run_audits

def main(
        urls_path: str,
        results_path: str,
        resource_type: str = None,
        resource_name: str = None,
        cookies_file: str = None,
        headless: bool = True
    ):
    """Audits the performance of multiple pages and generates a results file

    Args:

        urls_path: The path to the .txt file with the urls to be audited

        results_path: The path and name of the results csv file to be generated. Example: ./data/results.csv

        resource_type [OPTIONAL]: The type of requests you want to block during the audit. Example: image
        
        resource_name [OPTIONAL]: The full or partial name of the requests to be blocked. Example: bootstrap.js    

        cookies_file [OPTIONAL]: The path to a cookie configuration .json file

        headless [OPTIONAL]: A boolean value indicating whether to perform the audit in headless mode or not.
    """
    try:
        with open(urls_path, 'r') as f:
            urls = {u.strip() for u in f.read().split('\n') if len(u) > 0}

        audits = run_audits(urls, resource_type=resource_type, resource_name=resource_name, cookies_file=cookies_file, headless=headless)
        df = pd.DataFrame([audit.model_dump() for audit in audits])
        df.to_csv(results_path, index=None, encoding='utf-8')
        print('[+] File created')
    except Exception as e:
        print('[!] Something went wrong')
        print(f'\n{e}')


if __name__ == '__main__':
    typer.run(main)
import subprocess
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add the parent directory to the sys.path
import config


def run_scrapy_crawl():
    try:
        # Run the command in the terminal
        subprocess.run(["scrapy", "crawl", "blogSpider"], check=True)
        # FIXME: replace with logger
        print("scrapy crawl blogSpider completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running scrapy crawl blogSpider: {e}")

def get_ids_via_curl():
    try:
        subprocess.run(["curl", "--location", "--globoff",
                        ( config.content_url +
                        "?_px_fk=media_type&_px_fv=page&_px_p=0&_px_ps=500&_px_sk=modif_dtime&_px_so=d&graphql={counts%2Ccurrent_page%2Citems_per_page%2Cpage_number%2Citems{name}}"),
                        "-o",
                        "./scrape/blog_ids.json"],
                    check=True)
        print("GET request for getting the blog ids was successful.")
    except:
        print("Error in getting the blog ids.")

get_ids_via_curl()

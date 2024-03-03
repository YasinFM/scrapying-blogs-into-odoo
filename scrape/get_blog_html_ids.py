import subprocess
import config
import make_logs

def run_scrapy_crawl():
    try:
        # Run the command in the terminal
        subprocess.run(["scrapy", "crawl", "blogSpider"], check=True)
        # FIXME: replace with logger
        print("scrapy crawl blogSpider completed successfully.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running scrapy crawl blogSpider: {e}")
        return False

def get_ids_curl():
    #   Runs a curl request on the website and returns all blogs' ids
    try:
        subprocess.run(["curl", "--location", "--globoff",
                        ( config.content_url +
                        "?_px_fk=media_type&_px_fv=page&_px_p=0&_px_ps=500&_px_sk=modif_dtime&_px_so=d&graphql={counts%2Ccurrent_page%2Citems_per_page%2Cpage_number%2Citems{name}}"),
                        "-o",
                        "./scrape/blog_ids.json"],
                    check=True)
        print("\nGET request for getting the blog ids was successful.")
        return True
    except:
        print("\nError in getting the blog ids.")
        return False

def scrapy_crawl():
    wasSuccessful = run_scrapy_crawl()
    if wasSuccessful:
        log = make_logs.log_type.GET_IDS
        make_logs.make_log(log,type=0)
    else:
        log = make_logs.log_type.GET_IDS
        make_logs.make_error_log(log,type=0)

def get_ids_via_curl():
    wasSuccessful = get_ids_curl()
    if wasSuccessful:
        log = make_logs.log_type.GET_IDS
        make_logs.make_log(log,type=1)
    else:
        log = make_logs.log_type.GET_IDS
        make_logs.make_error_log(log,type=1)
    
get_ids_via_curl()

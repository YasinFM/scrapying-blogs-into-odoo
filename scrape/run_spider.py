import subprocess

def run_scrapy_crawl():
    try:
        # Run the command in the terminal
        subprocess.run(["scrapy", "crawl", "blogSpider"], check=True)
        print("scrapy crawl blogSpider completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running scrapy crawl blogSpider: {e}")

if __name__ == "__main__":
    run_scrapy_crawl()

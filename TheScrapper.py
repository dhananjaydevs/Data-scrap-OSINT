import argparse
from modules.scrapper import Scrapper
from modules.info_reader import InfoReader


def process_url(url: str):
    print(f"\nTarget → {url}")
    print("=" * 60)

    scrap = Scrapper(url)
    links, text = scrap.crawl()

    print("FOUND LINKS:", links)
    print("SCRAPPED TEXT PREVIEW:", text[:300])

    # Correct argument name
    IR = InfoReader(text=text)

    print("RAW TEXT:", IR.text[:500])

    # Extract info
    emails = IR.getEmails()
    phones = IR.getPhoneNumbers()

    # Correct method name
    social = IR.getSocials()

    return {
        "emails": emails,
        "phones": phones,
        "social": social,
        "links": links,
        "raw": text
    }


def main():
    parser = argparse.ArgumentParser(description="V-Scrap — Simple Web Scraper & Info Extractor")
    parser.add_argument("-u", "--url", required=True, help="Target URL to scrape")

    args = parser.parse_args()

    result = process_url(args.url)

    print("\n" + "=" * 60)
    print("V-SCRAP RESULTS")
    print("=" * 60)

    print("\nE-Mails:")
    for e in result["emails"]:
        print(" -", e)

    print("\nNumbers:")
    for p in result["phones"]:
        print(" -", p)

    print("\nSocial Media:")
    for s in result["social"]:
        print(" -", s)

    print("\nFound Links:")
    for l in result["links"]:
        print(" -", l)

    print("\nDone.")


if __name__ == "__main__":
    main()

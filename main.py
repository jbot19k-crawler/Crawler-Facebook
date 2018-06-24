import FacebookCrawler as FBCrawler
import time

def main():
    token = 'EAACEdEose0cBADvZAEM7EjLhigTsx7FmofA8yZAnsZCMcb1OZB7uoNPzYDoNEHJ6jsuOtchcnZCLkiZC4vYY5bXzeeZAupmRxrCRKbbntEyybZCWvtHmQZAuw8kPbmSQ1mByoREcFKyhmbJUDih8lnXFfuBBAxR0C6FURyrdpCuZClZA3maEvQlMl0DZCvH0lJmXDiwZD'
    fanpage_name = 'ETtoday新聞雲'
    fanpage_id = '242305665805605'
    page = 1

    print('Fan Page: ' + fanpage_name)
    print('Page: ' + str(page))

    start = time.time()
    posts = FBCrawler.Crawl(token, fanpage_id, page)
    print(u'Spend {} seconds on crawling.'.format(time.time()-start))

    ans = input('Save to database? [yes/no]:')
    if ans.lower() == 'yes':
        FBCrawler.Save2DB('data.db', posts)
    ans = input('Save to excel? [yes/no]:')
    if ans.lower() == 'yes':
        FBCrawler.Save2Excel(posts)

if __name__ == '__main__':
    main()
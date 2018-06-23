import warnings
warnings.filterwarnings('ignore')

import requests
import sqlite3
from bs4 import BeautifulSoup
from pandas import DataFrame
from multiprocessing import Pool

#######################################################
# crawl the given fan page                            #
# param: token -> your access token                   #
#        fanpage_id -> ID of the fan page             #
#        page -> number of pages that will be crawled #
#######################################################
def Crawl(token, fanpage_id, page):
    result = requests.get('https://graph.facebook.com/v3.0/{}/posts?limit=100&access_token={}'.format(fanpage_id, token))
    post_list = list()

    i = 0
    while True:
        if i == page:
            break
        i += 1

        for post in result.json()['data']:
            if 'message' in post:
                post_res = requests.get('https://graph.facebook.com/v3.0/{}?fields=likes.limit(0).summary(True),shares&access_token={}'.format(post['id'], token))
                if 'likes' in post_res.json():
                    likes = post_res.json()['likes']['summary'].get('total_count')
                else:
                    likes = 0

                if 'shares' in post_res.json():
                    shares = post_res.json()['shares'].get('count')
                else:
                    shares = 0

                post_list.append({
                    'date': post['created_time'],
                    'content': post['message'], 
                    'like': likes, 
                    'share': shares
                })

        if 'paging' in result.json():
            if 'next' in result.json()['paging']:
                result = requests.get(result.json()['paging']['next'])
            else:
                break
        else:
            break

    return post_list

##########################################
# save data into SQLite database         #
# param: db_name -> name of the database #
#        posts -> posts data             #
##########################################
def Save2DB(db_name, posts):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    create_table = """ CREATE TABLE IF NOT EXISTS table1(
                        ID integer PRIMARY KEY,
                        date text NOT NULL,
                        content text NOT NULL,
                        like text NOT NULL,
                        share text NOT NULL
                        ); """
    cur.execute(create_table)
    for i in posts:
        cur.execute("insert into table1 (date, content, like, share) values (?, ?, ?, ?)",
            (i['date'], i['content'], i['like'], i['share']))
    conn.commit()
    conn.close()

##############################
# save data into excel       #
# param: posts -> posts data #
##############################
def Save2Excel(posts):
    dates = [entry['date'] for entry in posts]
    contents = [entry['content'] for entry in posts]
    likes = [entry['like'] for entry in posts]
    shares = [entry['share'] for entry in posts]
    df = DataFrame({
        'date': dates,
        'content': contents,
        'like': likes,
        'share':shares
        })
    df.to_excel('data.xlsx', sheet_name='sheet1', index=False, columns=['date', 'content', 'like', 'share'])
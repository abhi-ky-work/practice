

# import requests


# total_pages = 10
# page_number = 2
# pageNum = stdInput1


# url = 'https://jsonmock.hackerrank.com/api/articles?page={pageNum}'
# # data = ''''''
# # response = requests.get(url)

# response = '''{
#     page : 1,
#     per_page : 4,
#     total : 34,
#     total_pages : 34,
#     data : [{
#     title : "tithle hai ye",
#     url : "url hai ye ", 
#     author : "author hai ye",
#     num_comments : "no of comments",
#     story_id : "this is story id ",
#     story_title : "this is story title ",
#     story_url: "this is story url ",
#     parent_id: "this is  parnt id ",
#     created_at: "this is story created at ",
#     },
#     {
#     title : "tithle hai ye",
#     url : "url hai ye ", 
#     author : "author hai ye",
#     num_comments : "no of comments",
#     story_id : "this is story id ",
#     story_title : "this is story title ",
#     story_url: "this is story url ",
#     parent_id: "this is  parnt id ",
#     created_at: "this is story created at ",
#     },{
#     title : "tithle hai ye",
#     url : "url hai ye ", 
#     author : "author hai ye",
#     num_comments : "no of comments",
#     story_id : "this is story id ",
#     story_title : "this is story title ",
#     story_url: "this is story url ",
#     parent_id: "this is  parnt id ",
#     created_at: "this is story created at ",
#     },

#     ]
# }'''



# def getArticleName(res):
#     res_data = res.data

#     res = []
#     for rec in res_data:
#         res_obj = {}
#         if rec.title :
#             res_obj["title"].append(rec.title)
#         else:
#             if rec.story_title :
#                 res_obj["story_title"].append(rec.story_title)
        
#         if rec.title == "" and rec.story_title == "":
#             pass
#         res.append(rec)

#     return res


# def topArticles(limit):
#     limit = 2

#     res = getArticleName(response)
#     new_res = sorted_list = sorted(res, key="num_comments" x: (x[0], -x[1]))

#     return limit






import requests  # Import the requests library for making HTTP requests

def top_articles(limit):
    if limit < 0:
        return []

    def make_request(page_number=1):
        response = requests.get(f"https://jsonmock.hackerrank.com/api/articles?page={page_number}")
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()

    def get_title(article):
        return article.get('title') or article.get('story_title') or None

    articles = []
    init_request = make_request()
    articles.extend(init_request['data'])

    for i in range(2, init_request['total_pages'] + 1):
        new_req = make_request(i)
        articles.extend(new_req['data'])

    for article in articles:
        article['parsed_name'] = get_title(article)

    # Sort by number of comments (treat None as 0) and then alphabetically by title
    articles.sort(key=lambda a: (
        -a.get('num_comments', 0) if a.get('num_comments') is not None else 0,
        a['parsed_name'] if a['parsed_name'] is not None else ""
    ))

    # Limit the number of articles to the specified limit
    articles = articles[:limit]

    final_article = [article['parsed_name'] for article in articles]
    for item in final_article:
        if item is not None:
            print( item )

    return final_article
# Example usage

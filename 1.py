import requests

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'cookie': '',#这边是你的cookie
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.douyin.com/?recommend=1',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

params = {
    'aweme_id': '7409181037001018687',#视频id还是个人id？不确定
    'cursor': '20',#页数
    'count': '200',#条数

}

response = requests.get('https://www.douyin.com/aweme/v1/web/comment/list/', params=params, headers=headers).json()


# 提取用户名、评论内容和个人标识符
for comment in response['comments']:
    username = comment['user']['nickname']
    comment_text = comment['text']
    user_id = comment['user']['uid']
    print(f"用户名: {username}, 评论内容: {comment_text}, 用户ID: {user_id}")
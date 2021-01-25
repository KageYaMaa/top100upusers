import requests
from bs4 import BeautifulSoup

url_upuser_search = "https://search.bilibili.com/upuser"      ## 加上up主的名字去搜索

def enter_space(name):
    params = {"keyword":name}                                 ## 拼接搜索参数

    # 搜索UP主的名字
    response_upuser_search = requests.get(url = url_upuser_search,
                                          params = params)

    print("当前搜索UP主：" + name)

    # 从返回的数据中拿到带UP主uid的space主页链接
    response_upuser_search_soup = BeautifulSoup(response_upuser_search.text,
                                                "lxml")
    for each_a_tag in response_upuser_search_soup.findAll(name = "a"):
        if each_a_tag.string == name:
            url_upuser_space = each_a_tag["href"]

    # 拼接一个正确的space地址
    url_upuser_space = "https:" + url_upuser_space.split("?")[0] + "/video"

    print("UP主的主页地址是：" + url_upuser_space)

    return url_upuser_space

if __name__ == '__main__':
    print(enter_space("啊吗粽"))
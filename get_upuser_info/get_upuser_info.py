'''
author:kageyama
date:2021/01/24
get information of a upuser in bilibili
'''

from selenium import webdriver
import time

from get_upuser_info import enter_space

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"

def get_upuser_info(name,url_upuser_space):

    upuser_info = {"name":name,
                   "follow_info":
                       {"following":0,
                        "followers":0,
                        "like_cnt":0,
                        "play_cnt":0}}

    driver = webdriver.Chrome(executable_path = chromedriver)

    # 进入个人主页
    driver.get(url_upuser_space)

    # 找到关注、粉丝、点赞、播放相关的数据
    time.sleep(2)
    following = driver.find_element_by_css_selector("a.n-data.n-gz").get_attribute("title")
    followers = driver.find_element_by_css_selector("a.n-data.n-fs").get_attribute("title")
    # like_cnt = driver.find_element_by_css_selector("div.n-data.n-bf")[0].get_attribute("title")
    # play_cnt = driver.find_element_by_css_selector("div.n-data.n-bf")[1].get_attribute("title")

    upuser_info["follow_info"]["following"] = following
    upuser_info["follow_info"]["followers"] = followers
    # upuser_info["like_cnt"] = like_cnt
    # upuser_info["play_cnt"] = play_cnt


    upuser_info["type_info"] = {}
    # 常发的品类专区
    type_fliter = driver.find_element_by_css_selector("div#submit-video-type-filter")
    types = type_fliter.find_elements_by_css_selector("a")
    for type in types:
        upuser_info["type_info"][type.text[:2]] = type.find_element_by_css_selector("span").text

    # 开始找视频信息
    video_info_list = []

    # 翻页机制，如果下一页没有显示的话

    # 在每一页都执行一次

    for each_video in driver.find_elements_by_css_selector("li.small-item.fakeDanmu-item"):
        video_info = {}
        video_info["video_name"] = each_video.find_elements_by_css_selector("a")[1].get_attribute("title")
        video_info["video_play_cnt"] = each_video.find_element_by_css_selector("span.play").text
        video_info["video_time"] = each_video.find_element_by_css_selector("span.time").text
        video_info_list.append(video_info)

    next_page = driver.find_element_by_css_selector("li.be-pager-next")

    while next_page.is_displayed():
        next_page.click()
        time.sleep(3)
        for each_video in driver.find_elements_by_css_selector("li.small-item.fakeDanmu-item"):
            video_info = {}
            video_info["video_name"] = each_video.find_elements_by_css_selector("a")[1].get_attribute("title")
            video_info["video_play_cnt"] = each_video.find_element_by_css_selector("span.play").text
            video_info["video_time"] = each_video.find_element_by_css_selector("span.time").text
            video_info_list.append(video_info)
        next_page = driver.find_element_by_css_selector("li.be-pager-next")
        time.sleep(3)

    upuser_info["video_info"] = video_info_list

    return upuser_info



if __name__ == '__main__':
    print(get_upuser_info("啊吗粽", enter_space.enter_space("啊吗粽")))
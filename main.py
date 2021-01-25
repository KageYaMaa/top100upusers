from get_upuser_names import get_names
from get_upuser_info import enter_space
import get_upuser_info
import json
from selenium.common import exceptions


src = "src/name_list.txt"
names = get_names.get_names(src)               # 所有UP主名字的list

with open(r"C:\Users\Admin\Desktop\top100up\upuser_info.txt","w",encoding="utf-8") as file:
    for each_name in names:
        try:
            upuser_info = get_upuser_info.get_upuser_info(name = each_name,
                                                          url_upuser_space = enter_space.enter_space(each_name))
            print(json.dumps(upuser_info,ensure_ascii=False))
            file.write(json.dumps(upuser_info,ensure_ascii=False))
            file.write("\r/n")
        except exceptions.NoSuchElementException:
            print("出错啦")
            continue

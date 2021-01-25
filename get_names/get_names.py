def get_names(src):
    with open(src,"r",encoding = "UTF-8") as file:
        name_list = file.read()
    return name_list.split("、")

if __name__ == "__main__":
    src = "../src/name_list.txt"
    get_names(src)
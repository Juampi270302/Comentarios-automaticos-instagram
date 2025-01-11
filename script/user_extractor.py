import json


def extractor_username_from_json():
    followers = []
    with open("../people_to_mencion/followers_1.json", 'r') as file:
        data = json.load(file)
    for follower in data:
        data_follower = follower["string_list_data"]
        followers.append(data_follower[0]["value"])
    print(followers)
    create_txt(followers)


def create_txt(followers):
    with open("../people_to_mencion/people_to_mencion.txt", 'w') as file:
        for follower in followers:
            file.write("@" + follower + "\n")


def extractor_name():
    with open("../people_to_mencion/people_to_mencion.txt", "r") as file:
        array = [line.strip() for line in file]
    return array


import requests
from time import sleep
import datetime
import os



one_hour = 3600
sleep_time = one_hour


def print_changes(old_list, new_list):
    print("The following games have been added to The Hotness")
    for game in new_list:
        if game not in old_list:
            print(game)
    print("The following items have been removed from The Hotness")
    for game in old_list:
        if game not in new_list:
            print(game)
    print("These games have changed rank in The Hotness")
    moved_games = []
    for game in new_list:
        if game in old_list:
            moved_games.append(game)
    #we are going to look at moved games one by one and perform subtraction if index of old and new do not equal zero print name
    for game in moved_games:
        old_index = old_list.index(game)
        new_index = new_list.index(game)
        dif = old_index - new_index
        if dif != 0:
            print("{} has changed position by {}".format(game, dif))

def write_changes(old_list, new_list):
    BGG_hotness.write("Last updated" + str(currentDT) + "\n")
    BGG_hotness.write("The following games have been added to The Hotness")
    BGG_hotness.write('\n')
    for game in new_list:
        if game not in old_list:
            BGG_hotness.write(game)
            BGG_hotness.write('\n')
    BGG_hotness.write('\n')
    BGG_hotness.write('\n')
    BGG_hotness.write("The following items have been removed from The Hotness")
    BGG_hotness.write('\n')
    for game in old_list:
        if game not in new_list:
            BGG_hotness.write(game)
            BGG_hotness.write('\n')
    BGG_hotness.write('\n')
    BGG_hotness.write('\n')
    BGG_hotness.write("These games have changed rank in The Hotness")
    BGG_hotness.write('\n')
    moved_games = []
    for game in new_list:
        if game in old_list:
            moved_games.append(game)
    for game in moved_games:
        old_index = old_list.index(game)
        new_index = new_list.index(game)
        dif = old_index - new_index
        if dif != 0:
            BGG_hotness.write("{} has changed position by {}".format(game, dif))
            BGG_hotness.write('\n')
    BGG_hotness.write('\n')
    BGG_hotness.write('\n')

def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))



def write_file(new_list):
    BGG_hotness.write("This List was last updated: " + str(currentDT) + "\n")
    for game in new_list:
        BGG_hotness.write(game)
        BGG_hotness.write('\n')

def get_games():
    url = "https://boardgamegeek.com/api/hotness"
    response = requests.get(url)
    json = response.json()
    games = json['items']
    names = [game["name"] for game in games]
    return names
print("Initailizing script getting games")
old_list = get_games()

print(old_list)
sleep(sleep_time)
while True:
    BGG_hotness = open("/Users/alexlaursen/PycharmProjects/BGG_hotness_py3/BGG_hotness_py3.txt", "w")
    currentDT = datetime.datetime.now()
    print("Checking current list")
    new_list = get_games()
    if new_list != old_list:
        print("The rankings have changed as of " + str(currentDT))
        print_changes(old_list, new_list)
        print(new_list)
        write_changes(old_list, new_list)
        write_file(new_list)
        BGG_hotness.close()
        notify("BGG Hotness", "The Hotness list has been updated!")


    else:
        print("The rankings have stayed the same as of " + str(currentDT))
        old_list = new_list
        print(new_list)
        write_file(new_list)
        BGG_hotness.close()
    sleep(sleep_time)




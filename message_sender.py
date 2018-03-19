import requests
import random
import time


class Assassin:
    def __init__(self, content):
        self.name = content[0]
        self.my_target = content[1]
        self.status = content[2]
        self.round_of_status = content[3]
        self.grade = content[4]
        self.section = content[5]
        self.number = content[6]
        self.has_new_target = content[7]
        self.error = content[8]

    def set_my_target(self, target):
        self.my_target = target

    def set_targeted_by(self, target):
        self.targeted_by = target


def send_to_all(all_assassins):
    if input("Are you sure you want to send a message to everyone?") != "yes":
        print("Exiting")
        exit(1)
    for assassin in all_assassins[:]:
        if "Yes" not in assassin.has_new_target or "Alive" not in assassin.status:
            continue

        message = ("Be wary, " + assassin.name + " EVERYONE has a NEW target! Yours is " + assassin.my_target
                   + ". Confirm you got this message by replying 'pizzicato'")

        encoded_message = requests.utils.quote(message, safe='')

        gateway = "http://192.168.1.154:8766/"

        number = assassin.number

        url = gateway + "?number=" + str(number) + "&message=" + encoded_message

        response = requests.get(url)
        print(assassin.name + ":")
        print(response)

        time.sleep(5)


if __name__ == "__main__":
    all_assassins = []
    with open("data/new_target_list.csv") as doc:
        for line in doc.readlines():
            if line != "\n":
                content = line.split(",")
                assassin = Assassin(content)
                all_assassins.append(assassin)

    send_to_all(all_assassins)





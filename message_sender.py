import requests
import random
import time


class Assassin:
    def __init__(self, content):
        self.name = content[0]
        self.status = content[1]
        self.round_of_status = content[2]
        self.grade = content[3]
        self.section = content[4]
        self.number = content[5]
        self.my_target = content[6]
        self.targeted_by = content[7]
        self.has_new_target = content[8]
        self.has_new_target = content[9]
        self.error = content[10]

    def set_my_target(self, target):
        self.my_target = target

    def set_targeted_by(self, target):
        self.targeted_by = target


def send_to_all(all_assassins):
    if input("Are you sure you want to send a message to everyone?") != "yes":
        print("Exiting")
        exit(1)
    for assassin in all_assassins:
        if assassin.status == "Dead" or "Yes" not in assassin.error:
            continue
        section = assassin.section
        if section == '':
            section = "Oops, you never wrote down a section!"
        message = ("Hello, and thank you for registering for Spoon Assassins. " 
                   + "You signed up with the following:\n"
                   + "Name: " + assassin.name + "\n"
                   + "Grade: " + assassin.grade + "\n"
                   + "Section: " + assassin.section + "\n"
                   + "If any of that is incorrect, reply with the correction. Otherwise, reply 'vivace'")

        encoded_message = requests.utils.quote(message, safe='')

        gateway = "http://192.168.1.154:8766/"

        number = assassin.number

        url = gateway + "?number=" + str(number) + "&message=" + encoded_message

        response = requests.get(url)
        print(response)

        time.sleep(1)


if __name__ == "__main__":
    all_assassins = []
    with open("data/new_target_list.csv") as doc:
        for line in doc.readlines():
            if line != "\n":
                content = line.split(",")
                assassin = Assassin(content)
                all_assassins.append(assassin)
    # assign_targets(all_assassins)

    send_to_all(all_assassins)





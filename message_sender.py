import requests
import random


class Assassin:
    def __init__(self, in_name, in_grade, in_number):
        self.name = in_name
        self.grade = in_grade
        self.number = in_number
        self.my_target = None
        self.targeted_by = None

    def set_my_target(self, target):
        self.my_target = target

    def set_targeted_by(self, target):
        self.targeted_by = target


def send_to_all(all_assassins):
    if input("Are you sure you want to send a message to everyone?") != "yes":
        exit(1)

    for assassin in all_assassins[90:]:
        message = "Ok, " + assassin.name + ". Your actual first target is " + assassin.my_target + ". Good luck and godspeed!"

        #message = "Sorry, a few people have duplicate targets. Disregard your first target an know you will get a new target in a few minutes."

        url = "http://smsgateway.me/api/v3/messages/send"

        print(message)
        data = {
        "email": "gabrielmukobi@gmail.com",
        "password":	"a4beb3b8ec",
        "device": 66226,
        "number": assassin.number,
        "message": message
        }

        print(data)
        response = requests.post(url, data=data)

        print(response.text)


def assign_targets(all_assassins):
    for assassin in all_assassins:
        target_num = random.randint(0, len(all_assassins) - 1)
        while True:
            x = all_assassins[target_num].name
            target_num = random.randint(0, len(all_assassins) - 1)
            if(all_assassins[target_num].name != assassin.name
              and all_assassins[target_num].my_target != assassin.name
              and all_assassins[target_num].targeted_by is None):
                break

        all_assassins[target_num].set_targeted_by(assassin.name)
        assassin.set_my_target(all_assassins[target_num].name)

    target_list = []
    for assassin in all_assassins:
        #print(assassin.my_target)
        target_list.append(assassin.my_target)
        print(assassin.name + " is targeting " + assassin.my_target + " and targeted by " + assassin.targeted_by)

    target_list = sorted(target_list)
    print("\n\n\n")
    print(len(target_list))
    print(len(all_assassins))
    print("\n\n")
    for name in target_list:
        print(name)

    # with open("data/new_target_list.csv", "w") as doc:
    #     for assassin in all_assassins:
    #         doc.write(assassin.name + "," + assassin.grade + "," + assassin.number + "," + assassin.my_target + "," + assassin.targeted_by + ",\n")

    # return all_assassins


if __name__ == "__main__":
    all_assassins = []
    with open("data/new_target_list.csv") as doc:
        for line in doc.readlines():
            if line != "\n":
                content = line.split(",")
                assassin = Assassin(content[0], content[1], content[2])
                assassin.set_my_target(content[3])
                assassin.set_targeted_by(content[4])
                all_assassins.append(assassin)
    print(all_assassins)

    #all_assassins = assign_targets(all_assassins)

    send_to_all(all_assassins)




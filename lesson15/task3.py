# Create a simple prototype of a TV controller in Python. It’ll use the following commands:
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes",
# if the channel N or 'name' exists in the list, or "No" - in the other case.
# The default channel turned on before all commands is №1.
# Your task is to create the TVController class and methods described above.


CHANNELS = ["BBC", "Discovery", "TV1000"]

class TVController:
    activeChanel = 0
    def __init__(self, list):
        self.list = list

    def first_channel(self):
        TVController.activeChanel = 0
        return self.list[0]

    def last_channel(self):
        TVController.activeChanel = len(self.list) - 1
        return self.list[TVController.activeChanel]

    def turn_channel(self, n):
        TVController.activeChanel = n-1
        return self.list[TVController.activeChanel]

    def next_channel(self):
        if TVController.activeChanel+1 > len(self.list) - 1:
            TVController.activeChanel = 0
            return self.list[0]
        TVController.activeChanel += 1
        return self.list[TVController.activeChanel]

    def previous_channel(self):
        if TVController.activeChanel-1 < 0:
            TVController.activeChanel = len(self.list) - 1
            return self.list[TVController.activeChanel]
        TVController.activeChanel -= 1
        return self.list[TVController.activeChanel]

    def current_channel(self):
        return self.list[TVController.activeChanel]

    def is_exist(self, val):
        try:
            if isinstance(val, str):
                for i in self.list:
                    if i == val:
                        return "Yes"
                return "No"

            if isinstance(val, int):
                if self.list[val]:
                    return "Yes"

            else:
                return "No"

        except IndexError:
            return 'No'




controller = TVController(CHANNELS)

print(controller.first_channel() == "BBC")

print(controller.last_channel() == "TV1000")

print(controller.turn_channel(1) == "BBC")

print(controller.next_channel() == "Discovery")

print(controller.previous_channel() == "BBC")

print(controller.current_channel() == "BBC")

print(controller.is_exist(4) == "No")

print(controller.is_exist("BBC") == "Yes")
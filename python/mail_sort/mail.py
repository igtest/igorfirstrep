import time
import copy
import random
import itertools

number_of_messages = 10

now = time.time()
two_week = 1209600
one_month = 2629743
two_week_ago = now - two_week
two_month_ago = now - one_month*2


message_list1 = []
message_list2 = []
mails = ['i@mail.ru', 'ibrikin@gmail.com', 'example@example.com', 'foo@yandex.ru']

class Message():
    def __init__(self, date, message_from, unread=True):
        self.message_id = str(id(self))
        self.date = date
        self.message_from = message_from
        self.unread = unread
        self.read_key = 0
        self.count = 1
    def __repr__(self):
        return 'Message from {0} on {1}. ID {2}. {3}, key={4}'.format(self.message_from,
        time.ctime(self.date), self.message_id, self.unread, self.read_key)
    def __eq__(self, other):
        return self.message_id == other.message_id

    def readMessage(self):
        self.unread = False
        self.read_key += 1

    def unreadMessage(self):
        self.unread = True

    def getDate(self):
        return self.date
    def getStatus(self):
        return self.unread
    def getStatusKey(self):
        return self.read_key

def generate_message_set():
    random_num_message = random.randint(1, number_of_messages)
    for i in range(random_num_message):
        random_date = random.randint(int(two_month_ago), int(two_week_ago))
        mail = mails[random.randint(0, len(mails)-1)]
        message_list1.append(Message(random_date, mail))

def todays_message_set():
    for i in range(random.randint(1,int(len(message_list2)//2))):
        del message_list2[i]

    for i in range(random.randint(1,14)):
        random_date = random.randint(int(two_week_ago), int(now))
        mail = mails[random.randint(0, len(mails)-1)]
        message_list2.append(Message(random_date, mail))

    for i in range(len(message_list2)):
        case = random.randint(0,1)
        if case == 1: # read message
            message_list2[random.randint(0, len(message_list2)-1)].readMessage()
        else:         # unread message
            index = random.randint(0, len(message_list2)-1)
            if message_list2[index].unread == True:
                message_list2[index].readMessage()
            message_list2[index].unreadMessage()


class Analyse():
    def __init__(self,oldest_set, *args):
        self.oldest_set = oldest_set
        self.set_of_days = args
        self.full_list = []
    def getFull(self):
        self.full_list = self.oldest_set[:]
        for bunch in self.set_of_days:
            for message in bunch:
                self.full_list.append(message)
    def getNextMessage(self):
        self.getFull()
        for message in self.full_list:
            yield message
    def countMessage(self): # count unique number of messages
        count = set(message.message_id for message in self.getNextMessage())
        return len(count)

    def isLastMonth(self, message):
        current_month = time.localtime(now)
        message_month = time.localtime(message.date)
        if current_month.tm_mon != message_month.tm_mon:
            return False
        else:
            return True

    def isReadMessage(self, message):
        if ((message.unread == False or message.unread == True)and message.read_key != 0) or (message.unread == False and message.read_key == 0):
            return True
        else:
            return False
    def countReadMessages(self):
        """Count all Messages which read"""
        count = set(message.message_id for message in self.getNextMessage() if self.isReadMessage(message) == True)
        return len(count)

    def countReadMessagesLastMonth(self):
        """Count read Messages on the last month"""
        count = set(message.message_id for message in self.getNextMessage() if self.isReadMessage(message) == True and self.isLastMonth(message) == True)
        return len(count)


    def countUnreadMessages(self):
        """Count unread Messages"""
        count = set(message.message_id for message in self.getNextMessage() if self.isReadMessage(message) == False)
        return len(count)

    def countUnreadMessagesLastMonth(self):
        """Count unread Messages in the last month"""
        count = set(message.message_id for message in self.getNextMessage() if self.isReadMessage(message) == False and self.isLastMonth(message) == True)
        return len(count)

    def countReadMessagesRemovedLastMonth(self):
        """Count read removed Messages"""

        last_set = [message for message in self.set_of_days[-1] if self.isReadMessage(message) == True and self.isLastMonth(message) == True]
        all_mes = set(message.message_id for message in self.getNextMessage()if self.isReadMessage(message) == True and self.isLastMonth(message) == True)
        for message in last_set:
            if message.message_id in all_mes:
                all_mes.remove(message.message_id)
        return len(all_mes)
    # def countReadMessagesRemovedLastMonth(self):
    #     """Count read removed Messages for last month"""

    def countUnreadMessagesRemoved(self):
        """Count unread removed Messages"""
    def countUnreadMessagesRemovedLastMonth(self):
        """Count unread removed Messages for last month"""
        last_set = [message for message in self.set_of_days[-1] if self.isReadMessage(message) == False and self.isLastMonth(message) == True]
        all_mes = set(message.message_id for message in self.getNextMessage()if self.isReadMessage(message) == False and self.isLastMonth(message) == True)
        for message in last_set:
            if message.message_id in all_mes:
                all_mes.remove(message.message_id)
        return len(all_mes)

    def countMessagesFrom(self, mail):
        count = set(message.message_id for message in self.getNextMessage() if message.message_from==mail)
        return len(count)

    def countMessagesFromLastMonth(self, mail):
        count = set(message.message_id for message in self.getNextMessage() if message.message_from==mail and self.isLastMonth(message))
        return len(count)


if __name__ == '__main__':

    generate_message_set()
    message_list2 = copy.deepcopy([message for message in message_list1])
    todays_message_set()
    print(message_list1)
    print(len(message_list1))
    print('++++++++++++++++++++++')
    print(message_list2)
    print(len(message_list2))
    message_list3 = [1,2,3,4,5]
    analyse = Analyse(message_list1, message_list2)
    print("Получил всего сообщений: ", analyse.countMessage())
    print("Всего прочитанных сообщений: ", analyse.countReadMessages())
    print("Всего прочитанных сообщений за последний месяц: ", analyse.countReadMessagesLastMonth())
    print("Всего непрочитанных сообщений: ", analyse.countUnreadMessages())
    print("Всего непрочитанных сообщений за последний месяц: ", analyse.countUnreadMessagesLastMonth())
    print("Всего прочитанных сообщений и удаленных за последний месяц: ",analyse.countReadMessagesRemovedLastMonth())
    print("Всего непрочитанных сообщений и удаленных за последний месяц", analyse.countUnreadMessagesRemovedLastMonth())
    print("Получено сообщений от ibrikin@gmail.com: ", analyse.countMessagesFrom('ibrikin@gmail.com'))
    print("Получено сообщений от ibrikin@gmail.com за последний месяц: ", analyse.countMessagesFromLastMonth('ibrikin@gmail.com'))


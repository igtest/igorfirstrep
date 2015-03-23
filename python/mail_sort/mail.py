import time
import copy
import random
import itertools



now = time.time()
two_week = 1209600 # two week in Unix epoch time
one_month = 2629743 #one month in Unix epoch time
two_week_ago = now - two_week
two_month_ago = now - one_month*2


message_list1 = []
message_list2 = []
mails = ['i@mail.ru', 'somebody@gmail.com', 'example@example.com', 'foo@yandex.ru']

class Message():
    def __init__(self, date, message_from, unread=True):
        self.message_id = str(id(self))
        self.date = date
        self.message_from = message_from
        self.unread = unread
        self.read_key = 0
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
    number_of_messages = 10 #number of generate messages
    random_num_message = random.randint(1, number_of_messages)
    for i in range(random_num_message):
        random_date = random.randint(int(two_month_ago), int(two_week_ago))
        mail = mails[random.randint(0, len(mails)-1)]
        message_list1.append(Message(random_date, mail))

def todays_message_set():
    for i in range(random.randint(0,int(len(message_list2)//2))):
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
        """Count read removed Messages for last month"""

        last_set = [message for message in self.set_of_days[-1] if self.isReadMessage(message) == True and self.isLastMonth(message) == True]
        all_mes = set(message.message_id for message in self.getNextMessage()if self.isReadMessage(message) == True and self.isLastMonth(message) == True)
        for message in last_set:
            if message.message_id in all_mes:
                all_mes.remove(message.message_id)
        return len(all_mes)

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
    # for test
    a = Message(time.mktime(time.strptime('Fri Feb 20 13:48:23 2015')),mails[0], False)
    b = Message(time.mktime(time.strptime('Fri Mar 13 13:48:23 2015')),mails[0], True)
    c = Message(time.mktime(time.strptime('Sun Mar 8 13:48:23 2015')),mails[0], True)
    ab = Message(time.mktime(time.strptime('Fri Mar 20 13:48:23 2015')),mails[1], False)
    ac = Message(time.mktime(time.strptime('Sun Mar 22 13:48:23 2015')),mails[0], False)
    aa = Message(time.mktime(time.strptime('Wed Mar 18 13:48:23 2015')),mails[0], False)
    list1 = [a,c]
    list2 = [b,ab,ac,aa]
    #
    analyse = Analyse(message_list1, message_list2)
    analyse2 = Analyse(list1, list2) # for test
    # print("Total messages: ", analyse.countMessage())
    # print("Total read messages: ", analyse.countReadMessages())
    print("Total read messages for last month: ", analyse.countReadMessagesLastMonth())
    # print("Total unread messages: ", analyse.countUnreadMessages())
    print("Total unread messages for last month: ", analyse.countUnreadMessagesLastMonth())
    print("Total read messages and removed for last month: ",analyse.countReadMessagesRemovedLastMonth())
    print("Total unread messaged and removed for last month: ", analyse.countUnreadMessagesRemovedLastMonth())
    print("Received from somebody@gmail.com: ", analyse.countMessagesFrom('somebody@gmail.com'))
    print("Received from somebody@gmail.com for last month: ", analyse.countMessagesFromLastMonth('somebody@gmail.com'))
    print("==================================================================")
    # for test
    print("Total messages: ", analyse2.countMessage())
    print("Total read messages: ", analyse2.countReadMessages())
    print("Total read messages for last month: ", analyse2.countReadMessagesLastMonth())
    print("Total unread messages: ", analyse2.countUnreadMessages())
    print("Total unread messages for last month: ", analyse2.countUnreadMessagesLastMonth())
    print("Total read messages and removed for last month: ",analyse2.countReadMessagesRemovedLastMonth())
    print("Total unread messaged and removed for last month: ", analyse2.countUnreadMessagesRemovedLastMonth())
    print("Received from somebody@gmail.com: ", analyse2.countMessagesFrom('somebody@gmail.com'))
    print("Received from somebody@gmail.com for last month: ", analyse2.countMessagesFromLastMonth('somebody@gmail.com'))
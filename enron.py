""" Anna Brobbey-Mensah, INST326 0105, HW #3 """

import argparse
from multiprocessing.shared_memory import SharedMemory
import re
import argparse
import sys 



class Server:
#this class holds the data for emails in the dataset
    all_emails = [] 
    def __init___(self, path):
        self.path = path
        self.emails = []
        email_file = open(path, "r")
        email_parser = email_file.read()
        data = email_parser.split("End Email")

        for email_inbox in data:
            inbox_id = re.findall(r"\s\S(\d+\S\d+\S[a-zA-Z]+\S+@[a-zA-Z0-9]+)", email_inbox)
            date = r.findall(r"^Date:\s(\w+, \s\d+\s\w+\s\d+\s+\d*:\d+:\d+\s-\d+\s\(\w+\)$)", email_inbox)
            if re.search("Subject: (\s)", email_inbox):
                subject = re.findall("Subject:\s", email_inbox)
            else:
                subject = re.findall("Subject: (\s)", email_inbox)
            messenger = re.findall(r"From:\s(.+)$", email_inbox)
            receiver = re.compile("^To:\s(.+)$").search(email_inbox)
            content = re.compile("^(X-FileName)").search(email_inbox)
            email = Email(mail_id, date, subject, messenger, receiver, content)
            self.emails.append(email)

class Email:
#this class breaks down the individual parts of an email
    def __init__(self, message_id, date, subject, sender, receiver, body):
        self.message_id = message_id
        self.date = date
        self.subject = subject
        self.sender = sender 
        self.receiver = receiver
        self.body = body 

def parse_args(args_list):
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type = str, help = "the path to the next file.")
    args = parser.parse_args(args_list)

    return args



def main(path):
    server_class = Server(path)
    return len(server_class.emails)

if __name__ == "__main__":
    arguments = parse_args(sys.argv[1:-1])
    main(arguments.path)
#imports
import yaml

# variables
filepath1 = '../data/credentials.yaml'

# functions/steps
with open(filepath1, "r") as stream:
    credentials = yaml.safe_load(stream)

print(credentials)
qa_uname = credentials['qa']['username']
qa_pword = credentials['qa']['password']
uat_uname = credentials['uat']['username']
print('username for qa env', qa_uname)
print('password for qa env', qa_pword)
print('username for uat env', uat_uname)

# data for negative login tests:
qa_uname1 = credentials['negative'],['case1'],['username']
qa_pword1 = credentials['negative'],['case1'],['password']
qa_uname2 = credentials['negative'],['case2'],['username']
qa_pword2 = credentials['negative'],['case2'],['password']
qa_uname3 = credentials['negative'],['case3'],['username']
qa_pword3 = credentials['negative'],['case3'],['password']

# login_page.enter_username(qa_uname)
# login_page.enter_password(qa_pword)
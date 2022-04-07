import json
import boto3
import re
import time
import os

session = boto3.Session(
    aws_access_key_id="AKIAVY7FBWM6YHXQQIKZ",
    aws_secret_access_key="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",
    region_name="us-east-2"
)

s3_client = session.client("s3")
s3=session.resource("s3")
obj=s3.Object("zhai1976","us_state/sjc.csv")
ccs_str=obj.get()["Body"].read().decode("utf-8")
print(ccs_str)

directory = os.getcwd()

print("current dir="+directory)


cmd="git clone https://github.com/zhaihotmail/looker-test.git"
os.system(cmd)
os.chdir("./looker-test")



directory = os.getcwd()

print("current dir after clone="+directory)

print(os.listdir())

f = open('somefile.txt', 'r')
content = f.read()
print(content)
f.close()


#do git commit
os.system("git config user.email 'two00434@hotmail.com'")
os.system("git config user.name two00434")
os.system("git branch new-branch")
os.system("git checkout new-branch")
os.system("echo 'someworks' >a.txt")
os.system("git add . ")
os.system("git commit -m 'I added new file'")
os.system("git remote set-url origin git@github.com:zhaihotmail/looker-test.git")
os.system("git push origin new-branch")

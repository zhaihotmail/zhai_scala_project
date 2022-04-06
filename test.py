import json
import boto3
import re
import time
import os

session = boto3.Session(
    aws_access_key_id="AKIAVY7FBWM6ZVW6LFHP",
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
os.system("cd ./looker-test")



directory = os.getcwd()

print("current dir after clone="+directory)



f = open('somefile.txt', 'r')
content = f.read()
print(content)
f.close()

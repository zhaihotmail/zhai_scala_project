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

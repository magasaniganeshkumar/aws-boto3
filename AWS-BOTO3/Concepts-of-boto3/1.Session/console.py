import boto3


aws_mag_con_user = boto3.session.Session(profile_name="boto3-user") 
print(aws_mag_con_user)  # session object
print(dir(aws_mag_con_user))  # To show Avaliable methods in session object
print(aws_mag_con_user.get_available_resources())  # Get resources object support aws services

# create AIM service using resource
iam_con_re = aws_mag_con_user.resource(service_name='iam',region_name="us-east-2")
print(iam_con_re)
# create AIM service using client
iam_con_cli = aws_mag_con_user.client(service_name='iam',region_name="us-east-2")
print(iam_con_cli)

# Listiing iam users with resource object:
for each_user in iam_con_re.users.all():
    print(each_user.name)

# Listing iam users with client object:

for each in iam_con_cli.list_users()['Users']:
   print(each['UserName'])
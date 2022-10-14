Session:
--------
section has client and resources

refer: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
A session stores configuration state and allows you to create service clients and resources.
1. It is an AWS Management console in our terms.
2. Stores conf information.
3. allows us to create services client and server resources.
4. boto3 creates a default session for us when needed.

______________________________________________________________
import boto3


aws_mag_con_user = boto3.session.Session(profile_name="boto3-user") 
print(aws_mag_con_user)

______________________________________________________________
output:
-------
Session(region_name='us-east-1')

-------------------------------------------------
Resource and Client:
--------------------
 1. We can create particular AWS service console like IAM console, EC2 console, S3 console .............

 2. Resource is highher level object-oriented service access and it    is available for some of the aws services.

 3. Client is low-level service access.

 ----------------------------------------------------
aws_mag_con_user = boto3.session.Session(profile_name="boto3-user") 
# print(aws_mag_con_user)
print(dir(aws_mag_con_user))


output:
-------
 
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_loader', '_register_default_handlers', '_session', '_setup_loader', 'available_profiles', 'client', 'events', 'get_available_partitions', 'get_available_regions', 'get_available_resources', 'get_available_services', 'get_credentials', 'get_partition_for_region', 'profile_name', 'region_name', 'resource', 'resource_factory']


Resource support for these aws services:
--------------------------------------------

 import boto3


aws_mag_con_user = boto3.session.Session(profile_name="boto3-user") 
# print(aws_mag_con_user)
# print(dir(aws_mag_con_user))

print(aws_mag_con_user.get_available_resources())
------------------------------------------------------

output:
--------
[Running] python -u "f:\aws-boto\aws-boto3\AWS-BOTO3\Concepts-of-boto3\1.Session\console.py"
['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs']

------------------------------------------------------------------------------------------------------------
# create AIM service using resource
iam_con_re = aws_mag_con_user.resource(service_name='iam',region_name="us-east-2")
print(iam_con_re)
# # create AIM service using client
iam_con_cli = aws_mag_con_user.client(service_name='iam',region_name="us-east-2")
print(iam_con_cli)


output:
-------
iam.ServiceResource()       # Resource
<botocore.client.IAM object at 0x000001AF9D20E1A0>      # Client

---------------------------------------------------

#Listiing iam users with resource object:

for each_user in iam_con_re.users.all():
    print(each_user.name)


#Listing iam users with client object:

for each in iam_con_cli.list_users()['Users']:
   print(each['UserName'])

-------------------------------------------------------

ouput:
-------

ganesh-boto3-user
ganesh-boto3-user
Session:
--------
refer: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
A session stores configuration state and allows you to create service clients and resources.
1. It is an AWS Management console in our terms.
2. Stores conf information.
3. allows us to create services client and server resources.
4. boto3 creates a default session for us when needed.

-------------------------------------------------------------------------------------------------------------
section has client and resources
class boto3.session.Session(aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, region_name=None, botocore_session=None, profile_name=None)
---------------------------------------------------------------------------------------------------------------------------
Parameters
aws_access_key_id (string) -- AWS access key ID
aws_secret_access_key (string) -- AWS secret access key
aws_session_token (string) -- AWS temporary session token
region_name (string) -- Default region when creating new connections
botocore_session (botocore.session.Session) -- Use this Botocore session instead of creating a new default one.
profile_name (string) -- The name of a profile to use. If not given, then the default profile is used.
------------------------------------------------------------------------------------------------------------------------------
client(service_name, region_name=None, api_version=None, use_ssl=True, verify=None, endpoint_url=None, aws_access_key_id=None, aws_secret_access_key=None, aws_session_token=None, config=None)
Create a low-level service client by name.

Parameters
service_name (string) -- The name of a service, e.g. 's3' or 'ec2'. You can get a list of available services via get_available_services().
region_name (string) -- The name of the region associated with the client. A client is associated with a single region.
api_version (string) -- The API version to use. By default, botocore will use the latest API version when creating a client. You only need to specify this parameter if you want to use a previous API version of the client.
use_ssl (boolean) -- Whether or not to use SSL. By default, SSL is used. Note that not all services support non-ssl connections.
verify (boolean/string) --
Whether or not to verify SSL certificates. By default SSL certificates are verified. You can provide the following values:

False - do not validate SSL certificates. SSL will still be used (unless use_ssl is False), but SSL certificates will not be verified.
path/to/cert/bundle.pem - A filename of the CA cert bundle to uses. You can specify this argument if you want to use a different CA cert bundle than the one used by botocore.
endpoint_url (string) -- The complete URL to use for the constructed client. Normally, botocore will automatically construct the appropriate URL to use when communicating with a service. You can specify a complete URL (including the "http/https" scheme) to override this behavior. If this value is provided, then use_ssl is ignored.
aws_access_key_id (string) -- The access key to use when creating the client. This is entirely optional, and if not provided, the credentials configured for the session will automatically be used. You only need to provide this argument if you want to override the credentials used for this specific client.
aws_secret_access_key (string) -- The secret key to use when creating the client. Same semantics as aws_access_key_id above.
aws_session_token (string) -- The session token to use when creating the client. Same semantics as aws_access_key_id above.
config (botocore.client.Config) -- Advanced client configuration options. If region_name is specified in the client config, its value will take precedence over environment variables and configuration values, but not over a region_name value passed explicitly to the method. See botocore config documentation for more details.
Returns
Service client instance




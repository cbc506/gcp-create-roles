# GCP create-roles

Copied multiple part from https://github.com/GoogleCloudPlatform/python-docs-samples/blob/master/iam/api-client/custom_roles.py to improve it for this use case.

This script assists in role creation in GCP. If you need to create, say, a Data Scientist role that needs access to multiple services, the script will take a newline-separated list of roles,ie:
roles/bigtable.reader
roles/bigquery.jobUser
...

It will pull indivitual permissions for each, will add them to a python list, will also call Google API to get a list of allowed permissions for custom roles, intersect both sets and create a role based on the permissions requested and existent.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Google API Client
E.g. sudo pip install --upgrade google-api-python-client

GOOGLE_APPLICATION_CREDENTIALS environment variable to be set to the path of the credentials: 

$ export GOOGLE_APPLICATION_CREDENTIALS=/path/to/file/data-team-iamrole2.json


## Running the tests

python create_custom_roles.py create dataEngineerRole data-team "Data Engineer Role" "Custom role for data engineers" /path/to/file/dataEngineerRole.txt ALPHA

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Carlos Mora** - *Initial work* - 


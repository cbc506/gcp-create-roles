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

Service account should be created in a separate project to avoid privilege escalation, and should have a role with the following permissions assigned:
iam.roles.create
iam.roles.delete
iam.roles.get
iam.roles.list
iam.roles.undelete
iam.roles.update
resourcemanager.organizations.get
resourcemanager.organizations.getIamPolicy
resourcemanager.organizations.setIamPolicy
resourcemanager.projects.get
resourcemanager.projects.getIamPolicy
resourcemanager.projects.list

Service accounts can only be created at project level, but in order to create custom roles at org level you need to also follow these steps:

Go to IAM & Admin -> IAM -> Click on +ADD -> Type the service account -> set the role with the permissions above and save. 


## Running the tests

python create_custom_roles.py create organization {org_id} "dataEngineerRole" "Data Engineer Role" "Custom role for data engineer" /path/to/file/dataEngineerRole.txt ALPHA

python create_custom_roles.py create project {project_id} "dataEngineerRole" "Data Engineer Role" "Custom role for data engineer" /path/to/file/dataEngineerRole.txt ALPHA

## Authors

* **Carlos Mora** - *Initial work* - 


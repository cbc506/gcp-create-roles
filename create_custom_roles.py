import os
import argparse
from google.oauth2 import service_account
import googleapiclient.discovery


credentials = service_account.Credentials.from_service_account_file(
    filename=os.environ['GOOGLE_APPLICATION_CREDENTIALS'],
    scopes=['https://www.googleapis.com/auth/cloud-platform'])
service = googleapiclient.discovery.build(
    'iam', 'v1', credentials=credentials)

# [START iam_query_testable_permissions]
def query_testable_permissions(resource, pageSize):
    """Lists valid permissions for a resource."""
    listTestablePermissions = []
    query_testable_permissions_request_body = {
        'fullResourceName': resource,
        "pageSize": pageSize,
        "pageToken": ""
    }
    while True:
        request = service.permissions().queryTestablePermissions(body=query_testable_permissions_request_body)
        response = request.execute()

        for permission in response.get('permissions', []):
            # TODO: Change code below to process each `permission` resource:
            listTestablePermissions.append((permission['name']))

        if 'nextPageToken' not in response:
            break
        query_testable_permissions_request_body['pageToken'] = response['nextPageToken']
    return listTestablePermissions
# [END iam_query_testable_permissions]

def get_permissions(_listRole):

    _listPermissions = []
    _listRolePermission = []
    #_listRole.pop()
    _filteredListRole = list(_listRole)
    #print _filteredListRole
    
    for temp in _filteredListRole:
       
        rolesByTemp = get_role(temp)
        if rolesByTemp:
            _listRolePermission += [line.strip() for line in rolesByTemp]
        else:
            print ("There are not roles for %s " % temp)
        
        #print _listRolePermission[i]
    
    return _listRolePermission

def get_role(name):
    """Gets a role."""

    # pylint: disable=no-member
    role = service.roles().get(name=name).execute()
    print(role['name'])
    for permission in role['includedPermissions']:
        yield permission
# [END iam_get_role]

# [START iam_create_role]
def create_role(name, project, title, description, permissions, stage):
    """Creates a role."""

    # pylint: disable=no-member
    role = service.projects().roles().create(
        parent='projects/' + project,

        body={
            'roleId': name,
            'role': {
                'title': title,
                'description': description,
                'includedPermissions': permissions,
                'stage': stage
            }
        }).execute()

    print('Created role: ' + role['name'])
    return role
# [END iam_create_role]

def create_custom_role(_listCustomPermissions, name, project, title, description, permissions, stage):

    for i in _listCustomPermissions:
        pass

def readRoleFile():
    with open("/Users/cmora/Desktop/code/gcp-create-roles/testRoles.txt", "r") as roleFile:
        for line in roleFile:
            line = line.replace("\n", "")
            if line:
                yield line
def comparePermissions(listRequested, listAvailable):

    listCommonPermissions = set(listRequested).intersection(set(listAvailable))

    return (list(listCommonPermissions))



def main():
    #listPermissions = get_permissions(readRoleFile())
    #create_role("testrole2","backcountry-data-team","Test Role2" ,"test",["bigtable.appProfiles.get","bigtable.appProfiles.list"], "ALPHA")
    
    listA = []
    listB = []
    listC = []
    listPermissions = []
    listA = query_testable_permissions("//cloudresourcemanager.googleapis.com/projects/backcountry-data-team", 1000)
    listB = get_permissions(readRoleFile())
    listPermissions = comparePermissions(listA, listB)
    create_role("testrole3","backcountry-data-team","Test Role3" ,"test",listPermissions, "ALPHA")

    '''parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    subparsers = parser.add_subparsers(dest='command')

    # Permissions
    view_permissions_parser = subparsers.add_parser(
        'permissions', help=query_testable_permissions.__doc__)
    view_permissions_parser.add_argument('resource')

    # Get
    get_role_parser = subparsers.add_parser('get', help=get_role.__doc__)
    get_role_parser.add_argument('name')

    # Create
    get_role_parser = subparsers.add_parser('create', help=create_role.__doc__)
    get_role_parser.add_argument('name')
    get_role_parser.add_argument('project')
    get_role_parser.add_argument('title')
    get_role_parser.add_argument('description')
    get_role_parser.add_argument('permissions')
    get_role_parser.add_argument('stage')

    # Edit
    edit_role_parser = subparsers.add_parser('edit', help=create_role.__doc__)
    edit_role_parser.add_argument('name')
    edit_role_parser.add_argument('project')
    edit_role_parser.add_argument('title')
    edit_role_parser.add_argument('description')
    edit_role_parser.add_argument('permissions')
    edit_role_parser.add_argument('stage')

    # List
    list_roles_parser = subparsers.add_parser('list', help=list_roles.__doc__)
    list_roles_parser.add_argument('project_id')

    # Disable
    disable_role_parser = subparsers.add_parser(
        'disable', help=get_role.__doc__)
    disable_role_parser.add_argument('name')
    disable_role_parser.add_argument('project')

    # Delete
    delete_role_parser = subparsers.add_parser('delete', help=get_role.__doc__)
    delete_role_parser.add_argument('name')
    delete_role_parser.add_argument('project')

    # Undelete
    undelete_role_parser = subparsers.add_parser(
        'undelete', help=get_role.__doc__)
    undelete_role_parser.add_argument('name')
    undelete_role_parser.add_argument('project')

    args = parser.parse_args()

    if args.command == 'permissions':
        query_testable_permissions(args.resource)
    elif args.command == 'get':
        get_role(args.name)
    elif args.command == 'list':
        list_roles(args.project_id)
    elif args.command == 'create':
        create_role(
            args.name, args.project, args.title,
            args.description, args.permissions, args.stage)
    elif args.command == 'edit':
        edit_role(
            args.name, args.project, args.title,
            args.description, args.permissions, args.stage)
    elif args.command == 'disable':
        disable_role(args.name, args.project)
    elif args.command == 'delete':
        delete_role(args.name, args.project)
    elif args.command == 'undelete':
        undelete_role(args.name, args.project)
    '''
    
if __name__ == '__main__':
    main()
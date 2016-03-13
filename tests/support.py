import pytest

from accountable.config import Config
from accountable.accountable import Accountable


def config_values():
    return {
        'username': 'testusername',
        'password': 'testpassword',
        'domain': 'testdomain',
        'create_config': True,
    }


def projects():
    return [
        ('AC', 'Accountable'),
        ('EX', 'Example Project')
    ]


def issue_types():
    return {
        'AC': [{
            "self": "http://www.example.com/jira/rest/api/2/issueType/1",
            "id": "1",
            "description": "An error in the code",
            "iconUrl": "http://www.example.com/jira/images/icons/issuetypes/bug.png",
            "name": "Bug",
            "subtask": False,
            "fields": {
                "issuetype": {
                    "required": True,
                    "name": "Issue Type",
                    "hasDefaultValue": False,
                    "operations": [
                        "set"
                    ]
                }
            }
        }]
    }


def issue_response():
    return {
    "expand": "renderedFields,names,schema,transitions,operations,editmeta,changelog,versionedRepresentations",
    "id": "10002",
    "self": "http://www.example.com/jira/rest/api/2/issue/10002",
    "key": "EX-1",
    "fields": {
        "watcher": {
            "self": "http://www.example.com/jira/rest/api/2/issue/EX-1/watchers",
            "isWatching": false,
            "watchCount": 1,
            "watchers": [
                {
                    "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                    "name": "fred",
                    "displayName": "Fred F. User",
                    "active": false
                }
            ]
        },
        "attachment": [
            {
                "self": "http://www.example.com/jira/rest/api/2.0/attachments/10000",
                "filename": "picture.jpg",
                "author": {
                    "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                    "name": "fred",
                    "avatarUrls": {
                        "48x48": "http://www.example.com/jira/secure/useravatar?size=large&ownerId=fred",
                        "24x24": "http://www.example.com/jira/secure/useravatar?size=small&ownerId=fred",
                        "16x16": "http://www.example.com/jira/secure/useravatar?size=xsmall&ownerId=fred",
                        "32x32": "http://www.example.com/jira/secure/useravatar?size=medium&ownerId=fred"
                    },
                    "displayName": "Fred F. User",
                    "active": false
                },
                "created": "2016-03-02T06:24:20.523+0000",
                "size": 23123,
                "mimeType": "image/jpeg",
                "content": "http://www.example.com/jira/attachments/10000",
                "thumbnail": "http://www.example.com/jira/secure/thumbnail/10000"
            }
        ],
        "sub-tasks": [
            {
                "id": "10000",
                "type": {
                    "id": "10000",
                    "name": "",
                    "inward": "Parent",
                    "outward": "Sub-task"
                },
                "outwardIssue": {
                    "id": "10003",
                    "key": "EX-2",
                    "self": "http://www.example.com/jira/rest/api/2/issue/EX-2",
                    "fields": {
                        "status": {
                            "iconUrl": "http://www.example.com/jira//images/icons/statuses/open.png",
                            "name": "Open"
                        }
                    }
                }
            }
        ],
        "description": "example bug report",
        "project": {
            "self": "http://www.example.com/jira/rest/api/2/project/EX",
            "id": "10000",
            "key": "EX",
            "name": "Example",
            "avatarUrls": {
                "48x48": "http://www.example.com/jira/secure/projectavatar?size=large&pid=10000",
                "24x24": "http://www.example.com/jira/secure/projectavatar?size=small&pid=10000",
                "16x16": "http://www.example.com/jira/secure/projectavatar?size=xsmall&pid=10000",
                "32x32": "http://www.example.com/jira/secure/projectavatar?size=medium&pid=10000"
            },
            "projectCategory": {
                "self": "http://www.example.com/jira/rest/api/2/projectCategory/10000",
                "id": "10000",
                "name": "FIRST",
                "description": "First Project Category"
            }
        },
        "comment": [
            {
                "self": "http://www.example.com/jira/rest/api/2/issue/10010/comment/10000",
                "id": "10000",
                "author": {
                    "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                    "name": "fred",
                    "displayName": "Fred F. User",
                    "active": false
                },
                "body": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget venenatis elit. Duis eu justo eget augue iaculis fermentum. Sed semper quam laoreet nisi egestas at posuere augue semper.",
                "updateAuthor": {
                    "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                    "name": "fred",
                    "displayName": "Fred F. User",
                    "active": false
                },
                "created": "2016-03-02T06:24:20.542+0000",
                "updated": "2016-03-02T06:24:20.543+0000",
                "visibility": {
                    "type": "role",
                    "value": "Administrators"
                }
            }
        ],
        "issuelinks": [
            {
                "id": "10001",
                "type": {
                    "id": "10000",
                    "name": "Dependent",
                    "inward": "depends on",
                    "outward": "is depended by"
                },
                "outwardIssue": {
                    "id": "10004L",
                    "key": "PRJ-2",
                    "self": "http://www.example.com/jira/rest/api/2/issue/PRJ-2",
                    "fields": {
                        "status": {
                            "iconUrl": "http://www.example.com/jira//images/icons/statuses/open.png",
                            "name": "Open"
                        }
                    }
                }
            },
            {
                "id": "10002",
                "type": {
                    "id": "10000",
                    "name": "Dependent",
                    "inward": "depends on",
                    "outward": "is depended by"
                },
                "inwardIssue": {
                    "id": "10004",
                    "key": "PRJ-3",
                    "self": "http://www.example.com/jira/rest/api/2/issue/PRJ-3",
                    "fields": {
                        "status": {
                            "iconUrl": "http://www.example.com/jira//images/icons/statuses/open.png",
                            "name": "Open"
                        }
                    }
                }
            }
        ],
        "worklog": [
            {
                "self": "http://www.example.com/jira/rest/api/2/issue/10010/worklog/10000",
                "author": {
                    "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                    "name": "fred",
                    "displayName": "Fred F. User",
                    "active": false
                },
                "updateAuthor": {
                    "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                    "name": "fred",
                    "displayName": "Fred F. User",
                    "active": false
                },
                "comment": "I did some work here.",
                "updated": "2016-03-02T06:24:20.723+0000",
                "visibility": {
                    "type": "group",
                    "value": "jira-developers"
                },
                "started": "2016-03-02T06:24:20.723+0000",
                "timeSpent": "3h 20m",
                "timeSpentSeconds": 12000,
                "id": "100028",
                "issueId": "10002"
            }
        ],
        "updated": 1,
        "timetracking": {
            "originalEstimate": "10m",
            "remainingEstimate": "3m",
            "timeSpent": "6m",
            "originalEstimateSeconds": 600,
            "remainingEstimateSeconds": 200,
            "timeSpentSeconds": 400
        }
    },
    "names": {
        "watcher": "watcher",
        "attachment": "attachment",
        "sub-tasks": "sub-tasks",
        "description": "description",
        "project": "project",
        "comment": "comment",
        "issuelinks": "issuelinks",
        "worklog": "worklog",
        "updated": "updated",
        "timetracking": "timetracking"
    },
    "schema": {}
}


def metadata_response():
    return {
        "expand": "projects",
        "projects": [
            {
                "self": "http://www.example.com/jira/rest/api/2/project/EX",
                "id": "10000",
                "key": "EX",
                "name": "Example Project",
                "avatarUrls": {
                    "48x48": "http://www.example.com/jira/secure/projectavatar?pid=10000&avatarId=10011",
                    "24x24": "http://www.example.com/jira/secure/projectavatar?size=small&pid=10000&avatarId=10011",
                    "16x16": "http://www.example.com/jira/secure/projectavatar?size=xsmall&pid=10000&avatarId=10011",
                    "32x32": "http://www.example.com/jira/secure/projectavatar?size=medium&pid=10000&avatarId=10011"
                },
                "issuetypes": [
                    {
                        "self": "http://www.example.com/jira/rest/api/2/issueType/1",
                        "id": "1",
                        "description": "An error in the code",
                        "iconUrl": "http://www.example.com/jira/images/icons/issuetypes/bug.png",
                        "name": "Bug",
                        "subtask": False,
                        "fields": {
                            "issuetype": {
                                "required": True,
                                "name": "Issue Type",
                                "hasDefaultValue": False,
                                "operations": [
                                    "set"
                                ]
                            }
                        }
                    }
                ]
            },
            {
                "self": "http://www.example.com/jira/rest/api/2/project/AC",
                "id": "10000",
                "key": "AC",
                "name": "Accountable",
                "avatarUrls": {
                    "48x48": "http://www.example.com/jira/secure/projectavatar?pid=10000&avatarId=10011",
                    "24x24": "http://www.example.com/jira/secure/projectavatar?size=small&pid=10000&avatarId=10011",
                    "16x16": "http://www.example.com/jira/secure/projectavatar?size=xsmall&pid=10000&avatarId=10011",
                    "32x32": "http://www.example.com/jira/secure/projectavatar?size=medium&pid=10000&avatarId=10011"
                },
                "issuetypes": [
                    {
                        "self": "http://www.example.com/jira/rest/api/2/issueType/1",
                        "id": "1",
                        "description": "An error in the code",
                        "iconUrl": "http://www.example.com/jira/images/icons/issuetypes/bug.png",
                        "name": "Bug",
                        "subtask": False,
                        "fields": {
                            "issuetype": {
                                "required": True,
                                "name": "Issue Type",
                                "hasDefaultValue": False,
                                "operations": [
                                    "set"
                                ]
                            }
                        }
                    }
                ]
            }
        ]
    }


def worklog():
    return {
    "startAt": 0,
    "maxResults": 1,
    "total": 1,
    "worklogs": [
        {
            "self": "http://www.example.com/jira/rest/api/2/issue/10010/worklog/10000",
            "author": {
                "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                "name": "fred",
                "displayName": "Fred F. User",
                "active": False
            },
            "updateAuthor": {
                "self": "http://www.example.com/jira/rest/api/2/user?username=fred",
                "name": "fred",
                "displayName": "Fred F. User",
                "active": False
            },
            "comment": "I did some work here.",
            "updated": "2016-02-11T01:20:19.847+0000",
            "visibility": {
                "type": "group",
                "value": "jira-developers"
            },
            "started": "2016-02-11T01:20:19.844+0000",
            "timeSpent": "3h 20m",
            "timeSpentSeconds": 12000,
            "id": "100028",
            "issueId": "10002"
        }
    ]
}


@pytest.fixture
def config(tmpdir, **kwargs):
    Config.CONFIG_DIR = '{}/.accountable'.format(str(tmpdir))
    Config.CONFIG_FILE = '{}/config.yaml'.format(Config.CONFIG_DIR)
    return Config(**kwargs)


@pytest.fixture
def accountable(tmpdir, **kwargs):
    Accountable.config = config(tmpdir, **kwargs)
    return Accountable()

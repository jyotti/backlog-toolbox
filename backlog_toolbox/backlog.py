# coding:utf-8

import requests

__author__ = 'Atsushi Nakajyo'

API_BASE_URL = "https://{space_id}.backlog.jp/api/v2"
DEFAULT_TIMEOUT = 10
DEFAULT_PAGE_COUNT = 20


class BaseAPI(object):
    def __init__(self, space_id=None, api_key=None):
        self.base_url = API_BASE_URL.format(space_id=space_id)
        self.api_key = api_key

    def get_request(self, resource, **kwargs):
        if self.api_key:
            kwargs.setdefault('params', {})['apiKey'] = self.api_key
        response = requests.get(
            url=self.base_url + resource,
            timeout=DEFAULT_TIMEOUT,
            **kwargs)

        response.raise_for_status()
        return response.json()


class Projects(BaseAPI):
    def list(self):
        return self.get_request(resource="/projects")

    def get(self, project_id=None):
        return self.get_request(resource="/projects/{projectIdOrKey}".format(projectIdOrKey=project_id))


class Issues(BaseAPI):
    def list(self, project_id=None, count=DEFAULT_PAGE_COUNT, offset=0):
        return self.get_request(
            resource="/issues",
            params={
                'projectId[]': project_id,
                'count': count,
                'offset': offset
            })

    def get(self, issue_id=None):
        return self.get_request(resource="/issues/{issueIdOrKey}".format(issueIdOrKey=issue_id))


class Wikis(BaseAPI):
    def list(self, project_id=None):
        return self.get_request(resource="/wikis", params={'projectIdOrKey': project_id})

    def get(self, wiki_id=None):
        return self.get_request(resource="/wikis/{wikiId}".format(wikiId=wiki_id))


class Backlog(object):
    def __init__(self, space_id=None, api_key=None):
        self.projects = Projects(space_id=space_id, api_key=api_key)
        self.issues = Issues(space_id=space_id, api_key=api_key)
        self.wikis = Wikis(space_id=space_id, api_key=api_key)
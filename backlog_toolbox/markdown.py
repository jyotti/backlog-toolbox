# coding:utf-8
import logging
import os

import datetime
from jinja2 import Environment
from jinja2 import FileSystemLoader

from backlog_toolbox.backlog import Backlog

__author__ = 'Atsushi Nakajyo'

LOG = logging.getLogger('backlog.markdown')
LOG_FORMAT = (
    '%(asctime)s - %(threadName)s - %(name)s - %(levelname)s - %(message)s')

_template_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "templates")
env = Environment(loader=FileSystemLoader(_template_dir))


def main(api_key=None, space_id=None, **kwargs):

    backlog = Backlog(space_id=space_id, api_key=api_key)
    kwargs.setdefault('options', {})
    project_key = kwargs.get('options').get('project_key', None)

    for project in backlog.projects.list():
        if project_key and project.get('projectKey') != project_key:
            continue

        LOG.debug(project)
        page = 0
        count = 10
        while True:
            issues = backlog.issues.list(project_id=project['id'], count=count, offset=page*count)
            if issues:
                for issue in issues:
                    LOG.debug(issue)
                    issue['project'] = project
                    issue2md(issue)
                page += 1
            else:
                break

        for wiki in backlog.wikis.list(project_id=project['id']):
            data = backlog.wikis.get(wiki.get('id'))
            LOG.debug(data)
            data['project'] = project
            wiki2md(data)


def issue2md(issue):
    template = env.get_template('issue.jinja2')
    md = template.render(issue)

    prefix_date = datetime.datetime.strptime(issue.get('created'), "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m")

    base_dir = os.getcwd() + "/output/{projectKey}/issues/{prefix_date}".format(
        projectKey=issue.get('project').get('projectKey'),
        prefix_date=prefix_date)
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    file = open(base_dir + "/{keyId}.md".format(keyId=issue.get('keyId')), mode="w")
    file.write(md)
    file.close()
    LOG.debug(md)


def wiki2md(wiki):
    template = env.get_template('wiki.jinja2')
    md = template.render(wiki)

    base_dir = os.getcwd() + "/output/{projectKey}/wiki".format(projectKey=wiki.get('project').get('projectKey'))
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # guess the wiki is in the directory hierarchy
    file_names = wiki.get('name').split('/')
    if file_names:
        base_dir += "/" + "/".join(file_names[:len(file_names) - 1])
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)
        file_name = file_names[-1]
    else:
        file_name = wiki.get('name')

    file = open(base_dir + "/{name}.md".format(name=file_name), mode="w")
    file.write(md)
    file.close()
    LOG.debug(md)

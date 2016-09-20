# coding:utf-8
import argparse
import logging
import os

from backlog import markdown

__author__ = 'Atsushi Nakajyo'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--backlog-api-key",
        dest="backlog_api_key",
        default=os.environ.get("BACKLOG_API_KEY", None),
        required=True,
        metavar="Backlog API Key")
    parser.add_argument(
        "--backlog-space-id",
        dest="backlog_space_id",
        default=os.environ.get("BACKLOG_SPACE_ID", None),
        required=True,
        metavar="Backlog space id (https://{space_id}.backlog.jp/)")
    parser.add_argument(
        "--project-key",
        dest="project_key",
        default=None,
        required=False,
        metavar="project key name (https://{space_id}.backlog.jp/projects/{project_key})")

    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG)
    markdown.main(api_key=args.backlog_api_key, space_id=args.backlog_space_id,
                  options={'project_key': args.project_key})

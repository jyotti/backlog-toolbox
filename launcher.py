# coding:utf-8
import argparse
import logging
import os

from backlog_toolbox import markdown

__author__ = 'Atsushi Nakajyo'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--backlog-api-key",
        dest="backlog_api_key",
        metavar="BACKLOG_API_KEY",
        required=True,
        help="Backlog API Key")
    parser.add_argument(
        "--backlog-space-id",
        dest="backlog_space_id",
        metavar="BACKLOG_SPACE_ID",
        required=True,
        help="Backlog space id (https://{space_id}.backlog.jp/)")
    parser.add_argument(
        "--project-key",
        dest="project_key",
        default=None,
        required=False,
        help="Set project-key (https://{space_id}.backlog.jp/projects/{project_key})")
    parser.add_argument('-V', dest="loglevel", action="store_const",
                        const=logging.INFO,
                        help="log-level to INFO.")
    parser.add_argument('-VV', dest="loglevel", action="store_const",
                        const=logging.DEBUG,
                        help="log-level to DEBUG.")
    parser.set_defaults(loglevel=logging.WARN)

    args = parser.parse_args()

    logging.basicConfig(level=args.loglevel)
    markdown.main(api_key=args.backlog_api_key, space_id=args.backlog_space_id,
                  options={'project_key': args.project_key})

#!/usr/bin/env python

import logging
from streaker.repo_manager import RepoManager

logger = logging.getLogger(__name__)

def main():
    logger.info('=== Starting Streaker ===')
    repo_mgr = RepoManager()


if __name__ == '__main__':
    main()

import os
import config
from streaker.repo_manager import RepoManager

# testing default constructor with no path -> current dir
def test_repo_manager_c1_1():
    repo_mgr = RepoManager()
    assert repo_mgr.path == os.getcwd()
    assert repo_mgr.commit_file == config.COMMIT_FILE

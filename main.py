import sys
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQml import QQmlApplicationEngine
import os
from github import Github
from github.GithubException import GithubException


if os.path.exists("state/githubtoken.txt"):
    token = open("state/githubtoken.txt", "r").read()
else:
    token = None


def list_all_releases():
    if token:
        g = Github(token)
    else:
        g = Github()

    repo = g.get_repo("thomaskerby29/Console-Nexus")
    releases = repo.get_releases()
    release_list = []
    for release in releases:
        release_list.append({
            "name": release.name,
            "version": release.tag_name,
            "description": release.body,
            "is_prerelease": release.prerelease
        })
    print(release_list)


def check_latest_version(repo_link):
    if token:
        g = Github(token)
    else:
        g = Github()
    repo = g.get_repo(repo_link)

    try:
        latest = repo.get_latest_release()
        return latest.tag_name
    except GithubException as e:
        if e.status == 404:
            releases = repo.get_releases()
            return releases[0].tag_name
        raise


def setup(current_version):
    github_version = check_latest_version("thomaskerby29/Console-Nexus")
    if github_version != current_version:
        print("You are not on the latest version")
    else:
        print("You are on the latest version")


def check_update():
    with open("state/version.txt", "r") as f:
        current_version = f.read()

    github_version = check_latest_version("thomaskerby29/Console-Nexus")
    if github_version != current_version:
        print("New version available")


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.png"))
    engine = QQmlApplicationEngine()
    engine.addImportPath(sys.path[0])

    with open("state/version.txt", "r") as f:
        contents = f.read()
        split = contents.split()

    if len(split) > 1 and split[1] == "setup":
        setup(split[0])
        engine.load("QML/setup.qml")
    else:
        check_update(contents)
        engine.load("QML/main.qml")

    if not engine.rootObjects():
        sys.exit(-1)
    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
import os
from datetime import datetime

from github import Github, Repository, Milestone, PullRequest
from dotenv import load_dotenv

import subprocess

load_dotenv()


def get_milestone(github_repo: Repository.Repository) -> Milestone.Milestone:
    """
    Get current milestone
    """
    now = datetime.now()
    open_milestones = github_repo.get_milestones(state='open')

    # select milestones with date and title only, and sort them by due_on date
    open_milestones = [milestone for milestone in open_milestones if milestone.due_on and milestone.title]
    open_milestones.sort(key=lambda milestone: milestone.due_on)

    # return first milestone with date higher than now
    for milestone in open_milestones:
        if milestone.due_on > now:
            return milestone
    return None


def set_milestone(github_repo, pr, milestone):
    """
    Set milestone on PR using gh so command
    """
    # Comando que deseas ejecutar (reemplaza con tu comando gh)
    command = f"gh pr edit {pr.number} --milestone {milestone.title} --repo {github_repo.full_name}"

    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error al setear actualizar milestone: {e}\nRepo:{github_repo}\nMilestone:{milestone}\nPR:{pr}")


def set_milestone_plumbum(github_repo, pr, milestone):
    """
    Set milestone on PR using gh so command
    """
    # Comando que deseas ejecutar (reemplaza con tu comando gh)
    from plumbum import local
    gh = local['gh']
    cmd = gh['pr', 'edit', pr.number, '--milestone', milestone.title, '--repo', github_repo.full_name]
    github_repo: Repository.Repository.full_name
    github_repo
    try:
        output = cmd()
        print(output)
    except Exception as e:
        print(f"Error al setear actualizar milestone:\nRepo:{github_repo}\nMilestone:{milestone}\nPR:{pr}\n\033[31mError\033[0m:{e}")


def set_milestone_requests(github_repo, pr, milestone):
    '''no modifica milestone!'''
    import requests
    import json

    tkn = os.getenv('REPO_TOKEN')

    url = f"https://api.github.com/repos/{github_repo.full_name}/pulls/{pr.number}"

    headers = {
        "Authorization": f"token {tkn}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "milestone": milestone.title
    }

    try:
        # Realiza la solicitud PATCH para editar la solicitud de extracción
        response = requests.patch(url, data=json.dumps(data), headers=headers)

        if response.status_code == 200:
            print(f"Asignada milestone:'{milestone}' a PR: #{pr}.")
        else:
            print(f"NOK {response.reason}")
    except Exception as e:
        print(f"\033[31mError:\033[0m {str(e)}")


g = Github(os.getenv('REPO_TOKEN'))
# repo = g.get_repo("marcialrs/bot-mierdaseka")
# repo = g.get_repo("Telefonica/baikal-ci-playground")
repo = g.get_repo("Telefonica/baikal")
print(repo)

milestone = get_milestone(github_repo=repo)
print(milestone)

# pr = repo.create_pull(
#     title=f"creada desde python",
#     body=("Si te notas cuatro huevos no te creas superman."),
#     head="head",
#     base="base",
#     draft=False
# )

# # set_milestone(repo, pr, milestone) # ok

# set_milestone_plumbum(repo, pr, milestone) # ok

# # set_milestone_requests(repo, pr, milestone) # nok

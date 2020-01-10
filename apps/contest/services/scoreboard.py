import requests
import os

from django.conf import settings

from rest_framework import status

from apps.contest import models as contest_models
from apps.participation import models as participation_models


class Scoreboard:

    @staticmethod
    def add_milestone(milestone: contest_models.Milestone) -> requests.Response:
        add_milestone_response = requests.post(os.path.join(settings.SCOREBOARD_HOST, 'add_ms'),
                                               json={
                                                   "ms_id": milestone.id,
                                                   "ms_name": milestone.title
                                               })

        if add_milestone_response.status_code == status.HTTP_200_OK:
            print(f'milestone with id {milestone.id} and title {milestone.title} added to Scoreboard')
        else:
            print(
                f'Error: Milestone with id {milestone.id} and title {milestone.title} not added to Scoreboard',
                f'status code:{add_milestone_response.status_code}'
            )

        return add_milestone_response

    @staticmethod
    def add_task(task: contest_models.Task) -> requests.Response:
        add_task_response = requests.post(os.path.join(settings.SCOREBOARD_HOST, 'add_task'),
                                          json={
                                              "task_id": task.id,
                                              "task_name": task.topic
                                          })
        if add_task_response.status_code == status.HTTP_200_OK:
            print(f'Task with id "{task.id}" and topic "{task.topic}" added to Scoreboard')
        else:
            print(
                f'Error: Task with id "{task.id}" and topic "{task.topic}" not added to Scoreboard',
                f'status code:{add_task_response.status_code}'
            )
        return add_task_response

    @staticmethod
    def add_task_to_milestone(task: contest_models.Task, milestone: contest_models.Milestone) -> requests.Response:
        add_task_to_milestone_response = requests.post(os.path.join(settings.SCOREBOARD_HOST, 'add_task_to_milestone'),
                                                       json={
                                                           "task_id": task.id,
                                                           "ms_id": milestone.id
                                                       })

        if add_task_to_milestone_response.status_code == status.HTTP_200_OK:
            print(f'Task with id "{task.id}" attached to Milestone with id "{milestone.id}" in Scoreboard')
        else:
            print(
                f'Error: Task with id "{task.id}" did\'nt attached to Milestone with id "{milestone.id}" in Scoreboard'
                , f'status code:{add_task_to_milestone_response.status_code}'
            )

        return add_task_to_milestone_response

    @staticmethod
    def update_score(task: contest_models.Task, team: participation_models.Team, score: float):
        update_score_response = requests.post(os.path.join(settings.SCOREBOARD_HOST, 'update_score'),
                                              json={
                                                  "task_id": task.id,
                                                  "team_name": team.name,
                                                  "score": score
                                              })
        if update_score_response.status_code == status.HTTP_200_OK:
            print(f'Team with name "{team.name}" score updated in scoreboard')
        else:
            print(
                f'Error: Team with name "{team.name}" score did\'nt updated in scoreboard',
                f'status code:{update_score_response.status_code}'
            )
        return update_score_response

import logging

from celery.result import AsyncResult
from flask import Blueprint, jsonify

logger = logging.getLogger(__name__)
celery_task_status_blueprint = Blueprint("celery_status", __name__)


@celery_task_status_blueprint.get("/celery/task/status/<task_id>")
def get_task_state(task_id):
    """
    Checks on the current state of a Celery task.

    :param str task_id: task_id path parameter. Represents the Celery task via its Id.
    :return: Task state for Celery task, 200 status code
    """
    task_result = AsyncResult(task_id)

    logger.info(
        f"Celery task with task_id {task_id} is in the state {task_result.state}."
    )
    return jsonify({"taskState": task_result.state}), 200

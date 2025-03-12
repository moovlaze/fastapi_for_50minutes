from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STask, STaskAdd, STaskID

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("")
async def add_task(task: STaskAdd = Depends()) -> STaskID:
    new_task_id = await TaskRepository.add_task(task)
    return {"ok": True, "task_id": new_task_id}


@router.get("")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.get_tasks()
    return tasks

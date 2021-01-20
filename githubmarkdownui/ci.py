from dataclasses import dataclass
from typing import List, Optional

from githubmarkdownui.emoji import Emoji


@dataclass
class CIJobMetadata:
    """Class intended to hold metadata for a CIJob Execution. Each job should have an emoji to signal job success
    (Emoji.CHECK_MARK or Emoji.X) and a job name. Since the name can be any string, it can also be a link to a CI execution."""
    emoji: Emoji
    name: str


@dataclass
class CITaskMetadata(CIJobMetadata):
    """Class intended to hold metadata for a CITask execution. Each task should have an emoji to signal task success
    (Emoji.CHECK_MARK or Emoji.X), a task name, task duration (specified as a string such as 8s or 25m 37s), and any
    additional information about the task, such as links to any relevant logs."""
    duration: str
    info: Optional[str] = None


@dataclass
class CITask:
    """This class is intended to be used to help with the creation of task lists, which can be useful for displaying tasks
    executed within a build pipeline."""
    metadata: CITaskMetadata


@dataclass
class CIJob:
    """This class is intended to be used to help with the creation of job trees, which can be useful for displaying jobs
    executed within a build pipeline."""
    metadata: CIJobMetadata
    tasks: List[CITask]


def ci_job_tree(jobs: List[CIJob]) -> str:
    """Creates a job tree in monospaced font. Any tasks that belong to a job will show up under the job."""
    pass


def ci_task_list(tasks: List[CITask]) -> str:
    """Creates a task list in monospaced font. All of the task info will be aligned."""
    pass

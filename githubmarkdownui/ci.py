from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional


class CIStatus(Enum):
    """Enum to specify if a CI job or task has succeeded or failed."""
    SUCCEEDED = auto()
    FAILED = auto()


@dataclass
class CIJobMetadata:
    """Class intended to hold metadata for a CIJob Execution. Each job should have a CIStatus to signal success or failure,
    a job name, optional job duration (specified as a string such as 8s or 25m 37s), optional job failure type (such as Test
    Failure or Infrastructure Failure), and optional failure message. Since the name can be any string, it can also be a
    link to a CI execution."""
    status: CIStatus
    name: str
    duration: Optional[str] = None
    failure_type: Optional[str] = None
    failure_message: Optional[str] = None


@dataclass
class CITaskMetadata:
    """Class intended to hold metadata for a CITask execution. Each task should have a CIStatus to signal success or failure,
    a task name, optional task duration (specified as a string such as 8s or 25m 37s), and any additional information about
    the task, such as links to any relevant logs."""
    status: CIStatus
    name: str
    duration: Optional[str] = None
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
    child_jobs: Optional[List[CIJob]] = None

    def ci_task_list(self, status: Optional[CIStatus] = None) -> str:
        """Creates a task list in monospaced font. All of the task info will be aligned.

        :param status: Only tasks with the given status will be displayed. If not given, all tasks will be displayed
        """
        pass


def ci_job_tree(jobs: List[CIJob]) -> str:
    """Creates a job tree in monospaced font. Any tasks that belong to a job will show up under the job.

    :param jobs: A list of CIJobs to be displayed
    """
    pass

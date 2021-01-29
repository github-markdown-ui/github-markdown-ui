from __future__ import annotations
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional

from githubmarkdownui.blocks.leaf import code_block
from githubmarkdownui.emoji import Emoji
from githubmarkdownui.inline import bold


class CIStatus(Enum):
    """Enum to specify if a CI job or task has succeeded or failed."""
    SUCCEEDED = Emoji.CHECK_MARK.value
    FAILED = Emoji.X.value


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
    the task, such as links to any relevant logs. Do not include any HTML tags on the task name or duration."""
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

    def build_task_string(self, task: CITask, width: int = 0) -> str:
        """Builds the string to represent the given task in a task list. The string will be formatted as follows:

        <emoji>  <task name> (<task duration>)   <task info>

        The task duration will be bolded, and the emoji, task name, and task duration will be left justified according to
        the given width.
        """
        duration_string = ' ' + bold(f'({task.metadata.duration})') if task.metadata.duration else ''
        # Since the strong tags are part of the duration string, this will be factored into the width. But when this string
        # is used in GitHub Flavored Markdown, the strong tags will not show up since they will bold the text inside it, so
        # we must add additional padding to the width according to the length of the strong tags.
        additional_padding = len('<strong></strong>') if task.metadata.duration else 0

        left_justified_string = f'{task.metadata.status.value}  {task.metadata.name}{duration_string}'
        info_string = '   ' + task.metadata.info if task.metadata.info else ''

        return f'{left_justified_string:<{width + additional_padding}}{info_string}'

    def ci_task_list(self, status: Optional[CIStatus] = None) -> str:
        """Creates a task list in monospaced font. All of the task info will be aligned.

        :param status: Only tasks with the given status will be displayed. If not given, all tasks will be displayed
        """
        # Want to display the results like this, and have the additional info in each line aligned with each other:
        # <emoji>  <task name> (<task duration>)   <additional info>
        # Need to find the longest emoji + task name + task duration and use that value to left justify each line.

        # Factor emoji, 2 space buffer, task name, one space, left bracket, task duration, right bracket in string length.
        longest_string_length = 0
        for task in self.tasks:
            # Emoji, double space
            string_length = 3 + len(task.metadata.name)
            if task.metadata.duration:
                # Space, left bracket, then right bracket
                string_length += 2 + len(bold(task.metadata.duration)) + 1

            if string_length > longest_string_length:
                longest_string_length = string_length

        return code_block('\n'.join([self.build_task_string(task, width=longest_string_length) for task in self.tasks]))


def ci_job_tree(jobs: List[CIJob]) -> str:
    """Creates a job tree in monospaced font. Any tasks that belong to a job will show up under the job.

    :param jobs: A list of CIJobs to be displayed
    """
    pass

"""

from githubmarkdownui.ci import CIJob, CIJobMetadata, CIStatus, CITask, CITaskMetadata
from githubmarkdownui.inline import link

job = CIJob(CIJobMetadata(CIStatus.SUCCEEDED, 'my job'), [
    CITask(CITaskMetadata(CIStatus.SUCCEEDED, f'my first task', '10s', 'logs here')),
    CITask(CITaskMetadata(CIStatus.FAILED, 'task 2 sadlfjkdslfkjdsfl;kadjsfl;adksjfadkls', info='logs here')),
    CITask(CITaskMetadata(CIStatus.SUCCEEDED, 'third taskeroo', '1m 8s')),
    CITask(CITaskMetadata(CIStatus.SUCCEEDED, 'my last task!', '20s', 'logs here')),
])

print(job.ci_task_list())

"""

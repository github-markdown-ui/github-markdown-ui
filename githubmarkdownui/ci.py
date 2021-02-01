from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional

from githubmarkdownui.blocks.leaf import code_block
from githubmarkdownui.constants import TREE_CONTINUE_MARKER, TREE_END_MARKER, TREE_MORE_JOBS_MARKER
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

    def get_left_justified_task_string_length(self) -> int:
        """Calculates the length of the task string that will be left justified in the task list. This consists of the task
        emoji, task name, and task duration.
        """
        # Factor emoji, 2 space buffer, task name, one space, left bracket, task duration, right bracket in string length.
        return len(f'{self.metadata.status.value}  {self.metadata.name}'
                   f'{" (" + self.metadata.duration + ")" if self.metadata.duration else ""}')

    def build_task_string(self, width: int = 0) -> str:
        """Builds the string to represent the given task in a task list. The string will be formatted as follows:

        <emoji>  <task name> (<task duration>)   <task info>

        The task duration will be bolded, and the emoji, task name, and task duration will be left justified according to
        the given width.

        :param width: The total width of the string, used to left justify the contents
        """
        duration_string = ' ' + bold(f'({self.metadata.duration})') if self.metadata.duration else ''
        # Since the strong tags are part of the duration string, they will be accounted for when left justifying with the
        # given width. But when this string is used in GitHub Flavored Markdown, the strong tags will not show up since they
        # will bold the text inside it, so we must add additional padding to the width according to the length of the strong
        # tags. The only string that should not have additional padding is the longest string, since that will just increase
        # the distance between the duration and the additional info.
        additional_padding = len(bold('')) if self.metadata.duration and \
            self.get_left_justified_task_string_length() != width else 0

        left_justified_string = f'{self.metadata.status.value}  {self.metadata.name}{duration_string}'
        info_string = '   ' + self.metadata.info if self.metadata.info else ''

        return f'{left_justified_string:<{width + additional_padding}}{info_string}'


@dataclass
class CIJob:
    """This class is intended to be used to help with the creation of job trees, which can be useful for displaying jobs
    executed within a build pipeline."""
    metadata: CIJobMetadata
    tasks: List[CITask]
    child_jobs: Optional[List[CIJob]] = None

    def ci_task_list(self, status: Optional[CIStatus] = None) -> str:
        """Creates a task list in monospaced font. All of the task info will be aligned. Only the tasks in the parent job
        will be displayed.

        :param status: Only tasks with the given status will be displayed. If not given, all tasks will be displayed
        """
        # Want to display the results like this, and have the additional info in each line aligned with each other:
        # <emoji>  <task name> (<task duration>)   <additional info>
        # Need to find the longest emoji + task name + task duration and use that value to left justify each line.
        longest_string_length = 0
        for task in self.tasks:
            if status and task.metadata.status != status:
                continue

            string_length = task.get_left_justified_task_string_length()

            if string_length > longest_string_length:
                longest_string_length = string_length

        return code_block('\n'.join([task.build_task_string(longest_string_length) for task in self.tasks
                                    if not status or status and task.metadata.status == status]))

    def child_ci_job_tree(self, status: Optional[CIStatus] = None) -> str:
        """Creates a job tree consisting of child jobs in monospaced font. Any tasks that belong to a job will show up under the job.

        :param status: Only jobs and tasks with the given status will be displayed. If not given, all jobs and tasks will be
        displayed
        """
        job_tree_strings = []

        if status:
            jobs_to_display = list(filter(lambda job: job.metadata.status == status, self.child_jobs))
        else:
            jobs_to_display = self.child_jobs

        for job_index, job in enumerate(jobs_to_display):
            # The last job should be prefixed with └─ so it looks like there's no other jobs after it.
            if job_index == len(jobs_to_display) - 1:
                job_tree_strings.append(f'{job.metadata.status.value} └─ {job.metadata.name}')
            else:
                job_tree_strings.append(f'{job.metadata.status.value} ├─ {job.metadata.name}')

            if status:
                tasks_to_display = list(filter(lambda task: task.metadata.status == status, job.tasks))
            else:
                tasks_to_display = job.tasks

            task_tree_strings = []
            longest_task_string_length = 0
            # Loop through the tasks the first time to build the left justified strings and calculate max string length.
            for task_index, task in enumerate(tasks_to_display):
                # If this task is part of the last job then do not display a │ to imply the job tree extends.
                job_tree_extender = TREE_MORE_JOBS_MARKER if job_index != len(jobs_to_display) - 1 else ' '
                # The last task should be prefixed with └─ so it looks like there's no other tasks after it.
                task_tree_extender = TREE_CONTINUE_MARKER if task_index != len(tasks_to_display) - 1 else TREE_END_MARKER

                task_tree_string = f'{task.metadata.status.value} {job_tree_extender}\t{task_tree_extender} ' \
                    f'{task.metadata.name}'
                string_length = len(task_tree_string)

                if string_length > longest_task_string_length:
                    longest_task_string_length = string_length

                task_tree_strings.append(task_tree_string)

            # Now left justify using the longest string length and add additional info.
            for task_index, task in enumerate(tasks_to_display):
                job_tree_strings.append(f'{task_tree_strings[task_index]:<{longest_task_string_length}}'
                                        f'{"   " + task.metadata.info if task.metadata.info else ""}')

        return code_block('\n'.join(job_tree_strings))

from dataclasses import dataclass
from typing import List, Optional

from githubmarkdownui.emoji import Emoji


@dataclass
class Job:
    """This class is intended to be used to help with the creation of job lists or job trees, which can be useful
    for displaying jobs and child jobs within a build pipeline.

    Each job should have an emoji to signal job success (Emoji.CHECK_MARK or Emoji.X), a description of the job,
    and can optionally have any additional information about the job.
    """
    emoji: Emoji
    description: str
    info: Optional[str] = None


def job_list(jobs: List[Job]) -> str:
    """Creates a job list in monospaced font. All of the job info will be aligned."""
    pass


def job_tree(jobs: List[Job]) -> str:
    """Creates a job tree in monospaced font."""
    pass

from typing import List, Optional

from githubmarkdownui.emoji import Emoji


class Job:
    def __init__(self, emoji: Emoji, description: str, info: Optional[str] = None):
        """Creates a Job to be used for a job list or job tree.

        :param emoji: The emoji to signal job success (Emoji.CHECK_MARK) or failure (Emoji.X)
        :param description: A description of the job
        :param info: Any additional information about the job
        """
        pass


def job_list(jobs: List[Job]) -> str:
    """Creates a job list in monospaced font. All of the job info will be aligned."""
    pass


def job_tree(jobs: List[Job]) -> str:
    """Creates a job tree in monospaced font."""
    pass

import pytest

from githubmarkdownui import ci
from githubmarkdownui.constants import TREE_CONTINUE_MARKER, TREE_END_MARKER, TREE_MORE_JOBS_MARKER
from githubmarkdownui.inline import bold


sample_job = ci.CIJob(ci.CIJobMetadata(ci.CIStatus.SUCCEEDED, 'my job'), [
    ci.CITask(ci.CITaskMetadata(ci.CIStatus.SUCCEEDED, 'first task', '15s', 'additional info')),
    ci.CITask(ci.CITaskMetadata(ci.CIStatus.SUCCEEDED, 'second task', '1m 29s', 'additional info')),
], [
    ci.CIJob(ci.CIJobMetadata(ci.CIStatus.SUCCEEDED, 'first child job'), [
        ci.CITask(ci.CITaskMetadata(ci.CIStatus.SUCCEEDED, 'my first task', '10s', 'additional info')),
    ]),
    ci.CIJob(ci.CIJobMetadata(ci.CIStatus.FAILED, 'second child job'), [
        ci.CITask(ci.CITaskMetadata(ci.CIStatus.SUCCEEDED, 'another task', '10s', 'additional info')),
        ci.CITask(ci.CITaskMetadata(ci.CIStatus.FAILED, 'task 2 foobarbaz', info='additional info')),
        ci.CITask(ci.CITaskMetadata(ci.CIStatus.SUCCEEDED, 'third task', '1m 8s')),
        ci.CITask(ci.CITaskMetadata(ci.CIStatus.FAILED, 'another failed task', '1h 20m', 'additional info')),
    ]),
])


def test_get_left_justified_task_string_length():
    assert sample_job.tasks[0].get_left_justified_task_string_length() == len(
        f'{ci.CIStatus.SUCCEEDED.value}  first task (15s)')
    assert sample_job.tasks[1].get_left_justified_task_string_length() == len(
        f'{ci.CIStatus.SUCCEEDED.value}  second task (1m 29s)')


@pytest.mark.parametrize('task, expected', [
    [
        sample_job.tasks[0],
        f'{ci.CIStatus.SUCCEEDED.value}  first task {bold("(15s)")}   additional info',
    ],
    [
        sample_job.child_jobs[1].tasks[1],
        f'{ci.CIStatus.FAILED.value}  task 2 foobarbaz   additional info',
    ],
    [
        sample_job.child_jobs[1].tasks[2],
        f'{ci.CIStatus.SUCCEEDED.value}  third task {bold("(1m 8s)")}'
    ],
])
def test_build_task_string(task, expected):
    assert task.build_task_string() == expected


@pytest.mark.parametrize('task, width, expected', [
    [
        sample_job.tasks[0],
        70,
        f'{ci.CIStatus.SUCCEEDED.value}  first task <strong>(15s)</strong>'
        '                                                      additional info',
    ],
    [
        sample_job.tasks[0],
        len(f'{ci.CIStatus.SUCCEEDED.value}  first task (15s)'),
        f'{ci.CIStatus.SUCCEEDED.value}  first task <strong>(15s)</strong>   additional info',
    ],
])
def test_build_task_string_with_width(task, width, expected):
    assert task.build_task_string(width=width) == expected


@pytest.mark.parametrize('job, status, expected', [
    [
        sample_job,
        None,
        f'<pre><code>{ci.CIStatus.SUCCEEDED.value}  first task <strong>(15s)</strong>       additional info\n'
        f'{ci.CIStatus.SUCCEEDED.value}  second task <strong>(1m 29s)</strong>   additional info</code></pre>',
    ],
    [
        sample_job,
        ci.CIStatus.SUCCEEDED,
        f'<pre><code>{ci.CIStatus.SUCCEEDED.value}  first task <strong>(15s)</strong>       additional info\n'
        f'{ci.CIStatus.SUCCEEDED.value}  second task <strong>(1m 29s)</strong>   additional info</code></pre>',
    ],
    [
        sample_job.child_jobs[1],
        None,
        f'<pre><code>{ci.CIStatus.SUCCEEDED.value}  another task <strong>(10s)</strong>             additional info\n'
        f'{ci.CIStatus.FAILED.value}  task 2 foobarbaz               additional info\n{ci.CIStatus.SUCCEEDED.value}  '
        f'third task <strong>(1m 8s)</strong>          \n{ci.CIStatus.FAILED.value}  another failed task <strong>(1h 20m)'
        '</strong>   additional info</code></pre>'
    ],
    [
        sample_job.child_jobs[1],
        ci.CIStatus.FAILED,
        f'<pre><code>{ci.CIStatus.FAILED.value}  task 2 foobarbaz               additional info\n{ci.CIStatus.FAILED.value}'
        '  another failed task <strong>(1h 20m)</strong>   additional info</code></pre>'
    ],
])
def test_ci_task_list(job, status, expected):
    assert job.ci_task_list(status) == expected


@pytest.mark.parametrize('status, expected', [
    [
        None,
        f'<pre><code>{ci.CIStatus.SUCCEEDED.value} {TREE_CONTINUE_MARKER} first child job\n{ci.CIStatus.SUCCEEDED.value} '
        f'{TREE_MORE_JOBS_MARKER}\t{TREE_END_MARKER} my first task   additional info\n{ci.CIStatus.FAILED.value} '
        f'{TREE_END_MARKER} second child job\n{ci.CIStatus.SUCCEEDED.value}  \t{TREE_CONTINUE_MARKER} another task          '
        f'additional info\n{ci.CIStatus.FAILED.value}  \t{TREE_CONTINUE_MARKER} task 2 foobarbaz      additional info\n'
        f'{ci.CIStatus.SUCCEEDED.value}  \t{TREE_CONTINUE_MARKER} third task         \n{ci.CIStatus.FAILED.value}  \t'
        f'{TREE_END_MARKER} another failed task   additional info</code></pre>'
    ],
    [
        ci.CIStatus.SUCCEEDED,
        f'<pre><code>{ci.CIStatus.SUCCEEDED.value} {TREE_END_MARKER} first child job\n{ci.CIStatus.SUCCEEDED.value}  \t'
        f'{TREE_END_MARKER} my first task   additional info</code></pre>'
    ],
    [
        ci.CIStatus.FAILED,
        f'<pre><code>{ci.CIStatus.FAILED.value} {TREE_END_MARKER} second child job\n{ci.CIStatus.FAILED.value}  \t'
        f'{TREE_CONTINUE_MARKER} task 2 foobarbaz      additional info\n{ci.CIStatus.FAILED.value}  \t{TREE_END_MARKER} '
        'another failed task   additional info</code></pre>'
    ],
])
def test_child_ci_job_tree(status, expected):
    assert sample_job.child_ci_job_tree(status) == expected

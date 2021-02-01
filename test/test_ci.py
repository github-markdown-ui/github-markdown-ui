import pytest

from githubmarkdownui import ci
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
    assert sample_job.tasks[0].get_left_justified_task_string_length() == len('✅  first task (15s)')
    assert sample_job.tasks[1].get_left_justified_task_string_length() == len('✅  second task (1m 29s)')


@pytest.mark.parametrize('task, expected', [
    [
        sample_job.tasks[0],
        f'✅  first task {bold("(15s)")}   additional info',
    ],
    [
        sample_job.child_jobs[1].tasks[1],
        '❌  task 2 foobarbaz   additional info',
    ],
    [
        sample_job.child_jobs[1].tasks[2],
        f'✅  third task {bold("(1m 8s)")}'
    ],
])
def test_build_task_string(task, expected):
    assert task.build_task_string() == expected


@pytest.mark.parametrize('task, width, expected', [
    [
        sample_job.tasks[0],
        70,
        '✅  first task <strong>(15s)</strong>                                                      additional info',
    ],
    [
        sample_job.tasks[0],
        len('✅  first task (15s)'),
        '✅  first task <strong>(15s)</strong>   additional info',
    ],
])
def test_build_task_string_with_width(task, width, expected):
    assert task.build_task_string(width=width) == expected


@pytest.mark.parametrize('job, status, expected', [
    [
        sample_job,
        None,
        '<pre><code>✅  first task <strong>(15s)</strong>       additional info\n✅  second task <strong>(1m 29s)'
        '</strong>   additional info</code></pre>',
    ],
    [
        sample_job,
        ci.CIStatus.SUCCEEDED,
        '<pre><code>✅  first task <strong>(15s)</strong>       additional info\n✅  second task <strong>(1m 29s)'
        '</strong>   additional info</code></pre>',
    ],
    [
        sample_job.child_jobs[1],
        None,
        '<pre><code>✅  another task <strong>(10s)</strong>             additional info\n❌  task 2 foobarbaz'
        '               additional info\n✅  third task <strong>(1m 8s)</strong>          \n❌  another failed '
        'task <strong>(1h 20m)</strong>   additional info</code></pre>'
    ],
    [
        sample_job.child_jobs[1],
        ci.CIStatus.FAILED,
        '<pre><code>❌  task 2 foobarbaz               additional info\n❌  another failed task <strong>(1h 20m)'
        '</strong>   additional info</code></pre>'
    ],
])
def test_ci_task_list(job, status, expected):
    assert job.ci_task_list(status) == expected


@pytest.mark.parametrize('status, expected', [
    [
        None,
        '<pre><code>✅ ├─ first child job\n✅ │\t└─ my first task   additional info\n❌ └─ second child job\n✅  '
        '\t├─ another task   additional info\n❌  \t├─ task 2 foobarbaz   additional info\n✅  \t├─ third task   '
        'None\n❌  \t└─ another failed task   additional info</code></pre>'
    ],
    [
        ci.CIStatus.SUCCEEDED,
        '<pre><code>✅ └─ first child job\n✅  \t└─ my first task   additional info</code></pre>',
    ],
    [
        ci.CIStatus.FAILED,
        '<pre><code>❌ └─ second child job\n❌  \t├─ task 2 foobarbaz   additional info\n❌  \t└─ another failed '
        'task   additional info</code></pre>'
    ],
])
def test_ci_job_tree(status, expected):
    assert sample_job.ci_job_tree(status) == expected

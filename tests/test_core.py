# tests/test_core.py
import pytest

from mytodo.core import TaskList


def test_add_task():
    tl = TaskList()
    t = tl.add("写代码")
    assert t.id == 1
    assert t.title == "写代码"


def test_done_invalid_id():
    tl = TaskList()
    with pytest.raises(ValueError, match="任务不存在"):
        tl.done(999)


@pytest.mark.parametrize(
    "title,ok",
    [
        ("hello", True),
        ("", False),
        ("x" * 200, False),
    ],
)
def test_title_validation(title, ok):
    tl = TaskList()
    if ok:
        tl.add(title)
    else:
        with pytest.raises(ValueError):
            tl.add(title)

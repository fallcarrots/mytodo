from pydantic import BaseModel, Field
from datetime import datetime
from pathlib import Path
from typing import Literal
import json

class Task(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=80)
    status: Literal["todo", "doing", "done"] = "todo"
    created_at: datetime = Field(default_factory=datetime.now)

class TaskList(BaseModel):
    tasks: list[Task] = []

    def add(self, title: str) -> Task:
        new_id = max((t.id for t in self.tasks), default=0) + 1
        t = Task(id=new_id, title=title)
        self.tasks.append(t)
        return t

    def done(self, tid: int) -> None:
        for t in self.tasks:
            if t.id == tid:
                t.status = "done"
                return
        raise ValueError(f"任务不存在 id={tid}")

    def save(self, path: Path) -> None:
        path.write_text(self.model_dump_json(indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path) -> "TaskList":
        if not path.exists():
            return cls()
        return cls.model_validate_json(path.read_text(encoding="utf-8"))

# 主程序
if __name__ == "__main__":
    db = Path("tasks.json")
    tl = TaskList.load(db)
    tl.add("写 W08 教程")
    tl.add("学 Pydantic")
    tl.done(1)
    tl.save(db)
    print(tl.model_dump_json(indent=2))
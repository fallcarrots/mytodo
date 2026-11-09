# src/mytodo/cli.py
import argparse

from mytodo.core import TaskList


# 这里必须叫 main，因为 pyproject.toml 里是这么约定的
def main():
    # 1. 创建解析器
    parser = argparse.ArgumentParser(description="我的极简待办事项工具")

    # 2. 定义子命令 (类似 git add, git commit 这种结构)
    subparsers = parser.add_subparsers(dest="command", help="支持的命令")

    # 定义 add 命令
    parser_add = subparsers.add_parser("add", help="添加一个任务")
    parser_add.add_argument("title", type=str, help="任务的名称")

    # 定义 done 命令
    parser_done = subparsers.add_parser("done", help="标记任务完成")
    parser_done.add_argument("tid", type=int, help="任务ID")

    # 3. 解析用户输入的参数
    args = parser.parse_args()

    # 4. 根据用户输入，调用 core 层的逻辑
    tl = TaskList()

    if args.command == "add":
        tl.add(args.title)
    elif args.command == "done":
        tl.done(args.tid)
    else:
        parser.print_help()


# 允许直接 python cli.py 测试
if __name__ == "__main__":
    main()

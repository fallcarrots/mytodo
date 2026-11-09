![CI Status](https://github.com/fallcarrots/mytodo/actions/workflows/test.yml/badge.svg)
# mytodo

一个用 Pydantic 写的极简命令行 TODO 工具。


## 安装

```bash
pip install mytodo


## 使用

```bash
mytodo add "买菜"
mytodo list
mytodo done 1


## 开发

```bash
uv sync --all-extras
uv run pytest

#!/usr/bin/env python3
"""Extract hotel records from a JSON array or nested JSON structure."""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path
from typing import Any, Iterator


FIELDS = ("名称", "酒店类型", "地址", "电话")


def walk(value: Any) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        if "名称" in value:
            yield value
        for child in value.values():
            yield from walk(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk(child)


def parse(input_path: Path, output_path: Path) -> int:
    with input_path.open("r", encoding="utf-8") as source:
        data = json.load(source)

    records = list(walk(data))
    if not records:
        raise ValueError("没有找到包含“名称”字段的酒店记录")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="", encoding="utf-8-sig") as target:
        writer = csv.DictWriter(target, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(records)
    return len(records)


def main() -> int:
    if len(sys.argv) not in (2, 3):
        print(f"用法: {sys.argv[0]} INPUT.json [OUTPUT.csv]", file=sys.stderr)
        return 2

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) == 3 else Path("output.csv")
    if not input_path.is_file():
        print(f"找不到输入文件: {input_path}", file=sys.stderr)
        return 1

    try:
        count = parse(input_path, output_path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"处理失败: {exc}", file=sys.stderr)
        return 1

    print(f"已提取 {count} 条记录 -> {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

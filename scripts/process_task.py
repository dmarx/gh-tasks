# scripts/process_task.py
from dataclasses import dataclass
import json

from duckduckgo_search import DDGS
import fire
import loguru
# TODO: import interfaces for compatibility

ddg = DDGS()

OPERATORS={
    "ddg.image": ddg.image,
    "ddg.chat": ddg.chat,
}

@dataclass
class TaskConfig:
    operator: str
    kwargs: dict

def main(config: Config):
    config = Config(**json.loads(config))
    loguru.info("hello gh-tasks")
    loguru.info(config)
    op = OPERATORS[config.operator]
    result = op(**kwargs)
    logger.info(result)
    return result

fire.Fire(main)

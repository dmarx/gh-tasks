# scripts/process_task.py
from dataclasses import dataclass
import json

from duckduckgo_search import DDGS
import fire
#from gh_store.core.access import AccessControl
from loguru import logger
# TODO: import abstract interfaces for compatibility

#access_control = AccessControl(self.repo)

# TODO: access validation as gh-store CLI capability
# issue = self.repo.get_issue(issue_number)
#         if not self.access_control.validate_issue_creator(issue):

ddg = DDGS()

def image_search(**kwargs):
    results = ddg.images(**kwargs)
    outstr="  \n".join([f"![{r['title']}]({r['image']})" for r in results])
    return outstr

OPERATORS={
    "ddg.images": image_search,
    "ddg.chat": ddg.chat,
}


@dataclass
class TaskConfig:
    operator: str
    kwargs: dict

def main(config: dict):
    config = TaskConfig(**config)
    logger.info(config)
    op = OPERATORS[config.operator]
    result = op(**config.kwargs)
    logger.info(result)
    return result

fire.Fire(main)

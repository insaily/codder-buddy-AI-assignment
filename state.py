
from typing import TypedDict, List


class AgentState(TypedDict):
    user_request: str
    project_plan: str
    architecture: str
    generated_files: List[str]
    status: str
    error: str

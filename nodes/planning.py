
import os
from langchain_groq import ChatGroq


def planning_node(state):
    """Convert the user's request into a structured project plan."""

    try:
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0.2,
            api_key=os.getenv("GROQ_API_KEY"),
        )

        prompt = f"""
You are a software project planner.

Create a clear, beginner-friendly plan for this project:
{state['user_request']}

Include:
1. Project goal
2. Main features
3. Technologies required
4. Files to create
5. Implementation steps

Return only the project plan.
"""

        response = llm.invoke(prompt)

        return {
            "project_plan": response.content,
            "status": "Planning completed",
            "error": "",
        }

    except Exception as e:
        return {
            "project_plan": "",
            "status": "Planning failed",
            "error": str(e),
        }

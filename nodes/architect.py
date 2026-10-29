
import os
from langchain_groq import ChatGroq


def architect_node(state):
    """Turn the project plan into detailed implementation instructions."""

    try:
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0.2,
            api_key=os.getenv("GROQ_API_KEY"),
        )

        prompt = f"""
You are a senior software architect.

Based on this project plan:
{state['project_plan']}

Create a detailed technical design that includes:
1. Application structure
2. File names and purpose
3. Technologies and libraries
4. How the components connect
5. Implementation guidelines

Keep the design practical and suitable for a beginner.
Return only the technical design.
"""

        response = llm.invoke(prompt)

        return {
            "architecture": response.content,
            "status": "Architecture completed",
            "error": "",
        }

    except Exception as e:
        return {
            "architecture": "",
            "status": "Architecture failed",
            "error": str(e),
        }

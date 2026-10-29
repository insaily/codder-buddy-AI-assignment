
import os
from pathlib import Path
from langchain_groq import ChatGroq


PROJECT_DIR = Path("generated_projects").resolve()


def coder_node(state):
    """Generate a simple HTML project and save it safely."""

    try:
        llm = ChatGroq(
            model="openai/gpt-oss-20b",
            temperature=0.2,
            api_key=os.getenv("GROQ_API_KEY"),
        )

        prompt = f"""
You are an expert software developer.

User request:
{state['user_request']}

Project plan:
{state['project_plan']}

Architecture:
{state['architecture']}

Create a complete, attractive, responsive website using HTML, CSS,
and JavaScript.

Return ONLY the complete HTML document. Put CSS inside a <style> tag
and JavaScript inside a <script> tag. Do not use Markdown code fences.
"""

        response = llm.invoke(prompt)
        html_code = response.content.strip()

        # Remove Markdown fences if the model includes them.
        if html_code.startswith("```"):
            html_code = html_code.split("\n", 1)[1]
            if html_code.endswith("```"):
                html_code = html_code[:-3].strip()

        PROJECT_DIR.mkdir(parents=True, exist_ok=True)
        output_file = (PROJECT_DIR / "index.html").resolve()

        # Prevent writing outside the generated project directory.
        if not output_file.is_relative_to(PROJECT_DIR):
            raise ValueError("Invalid output path.")

        output_file.write_text(html_code, encoding="utf-8")

        return {
            "generated_files": [str(output_file)],
            "status": "Code generation completed",
            "error": "",
        }

    except Exception as e:
        return {
            "generated_files": [],
            "status": "Code generation failed",
            "error": str(e),
        }

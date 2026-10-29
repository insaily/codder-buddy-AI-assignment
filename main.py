
from dotenv import load_dotenv
from graph import agent

load_dotenv()


def run_agent(user_request: str):
    """Run the complete Coder Buddy workflow."""

    initial_state = {
        "user_request": user_request,
        "project_plan": "",
        "architecture": "",
        "generated_files": [],
        "status": "Starting",
        "error": "",
    }

    result = agent.invoke(initial_state)

    return result


if __name__ == "__main__":
    request = input("What would you like Coder Buddy to build? ")

    result = run_agent(request)

    print("\n--- Project Plan ---")
    print(result.get("project_plan", ""))

    print("\n--- Architecture ---")
    print(result.get("architecture", ""))

    print("\n--- Status ---")
    print(result.get("status", ""))

    if result.get("error"):
        print("\n--- Error ---")
        print(result["error"])

    print("\n--- Generated Files ---")
    for file_path in result.get("generated_files", []):
        print(file_path)

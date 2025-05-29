from pathlib import Path

def extract_workflows(path: str = ".github/workflows/") -> str:
    workflows = []
    for f in Path(path).rglob("*.yml"):
        workflows.append(f.read_text())
    return "\n---\n".join(workflows)
from pathlib import Path

def extract_terraform_context(tf_path: str) -> str:
    content = []
    for tf_file in Path(tf_path).rglob("*.tf"):
        content.append(tf_file.read_text())
    return "\n".join(content)
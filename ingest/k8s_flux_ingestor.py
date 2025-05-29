import yaml
from pathlib import Path

def extract_k8s_manifests(kustomization_path: str) -> str:
    context = []
    for yml in Path(kustomization_path).rglob("*.yaml"):
        try:
            doc = yaml.safe_load(yml.read_text())
            context.append(str(doc))
        except:
            continue
    return "\n---\n".join(context)

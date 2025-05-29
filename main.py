from ingest.terraform_ingestor import extract_terraform_context
from ingest.k8s_flux_ingestor import extract_k8s_manifests
from ingest.github_actions_ingestor import extract_workflows
from context_index.index_builder import build_index
from prompt_engine.query_agent import get_retrieval_chain, query_ai

def main():
    terraform = extract_terraform_context("./infra")
    k8s = extract_k8s_manifests("./apps")
    workflows = extract_workflows("./.github/workflows")

    docs = [terraform, k8s, workflows]
    index = build_index(docs)

    chain = get_retrieval_chain(index)

    while True:
        q = input("Ask your SRE AI anything > ")
        print(query_ai(q, chain))

if __name__ == "__main__":
    main()
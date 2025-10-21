# /// script
# requires-python = ">=3.13"
# dependencies = [
# ]
# ///

import os

STEP_SUMMARY = os.getenv("GITHUB_STEP_SUMMARY")

scripts_template = """
#!/bin/bash
set -e

echo "=== start deploy scripts ==="

echo aws_region=${AWS_REGION}
echo image_ref=${IMAGE_REF}
echo registry=${REGISTRY}
echo repository=${ECR_REPOSITORY}

"""

def main():
    scripts = os.path.expandvars(scripts_template)
    with open(STEP_SUMMARY, "a") as summary_file:
        print(f"Start Deployment\n", file=summary_file)
        print(f"{scripts=}", file=summary_file)
        print(f"Finish Deployment\n", file=summary_file)


if __name__ == "__main__":
    main()

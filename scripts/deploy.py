# /// script
# requires-python = ">=3.13"
# dependencies = [
# ]
# ///

import os

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
    print(f"{scripts=}")


if __name__ == "__main__":
    main()

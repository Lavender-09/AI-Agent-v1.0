import sys
import os
import anthropic
from run_tests import run_tests

client = anthropic.Anthropic()

def get_hint(folder: str, test_class: str, source_file: str) -> str:
    """Runs the test, then asks the model for a hint based on the output and source code.
    Never asks for or returns a fix, only a hint."""
    test_output = run_tests(folder, test_class)

    source_path = os.path.join(folder, source_file)
    with open(source_path, "r") as f:
        source_code = f.read()

    prompt = f"""You are a tutor for a software engineering student. Below is a Java class and the output from compiling/running a test against it.

Your job: give ONE short hint about what might be wrong, if anything. Rules:
- Do NOT write corrected code.
- Do NOT give the full fix.
- Point to the general area or concept (e.g. "check what your getter for X returns" or "compare the constructor's parameter order to how you're calling it").
- If everything looks correct, say so briefly and why.
- Keep it to 2-4 sentences.

Source file ({source_file}):
{source_code}

Test output:
{test_output}
"""

    reply = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=300,
        messages=[{"role": "user", "content": prompt}],
    )
    return reply.content[0].text


if __name__ == "__main__":
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    test_class = sys.argv[2] if len(sys.argv) > 2 else "FruitTest"
    source_file = sys.argv[3] if len(sys.argv) > 3 else "Fruit.java"

    print("Running tests...\n")
    print(get_hint(folder, test_class, source_file))
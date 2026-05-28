# AutoDoc Documentation Generator

AutoDoc is a tool designed for automatically generating comprehensive documentation for source code repositories using a local Large Language Model (LLM) via Ollama.

## Installation

To use the repository, follow these steps:

1.  Clone the repository:
    ```bash
    git clone https://github.com/Perceptronic-Systems/AutoDoc
    ```
2.  Install required Python libraries within a virtual environment:
    ```bash
    pip install -r 'path/to/AutoDoc/requirements.txt'
    ```

**Prerequisites**: The library requires a local instance of **Ollama** to be running.

## Configuration

Behavior can be controlled via a configuration file located at `~/.config/autodoc/config.toml`. Alternatively, the code base can be customized directly.

### Example Configuration

A sample `config.toml` file structure is provided below:

```toml
[ollama]
host_address = "http://127.0.0.1:11434"
model_context = 16384

[repository]
repo_dir = "~/Autodoc/repo"
link = "https://github.com/Perceptronic-Systems/AutoDoc"

[output]
output_dir = "~/AutoDoc/Docs/generated_documentation.md"
```

## Functionality Overview

The process executed by `main.py` involves several distinct stages:

1.  **Source Code Acquisition**: Clones the target GitHub repository into a local `source` directory.
2.  **Configuration Loading**: Reads and applies settings from `~/.config/autodoc/config.toml`, overriding default parameters if present.
3.  **File Collection**: Recursively traverses the source directory, collecting the content of all source files while excluding common metadata files (e.g., `.gitignore`, `LICENSE`). The content of all files is concatenated into a single input string.
4.  **Prompt Construction**: A detailed, expert prompt is constructed. This prompt strictly enforces documentation formatting guidelines:
    *   The tone must be formal, brief, and impersonal.
    *   Output must be in Markdown format.
    *   Code quotes must use backticks (e.g., `code quote`).
    *   Code blocks must use fenced code blocks (e.g., `\`\`\`markdown\ncode block\n\`\`\``).
5.  **Documentation Generation**: Initializes an `ollama.Client` and streams the request to the configured LLM model (`gemma4:e4b`). The collected source code content is passed to the model along with the expert prompt.
6.  **Output**: The streamed response is printed to the console in real-time and simultaneously written to the output file specified in the configuration (`generated_doc.md`).

## Technical Details

*   **Dependencies**: Requires `ollama` for LLM interaction, `gitpython` for repository cloning, and `tomllib` for configuration parsing.
*   **Command Execution**: The script executes the entire pipeline upon running `main.py`.

```python
# Initialization setup:
# model = "gemma4:e4b"
# api = "http://127.0.0.1:11434"
# client = ollama.Client(host=api)
```
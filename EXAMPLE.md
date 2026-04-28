# AutoDoc Documentation Generator

This script is designed to automatically generate comprehensive documentation for a specified set of source code files using a local LLM via Ollama.

## Dependencies

The script requires the following libraries:

*   `ollama`: For interacting with the local Ollama API.
*   `git`: For cloning the source repository.
*   `tomllib`: For reading TOML configuration files.
*   `shutil`: For directory management (cleanup).

## Functionality Overview

The script performs the following steps:

1.  **Initialization and Setup**: Defines constants for the target GitHub repository, local source directory (`source`), and output document path (`generated_doc.md`).
2.  **Source Code Acquisition**:
    *   It checks if the local source directory exists and deletes its contents if present, ensuring a clean slate.
    *   It clones the repository specified by `github_repo` into the local `source` directory.
3.  **Configuration Loading**: Attempts to load configuration settings from the user's global TOML configuration file (`~/.config/autodoc/config.toml`). If the Ollama host address is specified in this file, it overrides the default API endpoint.
4.  **File Gathering**:
    *   The `get_files` function recursively traverses the `source` directory.
    *   It collects the content of all recognized files, excluding common version control and metadata files (e.g., `.gitignore`, `LICENSE`).
    *   The content of all gathered files is concatenated into a single string, separated by delimiters.
5.  **Prompt Construction**: A detailed prompt is constructed, instructing the language model to act as an expert code documenter. This prompt includes specific formatting guidelines for the output (Markdown format, use of backticks for quotes, and code blocks).
6.  **Documentation Generation**:
    *   An `ollama.Client` is initialized using the configured API address.
    *   The script calls `client.generate` with the constructed prompt and the concatenated source code content.
    *   The response stream is printed to the console in real-time while simultaneously accumulating the final documentation text.
7.  **Output**: The accumulated documentation string is written to the `generated_doc.md` file in the script's base directory.

## Execution Details

The script reads all relevant source files, packages their content, and passes them along with expert instructions to a local LLM instance running via Ollama to generate the final documentation document.

```python
# Placeholder for configuration loading and client initialization
# Example: api = "http://127.0.0.1:11434"
# Example: client = ollama.Client(host=api)
```

**Note**: The script utilizes the `ollama` library to interact with the language model service.
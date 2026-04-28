# AutoDoc
Automatic code documentation for github repos

AutoDoc makes it faster than ever to understand undocumented code.
To get started, first clone the repository with `git clone https://github.com/Perceptronic-Systems/AutoDoc`

Install the python libraries from your virtual environment using `pip install -r 'path/to/AutoDoc/requirements.txt`

This library requires ollama in order to work.

After these requirements are met, you can either create a config file at `~/.config/autodoc/config.toml` to control the behavior of AutoDoc, or customize the existing code base in order to achieve the desired results.

Here is an example config file:
```
[ollama]
host_address = "http://127.0.0.1:11434"
model_context = 16384

[repository]
repo_dir = "~/Autodoc/repo"
link = "https://github.com/Perceptronic-Systems/AutoDoc"

[output]
output_dir = "~/AutoDoc/Docs/generated_documentation.md"
```

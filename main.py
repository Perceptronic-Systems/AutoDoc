import ollama
import os
import tomllib
from git import Repo
import shutil

model = "gemma4:e4b"
api = "http://127.0.0.1:11434"
base_dir = os.path.dirname(os.path.abspath(__file__))
github_repo = "https://github.com/Perceptronic-Systems/AutoDoc"
src_dir = os.path.join(base_dir, "source") # Code files go here
doc_dir = os.path.join(base_dir, "generated_doc.md") # Output goes here

ignore = ['.gitignore', '.git', 'LICENSE', 'package.json', 'package-lock.json', 'vite-config.json']

if os.path.exists(src_dir):
    shutil.rmtree(src_dir)
if github_repo != "":
    Repo.clone_from(github_repo, src_dir)

config_path = os.path.expanduser("~/.config/autodoc/config.toml")
if os.path.exists(config_path):
    with open(config_path, 'rb') as f:
        config = tomllib.load(f)
    try:
        api = config['ollama']['host_address']
    except Exception as e:
        print("Could not find attribute in config")
        print(e)

print(f"Ollama API: {api}")
client = ollama.Client(host=api)

files = []

def get_files(dir):
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        if os.path.isdir(path) and file != ".git":
            get_files(path)
        elif file not in ignore:
            try:
                text = ""
                with open(path, 'r') as f:
                    text = f.read()
                files.append(file + '\n' + text)
            except Exception as e:
                print(f"Error while decoding utf-8 in file '{file}'")

get_files(src_dir)
content = '\n```\n\n```\n'.join(files)

prompt = f"""
You are an expert code documenter.
Your goal is to write efficient and easy to understand documentation for the provided code file.
Never speak in first person. Always use formal yet brief language. Always respond in markdown fromat.
Any code quotes should be placed in backquotes: e.g. `code quote`
Code snippets should be placed in a code block:
e.g.
```
markdown
code block
```
Only include relevant information, and documentation should be simple and concise.

Please write a markdown document for the following code files:
```
{content}
```
"""

stream = client.generate(model=model,
                         prompt=prompt,
                         think=False,
                         stream=True,
                         options={'num_ctx': 16384})

print("        Generated: \n")
generated = ""
for chunk in stream:
    token = chunk['response']
    print(token, end='', flush=True)
    generated += token

with open(doc_dir, 'w') as f:
    f.write(generated);
print("\n\n        Done!")
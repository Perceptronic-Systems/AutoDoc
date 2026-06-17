#!/usr/bin/env bash

set -e

REPO_URL="https://github.com/Perceptronic-Systems/AutoDoc"
INSTALL_DIR="$HOME/.local/bin"
CONFIG_DIR="$HOME/.config/autodoc"
BINARY_NAME="autodoc"

echo "========================================="
echo "       AutoDoc Installer / Updater       "
echo "========================================="

mkdir -p "$INSTALL_DIR"

if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo "Warning: $INSTALL_DIR is not in your PATH."
    echo "You may need to add 'export PATH=\"\$HOME/.local/bin:\$PATH\"' to your ~/.bashrc or ~/.zshrc"
fi

echo "Checking dependencies..."
for cmd in git python3 pip3; do
    if ! command -v $cmd &> /dev/null; then
        echo "Error: $cmd is required but not installed." >&2
        exit 1
    fi
done

echo "Installing/Updating required Python packages..."
pip3 install --user --upgrade ollama gitpython > /dev/null

TMP_DIR=$(mktemp -d)
echo "Downloading latest version..."

git clone --depth 1 "$REPO_URL" "$TMP_DIR" > /dev/null

echo "Installing executable to $INSTALL_DIR/$BINARY_NAME..."
cp "$TMP_DIR/$BINARY_NAME" "$INSTALL_DIR/$BINARY_NAME"
chmod +x "$INSTALL_DIR/$BINARY_NAME"

if [ ! -f "$CONFIG_DIR/config.toml" ]; then
    echo "Initializing default configuration..."
    mkdir -p "$CONFIG_DIR"
    # Create a minimal template config file
    cat <<EOF > "$CONFIG_DIR/config.toml"
[ollama]
host_address = "http://127.0.0.1:11434"
model_context = 32768

[repository]
link = ""
repo_dir = "~/.cache/autodoc/source"

[output]
output_dir = "~/generated_doc.md"
EOF
fi

rm -rf "$TMP_DIR"

echo "-----------------------------------------"
echo " Success! AutoDoc is installed/updated."
echo " Try running: $BINARY_NAME --help"
echo "========================================="
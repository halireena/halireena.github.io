#!/bin/bash
cd "$(dirname "$0")"
echo "Starting the preview. Your browser will open. Keep this window open while you edit;"
echo "every time you save a file the page refreshes. Press Ctrl+C here to stop."
quarto preview

#!/bin/bash
cd "$(dirname "$0")"
echo "Checking the site builds without errors..."
if ! quarto render > /tmp/quarto-render.log 2>&1; then
  echo "The site did not build. The error is below. Fix it (usually a typo in the --- block at the top of a page), then run this again."
  tail -20 /tmp/quarto-render.log; exit 1
fi
read -r -p "Short note about what you changed (e.g. 'New blog post'): " msg
git add -A
git commit -q -m "${msg:-Update site}" || echo "Nothing new to publish."
git push
echo
echo "Uploaded. GitHub publishes it in 1-3 minutes (longer if GitHub is busy)."
echo "Check: https://halireena.github.io   (refresh with Cmd+Shift+R if you see the old version)"

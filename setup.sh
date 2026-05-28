#!/usr/bin/env bash
# Initialize git, make the first commit, and prep the repo for GitHub.
# Run from inside the rugiet-lifecycle directory after unzipping the bundle.

set -e

echo "==> Initializing git repo..."
if [ ! -d .git ]; then
  git init -b main
else
  echo "    (already a git repo, skipping init)"
fi

echo "==> Ensuring empty directories are tracked..."
# Git doesn't track empty directories, so we drop .gitkeep files
touch briefs/.gitkeep
touch outputs/creative/.gitkeep
touch outputs/analyses/.gitkeep
touch outputs/strategy/.gitkeep

echo "==> Staging files..."
git add .

echo "==> Status:"
git status --short

echo ""
echo "==> Making first commit..."
git commit -m "Initial repo: copywriting + design skills, lifecycle-creative agent"

echo ""
echo "✅ Done."
echo ""
echo "Next steps:"
echo "  1. Create an empty repo on GitHub (private). Do not initialize with README."
echo "  2. Add it as your remote:"
echo "       git remote add origin git@github.com:YOUR-USERNAME/rugiet-lifecycle.git"
echo "  3. Push:"
echo "       git push -u origin main"
echo "  4. Open the folder in Cursor and start Claude Code:  claude"
echo ""
echo "When you're ready to move this to the Rugiet org, use GitHub's Settings →"
echo "Danger Zone → Transfer ownership. Local clones keep working via redirect."

#!/bin/bash
# Auto-pull script - checks for remote changes and pulls if needed
# Usage: ./auto-pull.sh /path/to/repo
# Cron example (every 5 min): */5 * * * * /path/to/auto-pull.sh /path/to/repo >> /var/log/auto-pull.log 2>&1

REPO_DIR="${1:-.}"
cd "$REPO_DIR" || exit 1

# Fetch latest from remote
git fetch origin

# Get current and remote branch
BRANCH=$(git rev-parse --abbrev-ref HEAD)
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse origin/$BRANCH)

# Pull if there are changes
if [ "$LOCAL" != "$REMOTE" ]; then
    echo "[$(date)] Changes detected on $BRANCH, pulling..."
    git pull origin "$BRANCH"
    echo "[$(date)] Pull complete"
else
    echo "[$(date)] No changes"
fi

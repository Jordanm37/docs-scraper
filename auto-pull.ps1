# Auto-pull script for Windows
# Usage: .\auto-pull.ps1 -RepoPath "C:\path\to\repo"
# Task Scheduler: powershell.exe -ExecutionPolicy Bypass -File "C:\path\to\auto-pull.ps1" -RepoPath "C:\path\to\repo"

param(
    [string]$RepoPath = "."
)

Set-Location $RepoPath

# Fetch latest from remote
git fetch origin

# Get current and remote branch
$branch = git rev-parse --abbrev-ref HEAD
$local = git rev-parse HEAD
$remote = git rev-parse "origin/$branch"

$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"

# Pull if there are changes
if ($local -ne $remote) {
    Write-Host "[$timestamp] Changes detected on $branch, pulling..."
    git pull origin $branch
    Write-Host "[$timestamp] Pull complete"
} else {
    Write-Host "[$timestamp] No changes"
}

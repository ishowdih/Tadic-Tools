# Tadic Tools - Windows Installer
# Usage: irm https://raw.githubusercontent.com/ishowdih/Tadic-Tools/main/install.ps1 | iex

$ErrorActionPreference = "Stop"

$repo    = "ishowdih/Tadic-Tools"
$apiUrl  = "https://api.github.com/repos/$repo/releases/latest"
$headers = @{ "Accept" = "application/vnd.github.v3+json" }

Write-Host "Fetching latest release info..." -ForegroundColor Cyan

try {
    $release = Invoke-RestMethod -Uri $apiUrl -Headers $headers
}
catch {
    Write-Host "[X] Could not reach GitHub API. Check your connection." -ForegroundColor Red
    exit 1
}

# Find the .exe asset
$asset = $release.assets | Where-Object { $_.name -like "*.exe" } | Select-Object -First 1

if (-not $asset) {
    Write-Host "[X] No .exe file found in the latest release." -ForegroundColor Red
    Write-Host "    Available assets: $($release.assets.name -join ', ')" -ForegroundColor Yellow
    exit 1
}

# Install location: %LOCALAPPDATA%\Programs\TadicTools
$installDir = Join-Path $env:LOCALAPPDATA "Programs\TadicTools"
New-Item -ItemType Directory -Path $installDir -Force | Out-Null

$exePath = Join-Path $installDir $asset.name

Write-Host "Downloading $($asset.name)..." -ForegroundColor Cyan
Invoke-WebRequest -Uri $asset.browser_download_url -OutFile $exePath -UseBasicParsing

Write-Host ""
Write-Host "✅ Installed to: $exePath" -ForegroundColor Green
Write-Host ""
Write-Host "To run Tadic Tools:" -ForegroundColor Cyan
Write-Host "  & `"$exePath`"" -ForegroundColor White
Write-Host ""
Write-Host "Want to add it to your PATH so you can type 'tadictools' anywhere?" -ForegroundColor Cyan
$addToPath = Read-Host "Add to PATH? (y/n)"

if ($addToPath -eq "y") {
    $userPath = [Environment]::GetEnvironmentVariable("Path", "User")
    if ($userPath -notlike "*$installDir*") {
        $newPath = "$installDir;$userPath"
        [Environment]::SetEnvironmentVariable("Path", $newPath, "User")
        Write-Host "✅ Added to user PATH. Restart your terminal for it to take effect." -ForegroundColor Green
    } else {
        Write-Host "Already in PATH." -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Done. Enjoy!" -ForegroundColor Green

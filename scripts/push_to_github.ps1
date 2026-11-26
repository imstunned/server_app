# Публикация проекта на GitHub
#
# Использование (из корня проекта):
#   powershell -ExecutionPolicy Bypass -File scripts/push_to_github.ps1 -RepoUrl https://github.com/USER/REPO.git
#
# Скрипт:
#   1. проверяет, что мы в git-репозитории;
#   2. добавляет (или обновляет) remote origin;
#   3. отправляет все ветки: main, develop, feature/lab1..lab4;
#   4. отправляет теги.

param(
    [Parameter(Mandatory = $true)]
    [string]$RepoUrl,

    [string]$Remote = "origin"
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".git")) {
    throw "Запустите скрипт из корня проекта (папка .git не найдена)."
}

$branches = @("main", "develop", "feature/lab1", "feature/lab2", "feature/lab3", "feature/lab4")

Write-Host "Проверяю наличие веток..." -ForegroundColor Cyan
foreach ($branch in $branches) {
    git rev-parse --verify --quiet "refs/heads/$branch" | Out-Null
    if ($LASTEXITCODE -ne 0) {
        throw "Ветка '$branch' не найдена."
    }
}

$existing = git remote
if ($existing -contains $Remote) {
    Write-Host "Обновляю remote $Remote -> $RepoUrl" -ForegroundColor Cyan
    git remote set-url $Remote $RepoUrl
} else {
    Write-Host "Добавляю remote $Remote -> $RepoUrl" -ForegroundColor Cyan
    git remote add $Remote $RepoUrl
}

Write-Host "Отправляю ветки..." -ForegroundColor Cyan
git push -u $Remote main develop
foreach ($branch in $branches | Where-Object { $_ -notin @("main", "develop") }) {
    git push -u $Remote $branch
}

Write-Host "Отправляю теги..." -ForegroundColor Cyan
git push $Remote --tags

Write-Host ""
Write-Host "Готово. Откройте репозиторий и создайте Pull/Merge Request:" -ForegroundColor Green
Write-Host "  feature/lab1 -> develop"
Write-Host "  feature/lab2 -> develop"
Write-Host "  feature/lab3 -> develop"
Write-Host "  feature/lab4 -> develop"
Write-Host "  develop -> main"

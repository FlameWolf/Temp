# Git Commands

## Create new branch

```bash
git checkout -b feature/refactor-code origin/master --no-track
```

## Clear unwanted branches from local

```bash
git checkout master; git pull --prune; git branch | Where-Object { $_ -notmatch '^\*' } | ForEach-Object { git branch -D $_.Trim() }
```

## Merge with rebase

```bash
git fetch origin master; git rebase origin/master; git push --force-with-lease; git fetch; git pull
```
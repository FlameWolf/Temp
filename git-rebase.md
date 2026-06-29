# Git Rebase

```bash
# 1. Verify you're on feature/feat01
git status

# 2. Fetch latest Dev branch
git fetch origin Dev

# 3. Rebase onto the fetched Dev
git rebase origin/Dev

# 4. If conflicts occur, resolve and continue
git add <resolved-files>
git rebase --continue

# 5. Verify the rebase
git log --oneline -5

# 6. Continue working as normal
git add <files>
git commit -m "Your message"
git push origin feature/feat01 --force-with-lease
```
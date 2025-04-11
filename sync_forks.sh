#!/bin/bash

#Url to main Repo (HTTPS)
UPSTREAM_URL="https://git.imp.fu-berlin.de/bks-tuts/bks-exercises.git"
#================================================================================================
#stage and commit local changes
commit_changes() {
    if [ -n "$(git status --porcelain)" ]; then
        echo "Committing uncommitted changes..."
        git add -A
        git commit -m "Auto-commit: saving changes before branch update"
        git push origin $(git rev-parse --abbrev-ref HEAD)
    fi
}
#================================================================================================


#Set upstream if not exist
#================================================================================================
if git remote | grep -q 'upstream'; then
    echo "Upstream already exists."
else
    echo "Adding upstream remote..."
    git remote add upstream $UPSTREAM_URL
fi
git remote -v
#================================================================================================


# Fetch changes from upstream
#================================================================================================
echo "Fetching all changes from upstream..."
git fetch upstream

# Track all branches from upstream and push them to origin
for branch in $(git branch -r | grep 'upstream/' | grep -v 'upstream/HEAD'); do
    # Extract the branch name
    local_branch=$(echo $branch | sed 's/upstream\///')

    # Check for uncommitted changes and commit if necessary
    commit_changes

    # Check if branch already exists locally
    if git show-ref --verify --quiet refs/heads/$local_branch; then
        echo "Branch '$local_branch' already exists locally. Checking out and merging changes from upstream..."
        git checkout $local_branch
        git pull origin $local_branch  # Ensure local is in sync with origin
        git merge upstream/$local_branch
    else
        # Checkout branch locally if it doesn't exist
        echo "Checking out and tracking new branch '$local_branch' from upstream..."
        git checkout -b $local_branch $branch
    fi

    # Push branch to origin (your fork)
    echo "Pushing branch '$local_branch' to origin..."
    git push origin $local_branch

done
#================================================================================================

# Check for uncommitted
commit_changes

echo "All branches have been fetched, tracked, and pushed to origin!"

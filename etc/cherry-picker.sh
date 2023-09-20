#!/bin/bash

sha=$1
base=v1
target=main
dirname=$(mktemp -d)
user=$(git config github.user)

if [ -z "$user" ]; then
    echo "Please set GitHub User"
    echo "git config --global github.user <github_handle>"
    exit 1
fi

mkdir -p $dirname
if [ -z $GITHUB_TOKEN ]; then
    git clone git@github.com:mongodb/mongo-go-driver.git $dirname
else
    echo "$GITHUB_TOKEN" > mytoken.txt
    gh auth login --with-token < mytoken.txt
    git clone https://github.com/mongodb/mongo-go-driver.git $dirname
fi

cd $dirname
if [ -z $GITHUB_TOKEN ]; then
    git remote add $user git@github.com:$user/mongo-go-driver.git
else
    git remote add $user https://github.com/$user/mongo-go-driver.git
fi

gh repo set-default mongodb/mongo-go-driver
branch="cherry-pick-$sha"
head="$user:$branch"
git fetch origin $base
git fetch origin $target
git checkout -b $branch origin/$target
git cherry-pick -x $sha

old_title=$(git --no-pager log  -1 --pretty=%B | head -n 1)
ticket=$(echo $old_title | sed -r 's/([A-Z]+-[0-9]+).*/\1/')
text=$(echo $old_title | sed -r 's/([A-Z]+-[0-9]+) (.*) \(#[0-9]*\)/\2/')
pr_number=$(echo $old_title| sed -r 's/.*(#[0-9]*)\)/\1/')

title="$ticket [$target] $text"
body="Cherry-pick of $pr_number from $base to $target"

echo
echo "Creating PR..."
echo "Title: $title"
echo "Body: $body"
echo "Base: $target"
echo "Head: $head"
echo

read -p 'Push changes? (Y/n) ' choice
if [[ "$choice" == "Y" || "$choice" == "y" || -z "$choice" ]]; then
    if [ -n $user ]; then
        git push $user
    fi
    gh pr create --title "$title" --base $target --head $head --body "$body"
fi

#!/bin/bash

# Abort if no commit message is provided
if [ -z "$1" ]; then
  echo "[ERROR] You forgot the commit message!"
  echo "Usage: ./update.sh \"Your message here\""
  exit 1
fi

echo "[*] Staging all files..."
git add .

echo "[*] Committing changes..."
git commit -m "$1"

echo "[*] Pushing to GitHub..."
git push origin main

echo "[SUCCESS] Code pushed to production!"
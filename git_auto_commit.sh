#!/bin/bash
cd /home/ambarshingade/mental_health_analysis || exit
git add .
git commit -m "Auto commit on $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main
echo "✅ Auto commit and push completed!"

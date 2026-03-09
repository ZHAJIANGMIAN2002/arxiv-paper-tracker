#!/bin/bash
# Setup cron job for daily VLN paper tracking at 10:00 AM

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CRON_CMD="0 10 * * * ${SCRIPT_DIR}/run_daily.sh >> ${SCRIPT_DIR}/output/cron.log 2>&1"

# Check if cron job already exists
if crontab -l 2>/dev/null | grep -q "run_daily.sh"; then
    echo "[INFO] Cron job already exists:"
    crontab -l | grep "run_daily.sh"
    echo ""
    read -p "Replace existing cron job? [y/N] " answer
    if [[ "$answer" != "y" && "$answer" != "Y" ]]; then
        echo "Skipped."
        exit 0
    fi
    # Remove old entry
    crontab -l 2>/dev/null | grep -v "run_daily.sh" | crontab -
fi

# Add new cron job
(crontab -l 2>/dev/null; echo "$CRON_CMD") | crontab -

echo "[OK] Cron job installed:"
echo "     $CRON_CMD"
echo ""
echo "Verify with: crontab -l"

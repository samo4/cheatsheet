#!/bin/bash
sleep 20
chromium-browser --kiosk http://localhost:3000 --no-first-run --touch-events=enabled --fast --fast-start --disable-popup-blocking --disable-infobars --disable-session-crashed-bubble --disable-tab-switcher --disable-translate --enable-low-res-tiling --noerordialogs

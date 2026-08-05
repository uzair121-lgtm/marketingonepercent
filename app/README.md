# Calorie Tracker

A simple, zero-dependency calorie tracking app. Log **one calorie value per day** and see the trend on a chart.

## Usage

Open `index.html` in any modern browser. That's it — no build step, no server, no install.

## Features

- **One value per day** — pick a date, enter calories, hit Save. Re-logging the same day overwrites it.
- **Trend chart** — a line/area chart of every logged day, drawn with the canvas API (no chart library).
- **Quick stats** — today's total, 7-day average, and days logged.
- **History table** — review or delete past entries.
- **Local persistence** — data is saved in your browser's `localStorage`, so it survives refreshes. Nothing leaves your device.

## Notes

- Data is stored under the key `calorie-tracker.v1` in `localStorage`. Clearing your browser data will erase it.
- Because it's per-browser, the log doesn't sync across devices.

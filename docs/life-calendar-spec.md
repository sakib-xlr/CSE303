# Life Calendar (Android) — Product + UX Spec

## Overview
Life Calendar is a minimalist, distraction-free Android app that visualizes the passage of time as a grid of dots. Each dot represents a day in the current year. Completed days are filled; remaining days are dim. The interface is intentionally sober—quiet, calm, and slightly uncomfortable—inspired by memento mori and stoic minimalism.

## Core Concept
- **Time visualization:** 365 dots, one per day.
- **State encoding:**
  - Completed day: solid white.
  - Remaining day: white at low opacity.
  - Current day: white at medium opacity with a subtle glow or slight scale.
- **Emotional goal:** make time passing visible, encouraging intentional living without nudges or gamification.

## Design Philosophy
- **Style:** Minimalist, dark, distraction-free.
- **Mood:** Calm, serious, reflective.
- **Inspiration:** Memento Mori, time awareness, stoic minimalism, visual accountability.

## UI Theme
- **Theme mode:** Dark.
- **Background:** #0B0B0D.
- **Text:**
  - Primary: #FFFFFF.
  - Secondary: #9A9A9A.
- **Accent:** #FFFFFF.
- **Typography:** Modern sans-serif (Inter / SF Pro style).
- **Icons:** Minimal line icons.

## Home Screen
- **Layout:** Single, scroll-free screen.
- **Header:**
  - Title: “Year Calendar”.
  - Subtitle: “Track the current year’s progress”.
  - Alignment: Center.
- **Date display (optional):**
  - Format: EEE MMM dd (e.g., Wed Dec 31).
  - Toggle in settings.
- **Time display (optional):**
  - Format: HH:mm (e.g., 08:00).
  - Style: large, subtle, semi-transparent.

## Calendar Visualization
- **Grid:** Centered dot grid with uniform spacing.
- **Dot shape:** Circle.
- **Dot size:** Small (adjustable to Medium via slider).
- **Total dots:** 365 (or 366 on leap years).

## Update Logic
- **Update frequency:** Daily at local midnight.
- **Time zone:** Device time zone.
- **Behavior:** On date change, mark previous day as completed and advance current-day highlight.

## Settings Screen
- **Show Time:** Toggle (default on).
- **Show Date:** Toggle (default on).
- **Start of Week:** Dropdown (Sunday/Monday).
- **Dot Size:** Slider (Small → Medium).
- **Reset Year:** Button with confirmation.

## Lock Screen Wallpaper Feature
- **Enabled:** Yes.
- **Description:** Generate a lock screen wallpaper that mirrors the dot-grid year progress.
- **Supported resolutions:** 1080x2400, 1440x3200.
- **Update frequency:** Daily.
- **Battery optimized:** Yes.

## Non-Functional Requirements
- **Ads:** None.
- **Login:** Not required.
- **Offline support:** Required.
- **Performance:** Instant load, low memory usage.
- **Privacy:** No data collection; analytics off by default.

## Future Extensions
- **Life Calendar Mode:**
  - Visualize lifespan with dots representing week/month.
  - Requires date of birth input.
- **Goal Overlay:**
  - Highlight dots for specific goals (e.g., gym, study, career).
  - Planned.
- **Streaks:**
  - Optional habit streaks without gamification.
  - Optional.

<template>
  <router-view />
</template>

<script setup>
// Use Vue Router to manage pages
</script>

<style>
/* ── Design tokens ──────────────────────────────────────────── */
:root {
  /* Backgrounds (dark simulation views) */
  --bg-base:     #0a0a0f;
  --bg-surface:  #0d0d18;
  --bg-card:     #12121e;
  --bg-elevated: #1a1a2e;

  /* Borders */
  --border-subtle: #1e1e2e;
  --border-muted:  #2e2e4e;

  /* Text */
  --text-primary:   #e8e8f0;
  --text-secondary: #8888aa;
  --text-tertiary:  #5a5a7a;

  /* Accent */
  --accent:    #6366f1;
  --accent-dim: rgba(99, 102, 241, 0.12);

  /* Semantic */
  --green:  #4ade80;
  --amber:  #f59e0b;
  --red:    #f87171;

  /* Typography */
  --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
}

/* ── Global reset ───────────────────────────────────────────── */
*, *::before, *::after {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: var(--font-sans);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #000000;
  background-color: #ffffff;
}

/* Focus-visible for keyboard nav */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* Scrollbar — dark for simulation views, light for home */
::-webkit-scrollbar { width: 6px; height: 6px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #333; border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: #555; }

button { font-family: inherit; cursor: pointer; }
</style>

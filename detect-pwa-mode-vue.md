# Vue router history mode for PWA vs browser

I want my Vue application's router to use `createWebHistory()` when it is accessed through a web browser and use `createMemoryHistory()` when it runs as a PWA. Is it possible?

---

Yes, this is possible. The trick is detecting PWA mode at startup and choosing the history implementation before passing it to `createRouter`.

The standard way to detect a PWA launch is via the `display-mode` media query, with a fallback for iOS Safari:

```js
import { createRouter, createWebHistory, createMemoryHistory } from 'vue-router'

const isPWA =
  window.matchMedia('(display-mode: standalone)').matches ||
  window.matchMedia('(display-mode: fullscreen)').matches ||
  window.matchMedia('(display-mode: minimal-ui)').matches ||
  window.navigator.standalone === true // iOS Safari

const router = createRouter({
  history: isPWA ? createMemoryHistory() : createWebHistory(),
  routes: [
    // ...
  ],
})

export default router
```

A few things worth knowing before you commit to this:

`createMemoryHistory()` doesn't touch the URL bar at all, and the history is wiped on reload. In a PWA that's often fine (it feels more app-like, and there's no browser back button to worry about), but it does mean deep links, shared URLs, and the OS-level swipe-back gesture won't restore a specific view. If you want app-like navigation while still preserving URLs for refresh/deep-linking, `createWebHashHistory()` is a middle-ground worth considering.

Also, the detection runs once at boot. If the user somehow transitions from browser → installed mode in the same session (rare), they'd need to relaunch for the router to switch. Not usually a problem, just something to be aware of.

If you'd like, I can also show how to make it work with Vite's PWA plugin or how to handle the case where you want some routes URL-synced and others not.
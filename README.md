git clone https://github.com/AP2003GIT/InstagramReelsIDE.git
cd InstagramReelsIDE
```

Create a virtual environment:

```powershell
python -m venv .venv
```

Install CodeReels and its dependencies using the virtual environment's interpreter:

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -e .
```

## Running

Run the Python module:

```powershell
.\.venv\Scripts\python.exe -m codereels
```

Alternatively, after activating the virtual environment, use the installed command:

```powershell
codereels
```

Instagram opens inside the CodeReels window. Sign in on the Instagram page itself; CodeReels never receives the password directly.

## Project structure

```text
src/codereels/
├── __main__.py              Application entry point
├── app.py                   Active pywebview/WebView2 application
├── config.py                Reserved for application configuration
├── browser/
│   ├── browser_controller.py
│   ├── navigation_policy.py
│   ├── secure_web_page.py
│   ├── instagram_session.py Legacy Qt WebEngine experiment
│   └── reels_window.py      Legacy Qt WebEngine experiment
└── state/
    ├── browser_settings.py
    └── window_state.py
```

The current execution path is intentionally small:

```text
codereels.__main__
        |
        v
CodeReelsApplication
        |
        v
pywebview
        |
        v
Microsoft Edge WebView2
        |
        v
instagram.com/reels
```

The files under `browser/` and `state/` are placeholders for the planned navigation, security, and settings layers. `instagram_session.py` and `reels_window.py` belong to an earlier PySide6 experiment and are not used by the active application. PySide6 is therefore not an installation dependency.

## Privacy and security

Authentication happens directly on Instagram's website inside WebView2. CodeReels does not expose a Python login form and does not read the user's password.

The browser profile may contain sensitive session cookies and local storage. It is kept in the user's platform-specific application-data directory rather than inside the repository. Do not copy, publish, or commit that profile directory.

## Known limitations

- The current application is Windows-only because it explicitly selects the Edge Chromium backend.
- It is a standalone desktop window, not yet a panel embedded in PyCharm, IntelliJ IDEA, or VS Code.
- Instagram may change its website or restrict embedded-browser behavior at any time.
- There are no custom keyboard shortcuts, feed controls, navigation restrictions, automated tests, or distraction-timer features yet.
- The repository contains several empty architectural placeholders that are not implemented.
- The normal personalized Reels feed is not available through Instagram's official API, so the prototype displays Instagram's website directly.

## Roadmap

- Remove the unused Qt WebEngine experiment.
- Add explicit navigation and popup policies.
- Add loading, offline, and authentication error states.
- Add configurable window dimensions and session preferences.
- Add useful tests for settings and navigation rules.
- Investigate a JetBrains JCEF host for PyCharm and IntelliJ IDEA.
- Investigate a VS Code Webview host while preserving the same security boundaries.

## Development principles

- Use only the official Instagram website or permitted public APIs.
- Never collect Instagram passwords or copy cookies from another browser.
- Never bypass authentication, DRM, provider restrictions, or access controls.
- Keep host integration separate from future application and state logic.

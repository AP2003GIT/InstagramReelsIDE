from pathlib import Path
from collections.abc import Sequence

import webview
from platformdirs import user_data_dir

#main class za apk
class CodeReelsApplication:
    REELS_URL = "https://www.instagram.com/reels/"

    def __init__(self, arguments: Sequence[str]) -> None:
        self.arguments = arguments
        self.storage_path = (
            Path(user_data_dir("CodeReels", "CodeReels"))
            / "browser-profile"
        )
        self.storage_path.mkdir(parents=True, exist_ok=True)

    def run(self) -> int:
        webview.create_window(
            title="CodeReels",
            url=self.REELS_URL,
            width=500,
            height=850,
            resizable=True,
        )

        webview.start(
            gui="edgechromium",
            debug=False,
            private_mode=False,
            storage_path=str(self.storage_path),
        )

        return 0


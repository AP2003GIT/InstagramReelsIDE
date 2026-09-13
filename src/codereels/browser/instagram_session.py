from pathlib import Path

from PySide6.QtCore import QObject, QStandardPaths, QUrl
from PySide6.QtWebEngineCore import QWebEnginePage, QWebEngineProfile


class InstagramSession(QObject):
    REELS_URL = QUrl("https://www.instagram.com/reels/")

    def __init__(self, parent: QObject | None = None) -> None:
        super().__init__(parent)

        app_data = Path(
            QStandardPaths.writableLocation(
                QStandardPaths.StandardLocation.AppDataLocation
            )
        )

        storage_path = app_data / "browser-profile"
        cache_path = app_data / "browser-cache"

        storage_path.mkdir(parents=True, exist_ok=True)
        cache_path.mkdir(parents=True, exist_ok=True)

        self.profile = QWebEngineProfile("CodeReels", self)
        self.profile.setPersistentStoragePath(str(storage_path))
        self.profile.setCachePath(str(cache_path))

        self.page = QWebEnginePage(self.profile, self)

    def open_reels(self) -> None:
        self.page.setUrl(self.REELS_URL)


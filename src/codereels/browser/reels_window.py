from PySide6.QtWidgets import QMainWindow
from PySide6.QtWebEngineWidgets import QWebEngineView

from codereels.browser.instagram_session import InstagramSession


class ReelsWindow(QMainWindow):
    def __init__(self, session: InstagramSession) -> None:
        super().__init__()

        self.session = session
        self.web_view = QWebEngineView(self)
        self.web_view.setPage(self.session.page)

        self.setWindowTitle("CodeReels")
        self.setMinimumSize(420, 700)
        self.resize(500, 850)
        self.setCentralWidget(self.web_view)

        self.session.open_reels()


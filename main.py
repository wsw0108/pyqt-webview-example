from PyQt6.QtWidgets import QApplication
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, QStandardPaths
from PyQt6.QtWebEngineCore import QWebEngineProfile, QWebEnginePage
import os
import pathlib

if __name__ == '__main__':

    import sys

    # app = QApplication(sys.argv)
    app = QApplication(sys.argv + ["--disable-web-security"])
    # app.setApplicationName('pyqt-webview-example')

    # defaultProfile is off-the-record
    # profile = QWebEngineProfile.defaultProfile()

    # A disk-based QWebEngineProfile should be destroyed on or before application exit, otherwise the cache and persistent data may not be fully flushed to disk.
    # XXX: parent is required?
    profile = QWebEngineProfile('Default', app)

    # WARN(?): Release of profile requested but WebEnginePage still not deleted. Expect troubles !
    # profile = QWebEngineProfile('Default')

    print('storage name: ' + profile.storageName())
    print('isOffTheRecord: {}'.format(profile.isOffTheRecord()))

    print('before set')
    print('cache path: ' + profile.cachePath())
    print('persist storage path: ' + profile.persistentStoragePath())
    print('http cache type: {}'.format(profile.httpCacheType().value))
    print('persist cookies police: {}'.format(profile.persistentCookiesPolicy().value))

    profile.setCachePath('')
    profile.setHttpCacheType(QWebEngineProfile.HttpCacheType.DiskHttpCache)
    profile.setPersistentStoragePath('')
    profile.setPersistentCookiesPolicy(QWebEngineProfile.PersistentCookiesPolicy.AllowPersistentCookies)

    print('after set')
    print('cache path: ' + profile.cachePath())
    print('persist storage path: ' + profile.persistentStoragePath())
    print('http cache type: {}'.format(profile.httpCacheType().value))
    print('persist cookies police: {}'.format(profile.persistentCookiesPolicy().value))

    view = QWebEngineView()

    # WARN: Release of profile requested but WebEnginePage still not deleted. Expect troubles !
    # page = QWebEnginePage(profile)

    # OK
    page = QWebEnginePage(profile, view)

    view.setPage(page)
    # test page: python -m http.server
    # page.load(QUrl('http://localhost:8000'))
    page.load(QUrl('https://bing.com'))
    # view.setUrl(QUrl('http://localhost:8000'))

    view.show()

    sys.exit(app.exec())

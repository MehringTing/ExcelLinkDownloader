import webview

from helpers.path_helper import resource_path
from services.downloader import Downloader


def main_window():
    api = Downloader()
    window = webview.create_window('ExcelLinkDownloader', resource_path('ui/index.html'), width=1080,
                                   height=760, min_size=(1080, 760), resizable=True, js_api=api, confirm_close=True
                                   )
    webview.start(debug=False)


if __name__ == '__main__':
    from multiprocessing import freeze_support
    freeze_support()

    main_window()

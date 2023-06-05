import webview
import threading
import time


def load_html(win):
    print(win)
    # win.load_url('http://www.p5w.net')
    win.load_url('../src/ui/index.html')


def change_title(win):
    """changes title every 3 seconds"""
    for i in range(1, 100):
        time.sleep(3)
        window.set_title("New Title #{}".format(i))


def on_loaded(win=None):
    print('on-loaded...')
    webview.windows[0].show()


if __name__ == '__main__':
    # t = threading.Thread(target=load_html, )
    # t.start()

    window = webview.create_window('Change window title')
    window.events.loaded += on_loaded
    webview.start(load_html, window)

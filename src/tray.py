"""
This example demonstrates running pywebview alongside with pystray to display a system tray icon.
"""
from PIL import Image
from pystray import Icon, Menu, MenuItem
import webview
import sys

if sys.platform == 'darwin':
    from multiprocessing import get_context

    ctx = get_context('spawn')
    Process = ctx.Process
    Queue = ctx.Queue

from threading import Thread
from queue import Queue


def onclose():
    global closed
    closed = True


queue = Queue()
window = webview.create_window('Webview', 'https://pywebview.flowrl.com/hello')
hide = False
closed = False
window.events.closed += onclose


def event_loop():
    global hide, window, closed
    while True:
        event = queue.get()
        print(event)
        if closed:
            break
        if event == 'open':
            if hide:
                window.show()
                window.restore()
                window.on_top = True
                hide = False

            else:
                window.hide()
                hide = True

        if event == 'exit':
            window.destroy()
            # break


def run_pystray(queue: Queue):
    def on_open(icon, item):
        queue.put('open')

    def on_exit(icon, item):
        icon.stop()
        queue.put('exit')

    image = Image.open('../pyinstaller/financial-report-helper/app.ico')
    menu = Menu(MenuItem('Open/Hide', on_open), MenuItem('Exit', on_exit))
    icon = Icon('Pystray', image, "Pystray", menu)
    icon.run()


if __name__ == '__main__':
    icon_thread = Thread(target=run_pystray, args=(queue,))
    icon_thread.daemon = True
    icon_thread.start()

    webview.start(event_loop)

    icon_thread.join()

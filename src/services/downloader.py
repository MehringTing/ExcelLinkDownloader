import os
import re
import subprocess

import requests
import webview

from multiprocessing import Pool


def get_hyperlink(text):
    pattern = r'\"(http[s]?://[^\"]+)\"'
    match = re.search(pattern, text)

    if match:
        return match.group(1)
    else:
        return ''


class Downloader:
    def __init__(self):
        self.settings = None

    def init(self) -> dict:
        return {
            'code': 0,
            'data': {
                'download_dir': os.path.join(os.path.expanduser('~'), 'Downloads'),
            },
        }

    def select_dir(self):
        window = webview.windows[0]
        file_tuple = window.create_file_dialog(webview.FOLDER_DIALOG)
        json = {
            'code': 0,
            'data': file_tuple[0] if file_tuple else '',
        }
        return json

    def replace(self, source: str, replace: dict) -> str:
        variables = re.compile(r'\[[a-zA-Z]+\]').findall(source)

        for v in variables:
            source = source.replace(v, replace.get(v[1:-1].upper()))

        return source

    def load(self, url: str, storage_path: str, filename: str):
        result = requests.get(url)

        if not os.path.isdir(storage_path):
            os.makedirs(storage_path, mode=777)

        with open(os.path.join(storage_path, filename), 'wb') as f:
            f.write(result.content)
            f.close()

        return True

    def deal_sheet_row(self, row: dict) -> bool:
        root_dirname = self.settings.get('root_dirname')
        dirname = self.settings.get('dirname')
        filename = self.settings.get('filename')

        if re.match(r'^([^:<>*?/|\\]+(/?[^:<>*?/|\\])?)+$', dirname):
            # replace column variable like [A], [B]
            dirname = self.replace(dirname, row)

        for col, cell_value in row.items():
            if not cell_value.startswith('http'):
                if cell_value.startswith('=HYPERLINK('):
                    cell_value = get_hyperlink(cell_value)
                else:
                    cell_value = ''

            if not cell_value:
                continue

            if filename:
                # replace column variable like [A], [B] etc and [EXT]
                if re.match(r'^[^:<>*?/|\\]+$', filename):
                    if re.match(r'\[[a-zA-A]+\]', filename):
                        if filename.endswith('[EXT]'):
                            _, ext = os.path.splitext(cell_value)
                            filename = filename.replace('[EXT]', ext)
                            filename = self.replace(filename, row)
                        else:
                            _, ext = os.path.splitext(cell_value)
                            filename = self.replace(filename, row)
                            filename += ext
                    else:
                        filename = os.path.basename(cell_value)
                else:
                    filename = os.path.basename(cell_value)
            else:
                filename = os.path.basename(cell_value)

            storage_path = os.path.join(root_dirname, dirname)
            self.load(cell_value, storage_path, filename)

        return True

    def download(self, data: dict, setting: dict) -> dict:
        raw = data.get('raw')

        if len(raw) < 1:
            return {
                'code': 0,
                'data': {},
            }

        self.settings = setting

        with Pool(processes=None) as p:
            p.map(self.deal_sheet_row, raw)

        return {
            'code': 0,
            'data': {},
            'message': '下载完成',
        }

    def show_result_dir(self, path: str = ''):
        if path:
            cmd = f'explorer /e, {path}'
            subprocess.call(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            pass
<template>
	<div>
		<div id="spreadsheet-container" style="width: 100%; height: 100%;"></div>
		<drop-menu :workbookReader="workbookReader" @trigger="clickDropMenu"></drop-menu>
		<setting-dialog :visible.sync="showSettingDialog" :settings="settings" @save="save"></setting-dialog>
		<div v-if="isStart" class="progress">
			<img src="@/assets/images/loading.gif" alt="" srcset="">
		</div>
	</div>
</template>

<script>
import Spreadsheet from 'x-data-spreadsheet';
import zhCN from 'x-data-spreadsheet/dist/locale/zh-cn';
import DropMenu from '@/components/DropMenu';
import SettingDialog from '@/components/SettingDialog';

Spreadsheet.locale('zh-cn', zhCN);

const XSDT_OPTIONS = {
	mode: 'edit', // edit | read
	showToolbar: true,
	showGrid: true,
	showContextmenu: true,
	view: {
		height: () => document.documentElement.clientHeight,
		width: () => document.documentElement.clientWidth,
	},
	row: {
		len: 1000,
		height: 25,
	},
	col: {
		len: 26,
		width: 100,
		indexWidth: 60,
		minWidth: 60,
	},
	style: {
		bgcolor: '#ffffff',
		align: 'left',
		valign: 'middle',
		textwrap: false,
		strike: false,
		underline: false,
		color: '#0a0a0a',
		font: {
			name: 'Helvetica',
			size: 10,
			bold: false,
			italic: false,
		},
	},
};

export default {
    name: "ExcelDownloader",
	components: {
		DropMenu,
		SettingDialog
	},
	data() {
		return {
			loaded: false,
			showSettingDialog: false,
			workbookReader: null,
			settings: {},
			sheetData: {},
			isStart: false,
		}
	},
	methods: {
		clickDropMenu({menu, data}) {
			console.log(menu, data)
			if (menu === 'open') {
				this.settings.dirname = data.dirname;
			} else if (menu === 'download-link') {
				this.sheetData = data.sheetData;
				this.showSettingDialog = true;
			} else {
				console.log('error')
			}
		},
		save(setting) {
			if (this.sheetData.raw.length < 1) {
				return false;
			}

			this.isStart = true;
			window.pywebview.api.download(this.sheetData, setting).then((res) => {
				if (res.code === 0) {
					const messager = this.$message({
						type: 'success',
						dangerouslyUseHTMLString: true,
						duration: 0,
						message: `${res.message}，<a id="output">点击打开文件夹</a>`
					});

					document.querySelector('#output').addEventListener('click', () => {
						window.pywebview.api.show_result_dir(setting.root_dirname);
						setTimeout(() => {
							messager.close();
						}, 500);
					});
				} else {
					console.log(res.message);
				}
				this.isStart = false;
			});
		},
	},
	created() {
		window.addEventListener('pywebviewready', () => {
			console.log('api ready:', window.pywebview.api);
			window.pywebview.api.init().then((res) => {
				console.log(res)
				if (res.code === 0) {
					this.settings = res.data;
					console.log(this.settings)
				}
			});
		});
	},
	mounted() {
		window.addEventListener('resize', () => {
			setTimeout(() => {
				document.querySelector('.x-spreadsheet-toolbar').style.width = '';
				document.querySelector('.x-spreadsheet-sheet').style.width = `${window.innerWidth}px`;
				document.querySelector('.x-spreadsheet-table').style.width = `${window.innerWidth}px`;
				document.querySelector('.x-spreadsheet-scrollbar.horizontal').style.width = `${window.innerWidth - 78}px`;
			}, 20);
		});

		this.workbookReader = new Spreadsheet('#spreadsheet-container', XSDT_OPTIONS);
		this.workbookReader.change(function (data) {
			console.log(data);
		});
	},
}
</script>

<style lang="scss" scoped>

.progress {
    position: absolute;
    bottom: 5px;
    right: 20px;
    img {
        width: 24px;
    }
}
a#output {
    cursor: pointer;
    font-weight: bold;
}
</style>
<template>
	<div>
		<div id="spreadsheet-container" style="width: 100%; height: 100%;"></div>
		<el-dropdown :hide-on-click="false" trigger="hover" :hide-timeout="50" class="dropdown-menu" @command="handleCommand">
			<span class="el-dropdown-link">
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"/><path d="M3 4h18v2H3V4zm0 7h18v2H3v-2zm0 7h18v2H3v-2z"/></svg>
			</span>
			<el-dropdown-menu slot="dropdown">
				<el-dropdown-item command="open">
				<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"><path fill="none" d="M0 0h24v24H0z"/><path d="M2.859 2.877l12.57-1.795a.5.5 0 0 1 .571.495v20.846a.5.5 0 0 1-.57.495L2.858 21.123a1 1 0 0 1-.859-.99V3.867a1 1 0 0 1 .859-.99zM4 4.735v14.53l10 1.429V3.306L4 4.735zM17 19h3V5h-3V3h4a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1h-4v-2zm-6.8-7l2.8 4h-2.4L9 13.714 7.4 16H5l2.8-4L5 8h2.4L9 10.286 10.6 8H13l-2.8 4z" fill="rgba(102,102,102,1)"/></svg>
				打开文件...</el-dropdown-item>
				<input type="file" name="" id="open-xlsx" accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" style="display: none;">
				<el-dropdown-item command="download-link">
					<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18"><path fill="none" d="M0 0h24v24H0z"/><path d="M3 19h18v2H3v-2zm10-5.828L19.071 7.1l1.414 1.414L12 17 3.515 8.515 4.929 7.1 11 13.17V2h2v11.172z" fill="rgba(102,102,102,1)"/></svg>
					下载链接文件...</el-dropdown-item>
			</el-dropdown-menu>
		</el-dropdown>
		<setting-dialog :visible.sync="showSettingDialog" :settings="settings" @save="save"></setting-dialog>
		<div v-if="isStart" class="progress">
			<img src="@/assets/images/loading.gif" alt="" srcset="">
		</div>
	</div>
</template>

<script>
import Spreadsheet from 'x-data-spreadsheet';
import zhCN from 'x-data-spreadsheet/dist/locale/zh-cn';
import XLSX from 'xlsx';
import { stox } from '@/assets/js/xlsxspread';
import SettingDialog from '@/components/SettingDialog';


Spreadsheet.locale('zh-cn', zhCN);
console.log(Spreadsheet);
console.log(XLSX)

const getExcelColumnName = function (index) {
	let colName = '';

	if (index >= 26) {
		colName = getExcelColumnName(index / 26 - 1);
		colName += String.fromCharCode(65 + index % 26);
	} else {
		colName += String.fromCharCode(65 + index);
	}

	return colName;
}

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
		SettingDialog,
	},
	data() {
		return {
			loaded: false,
			showSettingDialog: false,
			workbookReader: null,
			settings: {},
			sheetData: {
				raw: [],
				plain: [],
			},
			isStart: false,
		}
	},
	methods: {
		readWorkbookFromLocalFile(file, callback) {
			const reader = new FileReader();
			console.log(file)
			reader.onload = function (e) {
				const data = e.target.result;
				const workbook = XLSX.read(data, { type: 'binary' });
				console.log(workbook)
				console.log(XLSX.utils)
				console.log(XLSX.utils.sheet_to_json(workbook.Sheets[workbook.SheetNames[0]], {header: 'A', defval: ''}))

				if (callback) {
					callback(workbook);
				}
			}
			reader.readAsBinaryString(file);
		},
		handleCommand(command) {
			if (command === 'open') {
				const input = document.querySelector('#open-xlsx');
				input.click();
				input.addEventListener('change', (e) => {
					console.log(e)

					const file = e.target.files[0];
					this.settings.dirname = file.name.substring(0, file.name.lastIndexOf('.'));
					this.readWorkbookFromLocalFile(file, (wb) => {
						console.log(wb)
						const data = stox(wb);
						this.workbookReader.loadData(data);
						this.sheetData.raw = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]], {
							header: 'A',
							defval: '',
						});
					})
				});
			}

			if (command === 'download-link') {
				console.log('dddd', this.sheetData.raw)
				this.showSettingDialog = true;
				const data = this.workbookReader.getData();
				console.log(data, this.sheetData)
				const { rows } = data[0];

				delete rows.len;

				if (Object.keys(rows).length < 1) {
					// no data
				}

				const plain = [];
				const matrix = [];


				for (const rowIndex in rows) {
					const cells = rows[rowIndex]['cells'];
					const rowMap = {};

					for (const colIndex in cells) {
						console.log(colIndex, cells[colIndex])
						const { text } = cells[colIndex];
						const colName = getExcelColumnName(Number(colIndex));
						console.log({r: rowIndex, c: colIndex, v: text})
						plain.push({
							r: rowIndex,
							c: colIndex,
							v: text,
							cn: colName,
						});
						rowMap[colName] = text;
					}

					matrix.push(rowMap);
				}

				this.sheetData.plain = plain;
				this.sheetData.raw = matrix;
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
			console.log('resize')
			setTimeout(() => {
				document.querySelector('.x-spreadsheet-toolbar').style.width = '';
				document.querySelector('.x-spreadsheet-sheet').style.width = '';
			}, 50);
		});

		this.workbookReader = new Spreadsheet('#spreadsheet-container', XSDT_OPTIONS);
		this.workbookReader.change(function (data) {
			console.log(data);
		});
	},
}
</script>

<style lang="scss" scoped>
.dropdown-menu {
	position: absolute;
	right: 20px;
	top: 9px;
	z-index: 9;
	cursor: pointer;
}
.dot-menu {
	position: absolute;
	right: 15px;
	top: 10px;
	cursor: pointer;
}
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
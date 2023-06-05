<template>
    <el-dialog title="下载设置" width="600px" top="10vh" :visible.sync="showDialog" :append-to-body="true" :close-on-press-escape="false" :close-on-click-modal="false" @close="close">
        <el-form :model="form" size="small" label-width="100px" label-position="top">
            <el-form-item>
                <div slot="label">下载内容
                    <p class="form-item-tips">默认下载当前工作簿所有的链接文件</p>
                </div>
                <el-radio-group v-model="form.range_type">
                    <el-radio label="0">全部的链接</el-radio>
                    <el-radio label="1">所选区域的链接</el-radio>
                </el-radio-group>
            </el-form-item>
            <el-form-item label="单元格区域" v-if="form.range_type == 1">
                <div slot="label">单元格区域
                    <p class="form-item-tips">需要下载的链接数据所在的单元格列区域，多个列用英文逗号（,）隔开</p>
                </div>
                <el-input v-model="form.range" />
            </el-form-item>
            <el-form-item>
                <div slot="label">保存目录
                    <p class="form-item-tips">默认为当前用户的下载目录</p>
                </div>
                <el-input v-model="form.root_dirname" readonly>
                    <template slot="append">
                        <svg @click="openDir" t="1670296779688" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="24721" width="20" height="20"><path d="M759.466667 896h-618.666667c-53.333333 0-96-42.666667-96-96v-576C44.8 170.666667 87.466667 128 140.8 128h168.533333c21.333333 0 42.666667 6.4 59.733334 19.2l96 74.666667c12.8 10.666667 29.866667 14.933333 44.8 14.933333h249.6c53.333333 0 96 42.666667 96 96v102.4h-64v-102.4c0-17.066667-14.933333-32-32-32H509.866667c-29.866667 0-61.866667-10.666667-85.333334-29.866667l-96-74.666666c-6.4-2.133333-12.8-4.266667-19.2-4.266667H140.8c-17.066667 0-32 14.933333-32 32v578.133333c0 17.066667 14.933333 32 32 32h618.666667V896z" p-id="24722" fill="#666666"></path><path d="M778.666667 896H168.533333c-53.333333 0-96-42.666667-96-96 0-10.666667 2.133333-21.333333 6.4-32l104.533334-296.533333c12.8-38.4 49.066667-64 89.6-64h610.133333c53.333333 0 96 42.666667 96 96 0 10.666667-2.133333 21.333333-6.4 32L870.4 832c-12.8 38.4-51.2 64-91.733333 64zM273.066667 471.466667c-12.8 0-25.6 8.533333-29.866667 21.333333L138.666667 789.333333c-4.266667 10.666667-2.133333 21.333333 4.266666 29.866667 6.4 8.533333 14.933333 12.8 25.6 12.8h610.133334c12.8 0 25.6-8.533333 29.866666-21.333333l104.533334-296.533334c6.4-17.066667-2.133333-34.133333-19.2-40.533333-4.266667-2.133333-6.4-2.133333-10.666667-2.133333H273.066667z" p-id="24723" fill="#666666"></path></svg>
                    </template>
                </el-input>
            </el-form-item>
            <el-form-item>
                <div slot="label">文件夹名
                    <p class="form-item-tips">默认为当前工作簿的名称，支持多级文件夹，支持使用 [列] 引用列的数据，如 [A]，[A]/[B] </p>
                </div>
                <el-input v-model="form.dirname" />
            </el-form-item>
            <el-form-item>
                <div slot="label">文件名
                    <p class="form-item-tips">默认为该文件原始的文件名，支持使用 [列] 引用列的数据，使用 [EXT] 引用文件后缀。如 [A]，[A][EXT]，No.[B]，No.[B][EXT]</p>
                </div>
                <el-input v-model="form.filename" />
            </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
            <el-button @click="close">取 消</el-button>
            <el-button type="primary" @click="save">确 定</el-button>
        </div>
    </el-dialog>
</template>

<script>
export default {
    props: ['visible', 'settings'],
    data() {
        return {
            showDialog: false,
            form: {
                root_dirname: '',
                dirname: 'ExcelDownloader',
                range_type: '0',
                range: '',
                filename: '',
            },
            fields: [],
        }
    },
    watch: {
        visible(val) {
            this.showDialog = val;
            console.log(this.settings)
            if (val) {
                const { download_dir, dirname } = this.settings;
                this.form.root_dirname = download_dir;

                if (dirname) {
                    this.form.dirname = dirname;
                }
            }
        },
    },
    methods: {
        openDir() {
            window.pywebview.api.select_dir().then((res) => {
                if (res.code === 0) {
                    this.form.root_dirname = res.data;
                }
            });
        },
        save() {
            this.$emit('save', this.form);
            this.close();
        },
        close() {
            this.$parent.showSettingDialog = false;
        }
    },
    mounted() {

    }
}
</script>


<style lang="scss" scoped>
.form-item-tips {
    font-size: 12px;
    line-height: 1;
    color: #999;
}
</style>
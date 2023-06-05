<template>
    <div class="cover-container">
        <div class="menu-bar">
            <div class="menu-group">
                <el-button type="info" icon="el-icon-circle-plus-outline" @click="add('text')">文本</el-button>
                <el-button type="info" icon="el-icon-circle-plus-outline" @click="add('image')">图片</el-button>
            </div>
            <div class="tips">暂时只支持 company_shortname, company_code, report_date 三个变量，引用变量的格式为[变量名]， 如[company_code]
            </div>
            <el-button type="primary" @click="preview">保存配置</el-button>
        </div>
        <div class="main">
            <div class="property-container">
                <cover-property-form :element.sync="currentElement" @change="changeForm"></cover-property-form>
            </div>
            <div class="cover-editor">
                <div id="printable" class="page-container">
                    <div class="page" style="">
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <cell-cross></cell-cross>
                        <div class="page-break"></div>
                    </div>
                    <div class="page">
                        <cell-cross></cell-cross>
                        <div class="page-break"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
// import api from '../api';
import $ from 'jquery';
import print from 'print-js';
import CoverPropertyForm from "./CoverPropertyForm";
import CellCross from "@/components/cells/CellCross";
// import CellMeter from "@/components/cells/CellMeter";

export default {
    name: "CoverEditor",
    props: ['config'],
    components: {
        CoverPropertyForm,
        CellCross,
        // CellMeter,
    },
    data() {
        return {
            cover: '',
            cover_url: '',
            coverStyle: {
                width: '',
                height: '',
            },
            elements: [],
            items: [],
            currentIndex: 0,
            currentElement: {},
        }
    },
    computed: {
        elems() {
            return this.elements.map((item) => {
                return {
                    name: item.name,
                    type: item.type,
                    value: item.value,
                    placeholder: item.placeholder,
                    style: this.propertyToStyle(item),
                };
            });
        },
    },
    watch: {
        config(newVal) {
            console.log('data-config:', newVal);
        },
        cover_url(newVal) {
            console.log('cover-url:', newVal)
            const img = new Image();
            img.src = newVal;
            img.onload = () => {
                this.coverStyle.width = `${img.width}px`;
                this.coverStyle.height = `${img.height}px`;
            }
        },
        currentElement: {
            handler(newVal) {
                console.log('ccccccccccccccccccc', newVal)
                newVal.style = this.propertyToStyle(newVal)
                this.elements[this.currentIndex] = newVal;
            },
        }
    },
    methods: {
        change({id, url}) {
            this.cover = id;
            this.cover_url = url;
        },
        count(type) {
            if (type) {
                return this.elements.filter(item => item.type === type).length;
            }

            return this.elements.length;
        },
        add(type) {
            console.log(type)
        },
        handleMouseDown(index) {
            this.elements = this.elements.map((item, idx) => {
                item.active = index === idx;
                return item;
            });
            this.currentIndex = index;
            this.currentElement = this.elements[index];
        },
        remove(index) {
            this.elements.splice(index, 1);
        },
        async saveConfig() {
            const json = {
                cover: this.cover,
                cover_url: this.cover_url,
                elements: this.elems,
            };
            console.log(json);
        },
        changeForm(data) {
            console.log('data...:', data)
            this.$set(this.elements, this.currentIndex, data);
        },
        preview() {
            const style = `@page {
                                size: A4;
                                margin: 20mm 15mm 20mm 15mm;
                                mso-title-page: yes;
                                mso-page-orientation: portrait;
                                mso-header: header;
                                mso-footer: footer;
                           }
                           @media print {
                                html, body {
                                    margin: 0;
                                    padding: 0;
                                    width: 210mm;
                                    height: 297mm;
                                }
                                #printable {
                                    margin: 0;
                                }
                                div.page {
                                    margin: 0;
                                    padding: 0;
                                    page-break-inside: avoid !important;
                                    page-break-after: always !important;
                                    page-break-before: always !important;
                                    break-before: page !important;
                                }
                                div.page-break {
                                    page-break-after: always !important;
                                    page-break-before: avoid !important;
                                }
                           }`;
            print({
                printable: 'printable',
                type: 'html',
                documentTitle: 'abc...',
                scanStyles: false, // 不加此属性最后会多出一页空白页
                style: style,
                // font_size: '40px'
            });
        },
        printDom() {
            document.body.appendChild(document.querySelector('#printable'));
            window.print();
        }
    },
    mounted() {
        console.log($('.page'))
    }
}
</script>

<style lang="scss" scoped>
.cover-container {
    width: 100%;
    height: 100vh;
    overflow: hidden;

    .menu-bar {
        display: flex;
        justify-content: space-between;
        padding: 8px;
        height: 50px;
        background: #ffffff;
        border-bottom: 1px solid #cfcfcf;
        box-shadow: 0 0 6px 0 #dedede;

        .menu-group {
            display: flex;
        }

        > div {
            margin-right: 10px;
        }

        .el-button {
            padding: 0 20px;
        }
    }

    .main {
        display: flex;
        height: calc(100vh - 130px);
    }
}

.cover-editor {
    flex: 1;
    width: calc(100% - 2750px);
    height: calc(100vh - 50px);
    background: #efefef;
    overflow: auto;
    text-align: center;

    .page-container {
        position: relative;
        display: inline-block;
        margin: 50px auto;
        width: 210mm;
        text-align: left;
        .page {
            margin-bottom: 20px;
            padding: 20mm 15mm;
            width: 210mm;
            min-height: 297mm;
            background: #ffffff;
        }
    }

    .drag-item {
        position: absolute;
        padding: 0;
        min-height: 1em;
        background-color: #ffffff20;
        border: none;
        cursor: move;

        &.active {
            border: 1px solid #dddddd;
        }

        &:hover {
            .action {
                display: block;
            }
        }

        p {
            margin: 0;
        }

        img {
            max-width: 100%;
            max-height: 100%;
        }

        .action {
            position: absolute;
            right: -12px;
            top: -12px;
            width: 15px;
            height: 15px;
            border: 1px solid #fff;
            border-radius: 10px;
            color: #000000;
            background: #ffffff;
            font-size: 14px;
            text-align: center;
            cursor: pointer;
            display: none;
        }
    }
}

.tips {
    color: #999;
    line-height: 3;
    font-size: 12px;
}

.property-container {
    padding: 15px;
    width: 280px;
    height: 100vh;
    border-right: 1px;
    box-sizing: border-box;
}
</style>

<style lang="scss">
.property-container {
    .el-form-item {
        margin-bottom: 5px;
        text-align: left;
    }
}
</style>
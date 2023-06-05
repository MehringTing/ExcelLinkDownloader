<template>
    <el-form ref="form" :model="form" size="mini" label-width="80px">
        <el-form-item label="名称">
            <el-input v-model="form.name"></el-input>
        </el-form-item>
        <el-form-item label="类型">
            <el-select v-model="form.type" placeholder="请选择活动区域">
                <el-option label="文本" value="text"></el-option>
                <el-option label="图片" value="image"></el-option>
            </el-select>
        </el-form-item>
        <el-form-item label="内容">
            <el-input v-model="form.value"></el-input>
        </el-form-item>
        <el-form-item label="X">
            <el-input v-model="form.left">
                <template slot="append">px</template>
            </el-input>
        </el-form-item>
        <el-form-item label="Y">
            <el-input v-model="form.top">
                <template slot="append">px</template>
            </el-input>
        </el-form-item>
        <el-form-item label="层级">
            <el-input v-model="form.zIndex"></el-input>
        </el-form-item>
        <el-form-item label="宽">
            <el-input v-model="form.width">
                <template slot="append">px</template>
            </el-input>
        </el-form-item>
        <el-form-item label="高">
            <el-input v-model="form.height">
                <template slot="append">px</template>
            </el-input>
        </el-form-item>
        <el-form-item label="颜色">
            <el-color-picker v-model="form.color"></el-color-picker>
        </el-form-item>
        <el-form-item label="字号">
            <el-input v-model="form.fontSize">
                <template slot="append">px</template>
            </el-input>
        </el-form-item>
        <el-form-item label="字重">
            <el-radio-group v-model="form.fontWeight">
                <el-radio-button label="lighter">纤细</el-radio-button>
                <el-radio-button label="normal">正常</el-radio-button>
                <el-radio-button label="bold">加粗</el-radio-button>
            </el-radio-group>
        </el-form-item>
    </el-form>
</template>

<script>
export default {
    name: "CoverPropertyForm",
    props: ['element'],
    watch: {
        element(newVal) {
            this.form = newVal;
        },
        form: {
            handler() {
                // this.$emit('change', newVal);
            },
            deep: true,
        }
    },
    data() {
        return {
            form: {},
            rules: [],
        }
    },
    methods: {

    },
    mounted() {
        
    }
}
</script>

<style scoped>

</style>
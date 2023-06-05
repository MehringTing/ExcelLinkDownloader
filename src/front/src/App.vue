<template>
    <div id="app">
        <excel-downloader></excel-downloader>
    </div>
</template>

<script>
import ExcelDownloader from '@/pages/ExcelDownloader';

export default {
    name: 'App',
    components: {
        ExcelDownloader,
    },
    mounted() {

    }
}
</script>

<style lang="scss">
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    overflow: hidden;
}
</style>

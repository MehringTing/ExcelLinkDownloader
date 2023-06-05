<template>
    <div class="cell" :style="`position: relative; display: inline-flex; justify-content: center; align-items: center;width: ${cellWidth}px; height: ${cellWidth}px; font-family: ${fontFamily}; font-size: ${fontSize}px`">
        <svg xmlns="http://www.w3.org/2000/svg"
             :width="cellWidth"
             :height="cellWidth"
             style="position: absolute; top: 0; left: 0;">
            <rect id="svg_1"
                  :height="cellWidth"
                  :width="cellWidth"
                  :stroke="cellBorderColor"
                  stroke-width="2"
                  y="0"
                  x="0"
                  fill="none"/>
            <line :transform="`rotate(90 ${half},${half})`"
                  :stroke="cellBorderColor"
                  stroke-opacity="0.6"
                  stroke-dasharray="5,3"
                  stroke-linecap=""
                  stroke-linejoin=""
                  id="svg_2"
                  x1="0"
                  :y1="half"
                  x2="100"
                  :y2="half"
                  fill="none"/>
            <line :transform="`rotate(180 ${half},${half})`"
                  :stroke="cellBorderColor"
                  stroke-opacity="0.6"
                  stroke-dasharray="5,3"
                  stroke-linecap=""
                  stroke-linejoin=""
                  id="svg_3"
                  x1="0"
                  :y1="half"
                  x2="100"
                  :y2="half"
                  fill="none"/>
        </svg>
        <span :style="`position: relative; color: ${color}`">永</span>
    </div>
</template>

<script>
export default {
    name: "CellCross",
    props: {
        cellWidth: {
            type: Number,
            default: 60,
        },
        fontSize: {
            type: Number,
            default: 48,
        },
        fontFamily: {
            type: String,
            default: '楷体',
        },
        cellBorderColor: {
            type: String,
            default: '#ff0000',
        },
        color: {
            type: String,
            default: '#000000',
        },
    },
    computed: {
        half() {
            return this.cellWidth / 2;
        },
    },
    methods: {

    }
}
</script>

<style lang="scss" scoped>
.cell {
    box-sizing: border-box;
    svg {
        position: absolute;
        top: 0;
        left: 0;
    }
    span {
        position: relative;
    }
}
</style>
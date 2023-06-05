const {defineConfig} = require('@vue/cli-service');
const webpack = require('webpack');
const WebpackObfuscator = require('webpack-obfuscator');

const cdn = {
    js: [
        // 'js/jquery.min.js',
        // 'js/xspreadsheet/xspreadsheet.js',
        // 'js/xlsxspread.min.js',
        // 'js/xlsx.full.min.js',
    ],
    css: [

    ]
};

const isProduction = process.env.NODE_ENV === 'production';

module.exports = defineConfig({
    publicPath: '.',
    outputDir: isProduction ? '../ui' : 'dist',
    transpileDependencies: true,
    chainWebpack: config => {
        config.plugin('html').tap((args) => {
            if (isProduction) {
                args[0].cdn = cdn;
            }
            args[0].title = 'Abc';
            return args;
        });
        config.optimization.splitChunks({
            cacheGroups: {
                vendors: {
                    name: 'vendors',
                    test: /[\\/]node_modules[\\/]/,
                    priority: -10,
                    chunks: 'initial',
                }
            }
        });
        // config.plugin('provide').use(webpack.ProvidePlugin, [
        //     {
        //          $: 'jquery',
        //         jQuery: 'jquery',
        //         'window.jQuery': 'jquery',
        //     },
        // ]);
    },
    configureWebpack: config => {
        console.log('config',config)
        config.plugins.push(new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery',
        }));

        if (isProduction) {
            config.plugins.push(
                new WebpackObfuscator({
                    // rotateStringArray: true,
                }, [])
            )
        }
        config.externals = {
            // vue: 'Vue',
            // vuex: 'Vuex',
            // axios: 'axios',
            // jquery: 'JQuery',
            // 'element-ui': 'ElEMENT',
        }
    },
})

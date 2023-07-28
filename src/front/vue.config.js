const {defineConfig} = require('@vue/cli-service');
const webpack = require('webpack');
const WebpackObfuscator = require('webpack-obfuscator');

const cdn = {
    externals: {
        vue: 'Vue',
        'element-ui': 'ELEMENT',
        $: 'jquery',
        jQuery: 'jquery',
        'window.jQuery': 'jquery',
    },
    js: [
        'js/vue.min.js',
        'js/element-ui.min.js',
        // 'js/jquery.min.js',
    ],
    css: [
        // 'css/element-ui.min.css',
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

        // 移除相关的打包配置
        if (isProduction) {
            config.externals(cdn.externals);
        }

        // config.optimization.splitChunks({
        //     cacheGroups: {
        //         vendors: {
        //             name: 'vendors',
        //             test: /[\\/]node_modules[\\/]/,
        //             priority: -10,
        //             chunks: 'initial',
        //         }
        //     }
        // });

        config.optimization.splitChunks({
            cacheGroups: {
                vendors: {
                    name: (module, chunks, cacheGroupKey) => {
                      const moduleFileName = module.identifier().split('/').reduceRight(item => item);
                      const allChunksNames = chunks.map(item => item.name).join('~');
                      return `${cacheGroupKey}-${allChunksNames}-${moduleFileName}`;
                    },
                    test: /[\\/]node_modules[\\/]/,
                    chunks: 'all',
                    priority: -10,
                    minSize: 0,
                    minChunks: 2,
                },
                styles: {
                    name: 'styles',
                    test: /\.(css|less|scss)$/,
                    chunks: 'all',
                    enforce: true,
                },
            }
        });
    },
    configureWebpack: config => {
        // 通过 cdn 引入相关 js
        config.externals = isProduction ? cdn.externals : {};

        // if (isProduction) {
        //     config.plugins.push(
        //         new WebpackObfuscator({
        //             // rotateStringArray: true,
        //         }, [])
        //     )
        // }
    },
    // css: {
    //     loaderOptions: {
    //         css: {
    //             modules: {
    //                 auto: () => true,
    //             },
    //         }
    //     },
    //     sourceMap: !isProduction,
    // }
})

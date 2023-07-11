const {defineConfig} = require('@vue/cli-service');
const webpack = require('webpack');
const WebpackObfuscator = require('webpack-obfuscator');

const cdn = {
    js: [

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
    },
})

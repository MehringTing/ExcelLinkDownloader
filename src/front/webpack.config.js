// webpack.config.js
const JavaScriptObfuscator = require('webpack-obfuscator');

module.exports = {
//  entry: {
//    'abc': './test/input/index.js',
//    'cde': './test/input/index1.js'
//  },
  output: {
    publicPath: '.',
    path: 'dist',
    filename: '[name].js'
  },
  plugins: [
    new JavaScriptObfuscator({
      rotateUnicodeArray: true
      // 数组内是需要排除的文件
    }, ['abc.js'])
  ]
};

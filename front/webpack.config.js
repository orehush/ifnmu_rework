var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
module.exports = {
  mode: 'development',
  entry:  path.join(__dirname, './src/index'),
  output: {
    path: path.join(__dirname, 'assets/bundles'),
    filename: '[name]-[hash].js'
  },
  plugins: [
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.json'
    }),
  ],
  module: {
    rules: [
      {
        test: /\.jsx?$/,
        loader: 'babel-loader',
        exclude: /node_modules/,
      },
    ],
  },
}
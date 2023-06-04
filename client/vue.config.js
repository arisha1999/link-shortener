const NodePolyfillPlugin = require("node-polyfill-webpack-plugin");
const path = require("path");
const webpack = require("webpack");

module.exports = {
  configureWebpack: {
    resolve: {
      fallback: {
        fs: false,
        dns: require.resolve("node-libs-browser/mock/dns"),
        net: require.resolve("node-libs-browser/mock/net"),
      },
    },
    plugins: [
      new NodePolyfillPlugin(),
      new webpack.IgnorePlugin({
        resourceRegExp: /^pg-browserify$|^cloudflare:sockets$/,
      }),
    ],
  },
  transpileDependencies: true
}
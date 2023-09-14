module.exports = {
  devServer: {
    open: process.platform === 'darwin',
    host: '0.0.0.0',
    port: 8080,
  },
  transpileDependencies: ["vuetify"],
  chainWebpack: (config) => {
    config.module
      .rule("vue")
      .use("vue-loader")
      .loader("vue-loader")
      .tap((options) =>
        Object.assign(options, {
          transformAssetUrls: {
            "v-img": ["src", "lazy-src"],
            "v-card": "src",
            "v-card-media": "src",
            "v-responsive": "src",
          },
        }),
      );
  },
};
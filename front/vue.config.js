module.exports = {
  runtimeCompiler: true,
  devServer: {
    proxy: {
      "/pkr-api": {
        target: "http://370368-cv52016.tmweb.ru:8000/",
        pathRewrite: {
          "^/pkr-api": "/pkr",
        },
        cookieDomainRewrite: "",
        changeOrigin: true,
      },
    },
  },
};

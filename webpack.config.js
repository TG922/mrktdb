module.exports = {
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader"
        }
      },
      {
        test: /\.css$/i,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.scss$/i,
        use: [
          // Creates `style` nodes from JS strings
          'style-loader',
          // Translates CSS into CommonJS
          'css-loader',
          // Compiles Sass to CSS
          'sass-loader',],
      },
      {
        test: /\.(png|jpe?g|gif)$/i,
          use: [
            {
              loader: 'url-loader',
            },
          ],
      },
      {
        test: /\.svg$/i,
        use: [
          {
            loader: 'url-loader',
            options: {
              encoding: false,
            },
          },
        ],
      }
    ]
  }
};
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  // server: {
  //   // 跨域的写法
  //   proxy: {
  //     '/get_video': {
  //       target: 'http://127.0.0.1:8080', // 实际请求地址
  //       changeOrigin: true,
  //       rewrite: (path) => path.replace(/^\/get_video/, ""),
  //     },
  //   },
  // },
})

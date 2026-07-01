import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  build: {
    // Avoid lightningcss's native binary (platform-specific .node file) entirely —
    // it has caused missing-binary build failures across environments.
    cssMinify: 'esbuild',
  },
})

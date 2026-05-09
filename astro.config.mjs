import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import sitemap from '@astrojs/sitemap';
import icon from 'astro-icon';

export default defineConfig({
  site: 'https://lan13005.github.io',
  integrations: [tailwind({ applyBaseStyles: false }), sitemap(), icon()],
  output: 'static',
});

// Playwright configuration for Strands Shopper
// Headed mode for development, headless for production

module.exports = {
  use: {
    headless: process.env.PLAYWRIGHT_HEADLESS === '1',
    viewport: { width: 1280, height: 800 },
    screenshot: 'on',
    video: 'retain-on-failure',
    baseURL: 'https://www.heb.com/',
  },
};

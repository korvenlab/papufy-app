import type { CapacitorConfig } from "@capacitor/cli";

/**
 * Modo live (opcional): defina CAP_SERVER_URL=https://papufy.com
 * para carregar o site hospedado no WebView (útil no início do desenvolvimento).
 * Sem essa variável, o app usa o bundle em ./www (cópia do build do frontend).
 */
const liveUrl = process.env.CAP_SERVER_URL?.trim();

const config: CapacitorConfig = {
  appId: "com.papufy.app",
  appName: "Papufy",
  webDir: "www",
  backgroundColor: "#f0f9ff",
  server: liveUrl
    ? {
        url: liveUrl,
        cleartext: false,
      }
    : {
        androidScheme: "https",
        iosScheme: "https",
      },
  plugins: {
    SplashScreen: {
      launchShowDuration: 1500,
      launchAutoHide: true,
      backgroundColor: "#f0f9ff",
      showSpinner: false,
    },
    StatusBar: {
      style: "DARK",
      backgroundColor: "#f0f9ff",
    },
  },
};

export default config;

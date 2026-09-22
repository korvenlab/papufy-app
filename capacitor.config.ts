import type { CapacitorConfig } from "@capacitor/cli";

/**
 * O app é a versão mobile do site — mesmo UI do navegador no celular.
 * Carrega https://papufy.com no WebView (MobileShell, rotas, API iguais).
 *
 * Para build offline/bundle local no futuro:
 *   CAP_USE_BUNDLE=1  (usa ./www sincronizado do frontend)
 */
const useBundle = process.env.CAP_USE_BUNDLE === "1";
const siteUrl =
  process.env.CAP_SERVER_URL?.trim() || "https://papufy.com";

const config: CapacitorConfig = {
  appId: "com.papufy.app",
  appName: "Papufy",
  webDir: "www",
  backgroundColor: "#f0f9ff",
  server: useBundle
    ? {
        androidScheme: "https",
        iosScheme: "https",
      }
    : {
        url: siteUrl,
        cleartext: false,
        allowNavigation: [
          "papufy.com",
          "*.papufy.com",
          "*.vercel.app",
        ],
      },
  android: {
    allowMixedContent: false,
    backgroundColor: "#f0f9ff",
  },
  ios: {
    backgroundColor: "#f0f9ff",
    contentInset: "automatic",
    preferredContentMode: "mobile",
  },
  plugins: {
    SplashScreen: {
      launchShowDuration: 1200,
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

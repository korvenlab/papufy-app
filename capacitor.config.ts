import type { CapacitorConfig } from "@capacitor/cli";

/**
 * O app abre o site mobile (https://papufy.com) e acrescenta recursos do celular:
 * câmera, localização e notificações push (plugins nativos).
 * Uma atualização do site entra no app sem novo binário.
 *
 * Bundle local (sem URL remota): CAP_USE_BUNDLE=1
 */
const useBundle = process.env.CAP_USE_BUNDLE === "1";
const siteUrl =
  process.env.CAP_SERVER_URL?.trim() || "https://papufy.com";

const config: CapacitorConfig = {
  appId: "com.papufy.app",
  appName: "Papufy",
  webDir: "www",
  backgroundColor: "#ffffff",
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
    backgroundColor: "#ffffff",
  },
  ios: {
    backgroundColor: "#ffffff",
    contentInset: "automatic",
    preferredContentMode: "mobile",
  },
  plugins: {
    SplashScreen: {
      launchShowDuration: 1200,
      launchAutoHide: true,
      backgroundColor: "#ffffff",
      androidScaleType: "CENTER_INSIDE",
      showSpinner: false,
    },
    StatusBar: {
      style: "DARK",
      backgroundColor: "#ffffff",
    },
    PushNotifications: {
      presentationOptions: ["badge", "sound", "alert"],
    },
  },
};

export default config;

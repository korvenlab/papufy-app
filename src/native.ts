import { Capacitor } from "@capacitor/core";
import { StatusBar, Style } from "@capacitor/status-bar";
import { SplashScreen } from "@capacitor/splash-screen";
import { App as CapApp } from "@capacitor/app";

/**
 * Inicialização nativa — importar no entry do frontend quando o bundle
 * for empacotado no app. Por enquanto o shell Capacitor já aplica
 * splash/status bar via capacitor.config.ts.
 */
export async function initNativeShell(): Promise<void> {
  if (!Capacitor.isNativePlatform()) return;

  try {
    await StatusBar.setStyle({ style: Style.Dark });
    await StatusBar.setBackgroundColor({ color: "#f0f9ff" });
  } catch {
    /* web / plugin ausente */
  }

  try {
    await SplashScreen.hide();
  } catch {
    /* ignore */
  }

  CapApp.addListener("backButton", ({ canGoBack }) => {
    if (canGoBack) {
      window.history.back();
    } else {
      CapApp.exitApp();
    }
  });
}

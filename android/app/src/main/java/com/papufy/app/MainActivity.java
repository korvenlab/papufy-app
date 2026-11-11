package com.papufy.app;

import android.os.Bundle;
import androidx.core.splashscreen.SplashScreen;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Tem de rodar antes do super: o tema da abertura não é AppCompat
        // e a atividade fecha na hora se o tema não for trocado aqui.
        SplashScreen.installSplashScreen(this);
        super.onCreate(savedInstanceState);
    }
}

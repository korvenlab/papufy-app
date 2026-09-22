# Papufy App — Capacitor

O app nativo exibe **a mesma experiência mobile do navegador** em
[papufy.com](https://papufy.com) (MobileShell, bottom nav, rotas e API).

Não é um app redesenhado: é o site mobile dentro do WebView.

## Como funciona

Por padrão o Capacitor abre `https://papufy.com` no aparelho.
O que você vê no Chrome/Safari em modo celular = o que o app mostra.

```
papufy-app/       ← casco nativo (Android / iOS)
papufy-frontend/  ← UI (deploy Vercel → papufy.com)
papufy-backend/    ← API Render + Supabase
```

## Setup

```bash
cd D:\Projetos\papufy-app
npm install
npx cap sync
```

Abrir projetos nativos (quando for testar no device/emulador):

```bash
npx cap open android   # Android Studio
npx cap open ios       # Xcode (só macOS)
```

## Bundle local (opcional, depois)

Se um dia quiser embutir o `dist` do frontend em vez do site ao vivo:

```powershell
$env:CAP_USE_BUNDLE="1"
npm run sync:web
npx cap sync
```

## IDs

- App ID: `com.papufy.app`
- Nome: Papufy

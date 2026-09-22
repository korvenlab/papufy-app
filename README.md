# Papufy App — Capacitor

Shell nativo (Android / iOS) em cima do frontend React + Vite já existente.

## Estrutura

```
papufy-app/          ← este repositório
papufy-frontend/     ← UI web (irmã em D:\Projetos\papufy-frontend)
papufy-backend/      ← API Render + Supabase
```

## Pré-requisitos

- Node 20+
- Android Studio (Android)
- Xcode em macOS (iOS)
- Contas Apple Developer / Google Play (para publicar)

## Setup

```bash
cd D:\Projetos\papufy-app
npm install
npm run cap:sync
```

`cap:sync` copia o build de `../papufy-frontend/dist` para `www/` e roda `npx cap sync`.

Se o frontend ainda não tiver `dist`, o script tenta buildar o frontend (`npm run build` lá).

### Abrir no Android Studio

```bash
npm run cap:android
```

### Modo live (WebView apontando para produção)

Útil no começo, sem rebundle a cada mudança:

```powershell
$env:CAP_SERVER_URL="https://papufy.com"
npx cap sync
npx cap open android
```

## Variáveis do frontend (Vercel)

O app usa a mesma API. No bundle, o frontend já vem com `VITE_API_URL` apontando ao Render.

Para recovery de senha no app, configure no Supabase as Redirect URLs do domínio (e deep links depois).

## Bundle ID

- Android / iOS: `com.papufy.app`
- Nome: Papufy

## Próximos passos

1. Ícones e splash (`resources/` + `@capacitor/assets`)
2. Deep links / Universal Links
3. Ajustar CORS no backend para origem Capacitor se necessário
4. TestFlight + Internal testing Play

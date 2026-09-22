# Papufy — prontidão para as lojas

App ID: `com.papufy.app` · Versão: `1.0.0` (versionCode / build `1`)

O app carrega **https://papufy.com** (mesma UX mobile do navegador).
Atualizações de tela/API = deploy Vercel/Render. Build nativo só para casco/ícone/plugins.

## URLs obrigatórias (já no site após deploy do frontend)

| Uso | URL |
|-----|-----|
| Privacidade | https://papufy.com/privacidade |
| Termos | https://papufy.com/termos |
| Suporte | contato@papufy.com |
| Site | https://papufy.com |

## Google Play

1. Conta Google Play Console (US$ 25, única).
2. Criar app → tipo **App** → gratuito.
3. **Data safety**: dados de conta, localização (opcional), fotos, mensagens, pagamento via provedor.
4. **Content rating** (IARC).
5. Política de privacidade: URL acima.
6. Screenshots: telefone (mín. 2). Use o site mobile ou emulador.
7. Ícone 512×512: `store/icon-1024.png` (redimensionar se a loja pedir 512).
8. Assinar release:
   ```powershell
   keytool -genkey -v -keystore papufy-upload.keystore -alias papufy -keyalg RSA -keysize 2048 -validity 10000
   ```
   Em `android/keystore.properties` (não versionar):
   ```
   PAPUFY_UPLOAD_STORE_FILE=../papufy-upload.keystore
   PAPUFY_UPLOAD_STORE_PASSWORD=...
   PAPUFY_UPLOAD_KEY_ALIAS=papufy
   PAPUFY_UPLOAD_KEY_PASSWORD=...
   ```
   Ou passe as props no `gradle.properties` local.
9. Build AAB:
   ```powershell
   cd android
   .\gradlew bundleRelease
   ```
10. Contas pessoais novas: teste fechado ≥ 12 testadores / 14 dias antes da produção.

## Apple App Store

1. Apple Developer Program (US$ 99/ano).
2. App Store Connect → novo app → Bundle ID `com.papufy.app`.
3. Privacy Nutrition Labels (alinhados à Política).
4. Screenshots iPhone (6.7" e 6.1" no mínimo recomendado).
5. Review notes (sugerido):
   > Papufy é marketplace de serviços locais (anúncios, chat, reputação e pagamentos). O WebView exibe a plataforma Papufy (papufy.com), produto próprio — não é um browser genérico. Conta de teste: [e-mail] / [senha].
6. Build no Mac: `npx cap open ios` → Archive → Upload.
7. Export compliance: encryption isenta (`ITSAppUsesNonExemptEncryption = false`).

## Checklist técnico (repo)

- [x] Bundle ID `com.papufy.app`
- [x] Ícones / splash gerados
- [x] Permissões câmera, fotos, localização (Android + iOS)
- [x] Orientação portrait no celular
- [x] Deep link https papufy.com (Android; Associated Domains iOS — completar no Apple Developer)
- [x] Página `/privacidade` no frontend
- [ ] Contas das lojas
- [ ] Keystore / certificados de distribuição
- [ ] Screenshots finais
- [ ] Submissão

## Regenerar ícones (logo oficial do frontend)

```powershell
npm run icons
npx cap sync
```

Fonte: `../papufy-frontend/public/nome.png`

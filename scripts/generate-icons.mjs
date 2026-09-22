/**
 * Gera ícone/splash 1024 a partir da logo oficial (public/nome.png).
 * App Store não aceita transparência no ícone — fundo sólido.
 */
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import sharp from "sharp";

const __dirname = dirname(fileURLToPath(import.meta.url));
const appRoot = resolve(__dirname, "..");
const logoPath = resolve(appRoot, "..", "papufy-frontend", "public", "nome.png");
const resourcesDir = join(appRoot, "resources");
const storeDir = join(appRoot, "store");

const SIZE = 1024;
/** Fundo alinhado à arte oficial (logo azul sobre preto). */
const BG = { r: 11, g: 11, b: 11, alpha: 1 };

mkdirSync(resourcesDir, { recursive: true });
mkdirSync(storeDir, { recursive: true });

const logoBuf = await sharp(logoPath)
  .resize({
    width: Math.round(SIZE * 0.78),
    height: Math.round(SIZE * 0.42),
    fit: "inside",
    withoutEnlargement: false,
  })
  .png()
  .toBuffer();

const logoMeta = await sharp(logoBuf).metadata();
const left = Math.round((SIZE - (logoMeta.width ?? 0)) / 2);
const top = Math.round((SIZE - (logoMeta.height ?? 0)) / 2);

const square = await sharp({
  create: {
    width: SIZE,
    height: SIZE,
    channels: 4,
    background: BG,
  },
})
  .composite([{ input: logoBuf, left, top }])
  .png()
  .toBuffer();

const outIcon = join(resourcesDir, "icon.png");
const outSplash = join(resourcesDir, "splash.png");
const outSplashDark = join(resourcesDir, "splash-dark.png");
const outIconOnly = join(resourcesDir, "icon-only.png");
const outStore = join(storeDir, "icon-1024.png");

await sharp(square).toFile(outIcon);
copyFileSync(outIcon, outSplash);
copyFileSync(outIcon, outSplashDark);
copyFileSync(outIcon, outIconOnly);
copyFileSync(outIcon, outStore);

console.log("[icons] Logo oficial →", outIcon);
console.log("[icons] Store →", outStore);

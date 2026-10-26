import { readdirSync, mkdirSync, unlinkSync, existsSync } from "node:fs";
import { join } from "node:path";
import sharp from "sharp";

const srcDir = "store/screenshots/app-store-iphone-6.9";
const outDir = "store/screenshots/google-play-phone";
mkdirSync(outDir, { recursive: true });

for (const file of readdirSync(srcDir).filter(
  (f) => f.endsWith(".png") && !f.startsWith("_")
)) {
  const meta = await sharp(join(srcDir, file)).metadata();
  const cropH = Math.round((meta.width ?? 1080) * (16 / 9));
  await sharp(join(srcDir, file))
    .extract({
      left: 0,
      top: 0,
      width: meta.width ?? 1080,
      height: Math.min(cropH, meta.height ?? cropH),
    })
    .resize(1080, 1920, { fit: "fill", kernel: "lanczos3" })
    .flatten({ background: "#f8fafc" })
    .png()
    .toFile(join(outDir, file));
  console.log("play", file);
}

const logo = await sharp("../papufy-frontend/public/nome.png")
  .resize({ width: 520, height: 150, fit: "inside" })
  .png()
  .toBuffer();
const lm = await sharp(logo).metadata();
const caption = Buffer.from(
  `<svg width="1024" height="80" xmlns="http://www.w3.org/2000/svg">
    <text x="512" y="52" text-anchor="middle" font-family="Arial, sans-serif" font-size="34" font-weight="700" fill="#ffffff">Quem precisa e quem faz, na sua cidade</text>
  </svg>`
);

await sharp({
  create: {
    width: 1024,
    height: 500,
    channels: 3,
    background: { r: 29, g: 111, b: 191 },
  },
})
  .composite([
    {
      input: logo,
      left: Math.round((1024 - (lm.width ?? 0)) / 2),
      top: 155,
    },
    { input: caption, left: 0, top: 340 },
  ])
  .jpeg({ quality: 92 })
  .toFile("store/screenshots/google-play-feature-1024x500.jpg");

const test = "store/screenshots/_test-login.png";
if (existsSync(test)) unlinkSync(test);
console.log("feature ok");

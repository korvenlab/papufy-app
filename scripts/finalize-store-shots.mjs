import { renameSync, unlinkSync, readdirSync } from "node:fs";
import { join } from "node:path";
import sharp from "sharp";

const dir = "store/screenshots/app-store-ipad-13";
for (const file of readdirSync(dir)) {
  if (file.endsWith(".out.png")) {
    const dest = join(dir, file.replace(".out.png", ""));
    unlinkSync(dest);
    renameSync(join(dir, file), dest);
  }
}
for (const file of readdirSync(dir)) {
  if (file.startsWith("_")) unlinkSync(join(dir, file));
}

const logo = await sharp("../papufy-frontend/public/nome.png")
  .resize({ width: 560, height: 160, fit: "inside" })
  .png()
  .toBuffer();
const lm = await sharp(logo).metadata();
const caption = Buffer.from(
  `<svg width="1024" height="70" xmlns="http://www.w3.org/2000/svg"><text x="512" y="46" text-anchor="middle" font-family="Arial, sans-serif" font-size="32" font-weight="700" fill="#0f172a">Quem precisa e quem faz, na sua cidade</text></svg>`
);

await sharp({
  create: {
    width: 1024,
    height: 500,
    channels: 3,
    background: { r: 244, g: 249, b: 252 },
  },
})
  .composite([
    {
      input: logo,
      left: Math.round((1024 - (lm.width ?? 0)) / 2),
      top: 145,
    },
    { input: caption, left: 0, top: 345 },
  ])
  .jpeg({ quality: 92 })
  .toFile("store/screenshots/google-play-feature-1024x500.jpg");

for (const file of readdirSync(dir)) {
  const m = await sharp(join(dir, file)).metadata();
  console.log(file, m.width, m.height);
}

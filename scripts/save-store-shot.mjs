import { readdirSync, readFileSync, mkdirSync } from "node:fs";
import { join } from "node:path";
import sharp from "sharp";

const [, , name, folder = "app-store-iphone-6.9", scaleArg = "1"] = process.argv;
const scale = Number(scaleArg) || 1;
if (!name) {
  console.error("uso: node scripts/save-store-shot.mjs 01-home.png [pasta]");
  process.exit(1);
}

const logsDir = "C:/Users/almei/.cursor/browser-logs";
const files = readdirSync(logsDir)
  .filter((f) => f.startsWith("cdp-response-Page.captureScreenshot"))
  .map((f) => ({ f, t: readFileSync(join(logsDir, f)).length }))
  .sort((a, b) => a.f.localeCompare(b.f));

const latest = files.at(-1);
if (!latest) throw new Error("nenhum screenshot CDP");

const json = JSON.parse(readFileSync(join(logsDir, latest.f), "utf8"));
const buf = Buffer.from(json.data, "base64");
const outDir = join("store", "screenshots", folder);
mkdirSync(outDir, { recursive: true });
const out = join(outDir, name);

let pipeline = sharp(buf).flatten({ background: "#f8fafc" });
if (scale !== 1) {
  const meta = await sharp(buf).metadata();
  pipeline = pipeline.resize(
    Math.round((meta.width ?? 1) * scale),
    Math.round((meta.height ?? 1) * scale),
    { kernel: "lanczos3" }
  );
}
await pipeline.png().toFile(out);
const meta = await sharp(out).metadata();
console.log(latest.f, "->", out, meta.width, meta.height);

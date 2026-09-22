import { copyFileSync, cpSync, existsSync, mkdirSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { execSync } from "node:child_process";

const __dirname = dirname(fileURLToPath(import.meta.url));
const appRoot = resolve(__dirname, "..");
const wwwDir = join(appRoot, "www");
const frontendRoot = resolve(appRoot, "..", "papufy-frontend");
const frontendDist = join(frontendRoot, "dist");

function ensurePlaceholderWww() {
  mkdirSync(wwwDir, { recursive: true });
  writeFileSync(
    join(wwwDir, "index.html"),
    `<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="viewport-fit=cover, width=device-width, initial-scale=1.0" />
    <title>Papufy</title>
    <style>
      body { font-family: system-ui, sans-serif; margin: 0; min-height: 100dvh; display: grid; place-items: center; background: #f0f9ff; color: #0f172a; }
      main { text-align: center; padding: 2rem; }
      a { color: #0284c7; font-weight: 600; }
    </style>
  </head>
  <body>
    <main>
      <h1>Papufy</h1>
      <p>Bundle web ainda não sincronizado.</p>
      <p>Rode <code>npm run sync:web</code> com o frontend buildado,<br />ou use <code>CAP_SERVER_URL</code> apontando para o site.</p>
      <p><a href="https://papufy.com">Abrir papufy.com</a></p>
    </main>
  </body>
</html>
`
  );
}

function buildFrontendIfNeeded() {
  if (existsSync(join(frontendDist, "index.html"))) return true;
  if (!existsSync(join(frontendRoot, "package.json"))) {
    console.warn("[sync:web] papufy-frontend não encontrado em", frontendRoot);
    return false;
  }
  console.log("[sync:web] Buildando papufy-frontend...");
  try {
    execSync("npm run build", { cwd: frontendRoot, stdio: "inherit" });
    return existsSync(join(frontendDist, "index.html"));
  } catch {
    console.warn(
      "[sync:web] Build do frontend falhou (faltam envs VITE_*?). Usando placeholder."
    );
    return false;
  }
}

function syncDist() {
  if (existsSync(wwwDir)) {
    rmSync(wwwDir, { recursive: true, force: true });
  }
  mkdirSync(wwwDir, { recursive: true });
  cpSync(frontendDist, wwwDir, { recursive: true });
  console.log("[sync:web] Copiado", frontendDist, "→", wwwDir);
}

const ok = buildFrontendIfNeeded();
if (ok) {
  syncDist();
} else {
  ensurePlaceholderWww();
  console.log("[sync:web] Placeholder em www/ (ok para cap add / modo live).");
}

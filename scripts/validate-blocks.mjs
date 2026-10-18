// Offline schema check only. No URL is contacted and no token is read.
import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const deps = resolve(process.argv[2] ?? join(root, ".validation"));
const config = await import(pathToFileURL(join(deps, "node_modules/@continuedev/config-yaml/dist/index.js")));
const catalog = JSON.parse(await readFile(join(root, "catalog.json"), "utf8"));
for (const service of catalog.services) {
  const yaml = await readFile(join(root, "blocks", service.slug, "block.yaml"), "utf8");
  const parsed = config.parseConfigYaml(yaml);
  assert.equal(parsed.schema, "v1");
  assert.equal(parsed.mcpServers.length, 1);
  const server = parsed.mcpServers[0];
  assert.equal(server.name, service.title);
  assert.equal(server.url, service.endpoint_url);
  assert.equal(server.type, "streamable-http");
  assert.equal(server.requestOptions.headers.Authorization, "Bearer ${{ secrets.ACEDATACLOUD_API_TOKEN }}");
  console.log(`${service.slug}: PASS`);
}

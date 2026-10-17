# Ace Data Cloud service blocks for Continue

Install only the service you need: each directory contains an independently loadable MCP block and its own English/Chinese token-to-result guide. Runtime tools remain in the existing Ace MCP servers; this repository does not create another provider backend.

**Not a Continue Hub listing.** Current Continue has removed Hub loading. These are local candidates plus publication materials; they do not mean users can search the official Hub and install them. See [distribution evidence](docs/distribution.md).

| Service | Independent block and guide | Existing runtime source |
| --- | --- | --- |
| Suno by Ace Data Cloud | [suno](blocks/suno) | [SunoMCP](https://github.com/AceDataCloud/SunoMCP) |
| Seedance by Ace Data Cloud | [seedance](blocks/seedance) | [SeedanceMCP](https://github.com/AceDataCloud/SeedanceMCP) |
| HappyHorse by Ace Data Cloud | [happyhorse](blocks/happyhorse) | [HappyHorseMCP](https://github.com/AceDataCloud/HappyHorseMCP) |
| GPT Image by Ace Data Cloud | [gpt-image](blocks/gpt-image) | [OpenAIMCP](https://github.com/AceDataCloud/OpenAIMCP) |
| Nano Banana by Ace Data Cloud | [nano-banana](blocks/nano-banana) | [NanoBananaMCP](https://github.com/AceDataCloud/NanoBananaMCP) |

Use your own Ace account and API token. Model access, tool permission and current prices must be checked before a real operation. Generation can be billed; task polling uses the same returned ID. No successful Continue generation, official listing or commercial conversion is claimed.

`GPT Image` uses the existing OpenAI MCP and exposes its other tools as well; restrict token APIs. Named blocks do not filter tool permissions. Full runtime contracts come from each existing MCP server.

The named Ace model Provider is a separate Continue source contribution, not required to load these media blocks with another configured tool-capable model.

## Validation

```bash
python3 -m unittest discover -s tests -v
node scripts/validate-blocks.mjs /path/to/npm-prefix
```

Normal CI uses test discovery. Validation must not submit a model/media generation. Official screenshot sources and dates are in [assets/source.json](assets/source.json).

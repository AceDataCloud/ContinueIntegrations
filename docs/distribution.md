# Official distribution status — 2026-10-19

Continue's current source explicitly removed Hub package loading and slug resolution:

- [CLI hubLoader](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/extensions/cli/src/hubLoader.ts): `Hub package loading has been removed`.
- [RegistryClient](https://github.com/continuedev/continue/blob/5522c6f44ca0ac3528b37244818fbfa39b5af470/packages/config-yaml/src/registryClient.ts): slug-based package resolution is unsupported.
- [Official homepage](https://continue.dev/): Continue joined Cursor; official repository README says no longer actively maintained.
- [Allowed local MCP configuration](https://docs.continue.dev/customize/deep-dives/mcp): standalone YAML includes name/version/schema and a list of MCP servers.

The previous Hub Models/MCP/Rules/Prompts/Agents distribution mechanism cannot currently be published through a verified active path. A repository or a local install is not an official searchable listing. No evidence of a separate current Skills store exists. We will not create duplicate publisher identities, accept agreements, or invent a Hub URL.

Five independent service brands are published as standalone installable files on the [GitHub source releases page](https://github.com/AceDataCloud/ContinueIntegrations/releases/latest), with submission-ready metadata if the platform reopens a catalog; they share one packaging source here because there is no official mechanism requiring five repositories. No rule forbidding separate service brands was found; the blocker is removed distribution infrastructure, not an asserted duplicate rule.

The native `acedatacloud` Provider contribution is [upstream #13394](https://github.com/continuedev/continue/pull/13394), separate from the [five-service official examples contribution #13396](https://github.com/continuedev/continue/pull/13396). Upstream review, CLA, merge, official package release and ordinary user installation remain separate gates. No CLA has been signed by this automation.

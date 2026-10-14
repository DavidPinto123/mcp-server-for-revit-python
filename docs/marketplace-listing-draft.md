# Marketplace listing draft

**Title:** MCP Server for Revit - Python

**Type:** Free desktop MCP connector; Windows 64-bit; local `stdio` server paired
with a pyRevit extension. No Autodesk endorsement or certification claimed.

**Short description:** Connect a local MCP client to Autodesk Revit for model
inspection, family placement, view visualization and reviewed Python automation.

**Description:** This open-source connector exposes 20 tools through the Model
Context Protocol. It reads model/level/family/view information, exports a view as
an image, places loaded family instances, applies or clears view color overrides,
opens/saves/closes/synchronizes documents, discovers or launches Revit, and executes
user-reviewed IronPython in Revit. Local Windows-user pairing is required. Model
changes and Python requests are displayed for review in Revit before execution.
Python runs with the Windows user's permissions and is not sandboxed. Your chosen
AI client may forward tool responses to its provider; review its privacy settings.

**License:** MIT; the repository retains its original attribution and license.

**Compatibility:** Revit 2027 is required for publication but has not been proven
for this PR by a live runtime test. Do not select compatibility checkboxes until
validation is recorded. pyRevit and Python 3.11+ are dependencies.

**Privacy URL:** The public `PRIVACY.md` URL for the final approved release. Do not
link a nonexistent default-branch document or claim a draft policy is published.

## Reviewer quick start for the source candidate

These steps validate the source candidate and are not a finished Marketplace
installer. Final dependency/bundle packaging must be agreed with Autodesk.

1. Install a supported pyRevit version into Revit 2027. Add the exact candidate
   checkout as a `.extension` folder and enable the extension/Routes server.
2. Start Revit with a non-confidential disposable test model. Confirm the MCP tab
   and Bridge panel exist. Choose Connect and review the consent notice.
3. From the candidate directory run `uv sync --frozen` followed by
   `uv run python main.py` as the chosen MCP client's stdio command. Use an absolute
   `--directory` path in client configuration so the exact candidate is selected.
4. Verify all manifest tools are listed. Test read tools, image export and all
   modification/lifecycle tools on disposable models. For writes/code, test both
   declining and accepting the Revit review prompt. Verify rollback/error behavior.
5. Choose Disconnect and verify tool calls are denied. Reconnect and verify old
   bearer headers are rejected. Confirm HTTP modes reject missing credentials and
   browser-originated requests. Never publish or paste the pairing token.
6. Remove the extension and Disconnect pairing; verify expected uninstall behavior
   and preserve user-created model files. Do not test destructive lifecycle actions
   on an unsaved or production model.

## Client example

```json
{
  "mcpServers": {
    "Revit Python": {
      "command": "uv",
      "args": ["run", "--frozen", "--directory", "C:/path/to/revit-mcp-python.extension", "python", "main.py"]
    }
  }
}
```

For multiple Revit instances set `REVIT_PORT` to the selected instance's pyRevit
Routes port. All pairings for the same Windows user share one revocation boundary.

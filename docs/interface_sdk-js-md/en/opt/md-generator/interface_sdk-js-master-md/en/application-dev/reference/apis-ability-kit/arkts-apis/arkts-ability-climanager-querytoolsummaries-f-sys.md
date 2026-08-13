# queryToolSummaries (System API)

## Modules to Import

```TypeScript
import { cliManager } from '@kit.AbilityKit';
```

## queryToolSummaries

```TypeScript
function queryToolSummaries(): Promise<Array<ToolSummary>>
```

Query all tool summary information. The summary information only contains the fields: name, description, version.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.QUERY_CLI_TOOL

**Model restriction:** This API can be used only in the stage model.

<!--Device-cliManager-function queryToolSummaries(): Promise<Array<ToolSummary>>--><!--Device-cliManager-function queryToolSummaries(): Promise<Array<ToolSummary>>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[ToolSummary](arkts-ability-toolinfo-toolsummary-i-sys.md)&gt;&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 35600050 |

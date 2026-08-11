# getToolInfoByName (System API)

## Modules to Import

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## getToolInfoByName

```TypeScript
function getToolInfoByName(toolName: string): Promise<ToolInfo>
```

Get detailed information of a single tool by its name

**Since:** 26.0.0

**Required permissions:** ohos.permission.QUERY_CLI_TOOL

**Model restriction:** This API can be used only in the stage model.

<!--Device-cliManager-function getToolInfoByName(toolName: string): Promise<ToolInfo>--><!--Device-cliManager-function getToolInfoByName(toolName: string): Promise<ToolInfo>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| toolName | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[ToolInfo](arkts-ability-toolinfo-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| 35600030 |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 35600050 |

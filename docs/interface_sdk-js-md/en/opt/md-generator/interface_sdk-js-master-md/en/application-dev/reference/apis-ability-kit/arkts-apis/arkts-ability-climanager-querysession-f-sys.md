# querySession (System API)

## Modules to Import

```TypeScript
import { cliManager } from '@kit.AbilityKit';
```

## querySession

```TypeScript
function querySession(sessionId: string): Promise<CliSessionInfo>
```

Query session status.

**Since:** 26.0.0

**Deprecated since:** -1

**Required permissions:** ohos.permission.EXEC_CLI_TOOL

**Model restriction:** This API can be used only in the stage model.

<!--Device-cliManager-function querySession(sessionId: string): Promise<CliSessionInfo>--><!--Device-cliManager-function querySession(sessionId: string): Promise<CliSessionInfo>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| sessionId | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[CliSessionInfo](arkts-ability-climanager-clisessioninfo-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| 35600050 |
| 35600032 |

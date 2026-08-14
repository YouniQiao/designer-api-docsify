# execTool (System API)

## Modules to Import

```TypeScript
import { cliManager } from 'cliManager';
```

## execTool

```TypeScript
function execTool(toolName: string, subCommand: string, args: Record<string, Object>, challenge: string,
    execOptions?: ExecOptions): Promise<CliSessionInfo>
```

Execute a CLI command

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Deprecated since:** -1

**Required permissions:** ohos.permission.EXEC_CLI_TOOL

**Model restriction:** This API can be used only in the stage model.

<!--Device-cliManager-function execTool(toolName: string, subCommand: string, args: Record<string, Object>, challenge: string,    execOptions?: ExecOptions): Promise<CliSessionInfo>--><!--Device-cliManager-function execTool(toolName: string, subCommand: string, args: Record<string, Object>, challenge: string,    execOptions?: ExecOptions): Promise<CliSessionInfo>-End-->

**System capability:** SystemCapability.Ability.AgentRuntime.Core

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| toolName | string | Yes | The name of target tool. |
| subCommand | string | Yes | The subCommand of this execute action. |
| args | Record&lt;string, Object&gt; | Yes | The input args of tool. |
| challenge | string | Yes | The unique identifier get from access token manager. |
| execOptions | [ExecOptions](arkts-ability-climanager-execoptions-i-sys.md) | No | The options of this action. |

**Return value:**

| Type | Description |
| --- | --- |
| Promise&lt;[CliSessionInfo](arkts-ability-climanager-clisessioninfo-i-sys.md)&gt; | execute result. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 35600031 | Maximum number of processes has been reached. |
| 35600030 | No tool with the specified name exists. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied, interface caller does not have permission "ohos.permission.EXEC_CLI_TOOL". |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) | Not system application. Interface caller is not a system app. |
| 35600050 | System Error. 1. Connect to system service failed; 2. The system service failed to communicate with the dependent module. |


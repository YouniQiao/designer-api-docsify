# execTool（系统接口）

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## execTool

```TypeScript
function execTool(toolName: string, subCommand: string, args: Record<string, Object>, challenge: string,
    execOptions?: ExecOptions): Promise<CliSessionInfo>
```

Execute a CLI command

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**需要权限：** ohos.permission.EXEC_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cliManager-function execTool(toolName: string, subCommand: string, args: Record<string, Object>, challenge: string,    execOptions?: ExecOptions): Promise<CliSessionInfo>--><!--Device-cliManager-function execTool(toolName: string, subCommand: string, args: Record<string, Object>, challenge: string,    execOptions?: ExecOptions): Promise<CliSessionInfo>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| toolName | string | 是 | The name of target tool. |
| subCommand | string | 是 | The subCommand of this execute action. |
| args | [Record](../../apis-default/arkts-apis/arkts-record-t.md)&lt;string, Object&gt; | 是 | The input args of tool. |
| challenge | string | 是 | The unique identifier get from access token manager. |
| execOptions | [ExecOptions](arkts-ability-climanager-execoptions-i-sys.md) | 否 | The options of this action. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CliSessionInfo&gt; | execute result. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 35600031 | Maximum number of processes has been reached. |
| 35600030 | No tool with the specified name exists. |
| 201 | Permission denied, interface caller does not have permission "ohos.permission.EXEC_CLI_TOOL". |
| 202 | Not system application. Interface caller is not a system app. |
| 35600050 | System Error. 1. Connect to system service failed; 2. The system service failed to communicate with the dependent module. |


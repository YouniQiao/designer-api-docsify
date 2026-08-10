# execCmd（系统接口）

## 导入模块

```TypeScript
import { cliManager } from 'kits/@kit.AbilityKit';
```

## execCmd

```TypeScript
function execCmd(cmd: string, execCmdOptions?: ExecCmdOptions): Promise<CliSessionInfo>
```

Execute a command. This API uses a promise to return the result.

**起始版本：** 26.0.0

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为26.0.0。

**需要权限：** ohos.permission.EXEC_CLI_TOOL

**模型约束：** 此接口仅可在Stage模型下使用。

<!--Device-cliManager-function execCmd(cmd: string, execCmdOptions?: ExecCmdOptions): Promise<CliSessionInfo>--><!--Device-cliManager-function execCmd(cmd: string, execCmdOptions?: ExecCmdOptions): Promise<CliSessionInfo>-End-->

**系统能力：** SystemCapability.Ability.AgentRuntime.Core

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cmd | string | 是 | The command to execute. |
| execCmdOptions | [ExecCmdOptions](arkts-ability-climanager-execcmdoptions-i-sys.md) | 否 | The options of this action. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;CliSessionInfo&gt; | Promise used to return CliSessionInfo. |

**错误码：**

| 错误码ID | 错误信息 |
| --- | --- |
| 35600031 | Maximum number of processes has been reached. |
| 201 | Permission denied. |
| 202 | Not system application. |
| 35600050 | System Error. 1. Failed to connect to the system service; 2. The system service failed to communicate with the dependent module. |

